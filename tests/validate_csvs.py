#!/usr/bin/env python3
"""Validate every CSV in the dataset so a bad edit can never reach Kaggle.

Checks, in increasing strictness:
  1. every .csv parses as UTF-8 CSV with a sane header
  2. every row has the same number of fields as the header (strict files only)
  3. kaggle_dataset/tanzania_ushirika_master.csv matches its published schema
  4. kaggle_dataset/tanzania_ushirika_regional_analysis.csv has all 31 regions
     with plausible values (populations positive, percentages within 0-100)
  5. dataset-metadata.json is valid JSON with the required fields

Exit code 0 = all good, 1 = at least one failure (details printed).
"""
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "ushirika_statistics_data"
KAGGLE = DATA / "kaggle_dataset"

# Raw extractions with known column misalignment, kept for provenance only.
# They are excluded from the strict same-row-length check (never from parsing).
KNOWN_MISALIGNED = {
    "02_cooperatives_by_region_jul2024_jun2025.csv",
    "10_cooperatives_by_type_sep2021.csv",
    "11_new_cooperatives_fy2024_2025.csv",
}

REGIONS = {
    "Arusha", "Dar es Salaam", "Dodoma", "Geita", "Iringa", "Kagera",
    "Katavi", "Kigoma", "Kilimanjaro", "Lindi", "Manyara", "Mara", "Mbeya",
    "Morogoro", "Mtwara", "Mwanza", "Njombe", "Pwani", "Rukwa", "Ruvuma",
    "Shinyanga", "Simiyu", "Singida", "Songwe", "Tabora", "Tanga",
    "Mjini Magharibi", "Kaskazini Pemba", "Kusini Pemba",
    "Kaskazini Unguja", "Kusini Unguja",
}

MASTER_COLUMNS = ["category", "entity_type", "entity", "indicator",
                  "period", "value", "note", "source"]
MASTER_CATEGORIES = {
    "cooperatives", "finance_access", "risk", "impact_poverty",
    "impact_employment", "impact_inclusion", "agriculture_trade", "demography",
}
MASTER_ENTITY_TYPES = {
    "national", "region", "crop", "cooperative", "coop_type",
    "agro_input", "asset_type", "category",
}

errors = []


def err(msg):
    errors.append(msg)


def read_rows(path):
    try:
        with open(path, newline="", encoding="utf-8") as f:
            return list(csv.reader(f))
    except (UnicodeDecodeError, csv.Error) as e:
        err(f"{path.name}: cannot parse ({e})")
        return None


def check_generic(path, strict):
    rows = read_rows(path)
    if rows is None:
        return None
    if len(rows) < 2:
        err(f"{path.name}: fewer than 2 rows (header + data required)")
        return None
    header = rows[0]
    if any(not c.strip() for c in header):
        err(f"{path.name}: blank column name in header")
    if len(set(header)) != len(header):
        err(f"{path.name}: duplicate column names in header")
    if strict:
        for i, row in enumerate(rows[1:], start=2):
            if len(row) != len(header):
                err(f"{path.name}: line {i} has {len(row)} fields, "
                    f"header has {len(header)}")
    return rows


def as_float(s):
    try:
        return float(str(s).replace(",", ""))
    except ValueError:
        return None


def check_master(path):
    rows = check_generic(path, strict=True)
    if not rows:
        return
    header = rows[0]
    if header != MASTER_COLUMNS:
        err(f"{path.name}: header changed; expected {MASTER_COLUMNS}, "
            f"got {header}")
        return
    for i, row in enumerate(rows[1:], start=2):
        rec = dict(zip(header, row))
        if rec["category"] not in MASTER_CATEGORIES:
            err(f"{path.name}: line {i} unknown category {rec['category']!r}")
        if rec["entity_type"] not in MASTER_ENTITY_TYPES:
            err(f"{path.name}: line {i} unknown entity_type "
                f"{rec['entity_type']!r}")
        if not rec["entity"].strip():
            err(f"{path.name}: line {i} empty entity")
        if not rec["indicator"].strip():
            err(f"{path.name}: line {i} empty indicator")
        if not rec["value"].strip():
            err(f"{path.name}: line {i} empty value")
        if rec["entity_type"] == "region" and rec["entity"] not in REGIONS \
                and rec["entity"] != "TOTAL":
            err(f"{path.name}: line {i} unknown region {rec['entity']!r}")
        if rec["indicator"].endswith("_Pct"):
            v = as_float(rec["value"])
            if v is None or not 0 <= v <= 100:
                err(f"{path.name}: line {i} {rec['indicator']} value "
                    f"{rec['value']!r} is not a percentage")


def check_regional_wide(path):
    rows = check_generic(path, strict=True)
    if not rows:
        return
    header = rows[0]
    recs = [dict(zip(header, r)) for r in rows[1:]]
    names = {r.get("region", "") for r in recs}
    missing = REGIONS - names
    extra = names - REGIONS
    if missing:
        err(f"{path.name}: missing regions {sorted(missing)}")
    if extra:
        err(f"{path.name}: unknown regions {sorted(extra)}")
    for rec in recs:
        region = rec.get("region", "?")
        pop = as_float(rec.get("population_2022", ""))
        if pop is None or pop <= 0:
            err(f"{path.name}: {region} population_2022 invalid: "
                f"{rec.get('population_2022')!r}")
        for col, val in rec.items():
            if not val:
                continue
            if col.endswith("_pct") or "_pct_" in col:
                v = as_float(val)
                if v is None or not 0 <= v <= 100:
                    err(f"{path.name}: {region} {col}={val!r} "
                        f"is not a percentage")
            elif col not in ("region", "zone"):
                if as_float(val) is None:
                    err(f"{path.name}: {region} {col}={val!r} is not numeric")


def check_metadata(path):
    try:
        meta = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        err(f"{path.name}: invalid JSON ({e})")
        return
    for key in ("title", "id", "licenses"):
        if key not in meta:
            err(f"{path.name}: missing required key {key!r}")
    if "YOUR_KAGGLE_USERNAME" in meta.get("id", ""):
        print(f"WARNING: {path.name} still has the placeholder username; "
              "the publish job will refuse to push until it is set.")
    for res in meta.get("resources", []):
        p = path.parent / res.get("path", "")
        if not p.is_file():
            err(f"{path.name}: resource {res.get('path')!r} not found")


def main():
    if not DATA.is_dir():
        print(f"data directory not found: {DATA}")
        return 1

    for path in sorted(DATA.glob("*.csv")):
        check_generic(path, strict=path.name not in KNOWN_MISALIGNED)

    master = KAGGLE / "tanzania_ushirika_master.csv"
    wide = KAGGLE / "tanzania_ushirika_regional_analysis.csv"
    meta = KAGGLE / "dataset-metadata.json"
    for required in (master, wide, meta):
        if not required.is_file():
            err(f"missing required file: {required.relative_to(ROOT)}")

    if master.is_file():
        check_master(master)
    if wide.is_file():
        check_regional_wide(wide)
    if meta.is_file():
        check_metadata(meta)

    if errors:
        print(f"FAILED: {len(errors)} problem(s)")
        for e in errors:
            print(f"  - {e}")
        return 1
    csv_count = len(list(DATA.glob('*.csv'))) + len(list(KAGGLE.glob('*.csv')))
    print(f"OK: {csv_count} CSV files validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
