# Tanzania Cooperatives & SACCOS: Access, Risk & Impact (2019-2025)

A combined dataset on Tanzanian cooperatives (vyama vya ushirika), covering AMCOS
(agricultural marketing cooperatives), SACCOS (savings and credit cooperatives) and other
cooperative types, merged with population, poverty and financial inclusion data. The goal
is to let you study coverage gaps, loan access, risk and impact in one place.

All data comes from publicly available official sources (listed at the bottom).

## Files

### 1. `tanzania_ushirika_master.csv`

Everything in one file, tidy/long format. One row per observation, about 1,900 rows in
total: national time series (2019 to 2025), regional breakdowns, crop sales, exports,
employment, risk indicators and financial inclusion.

| Column | Description |
|--------|-------------|
| `category` | `cooperatives`, `finance_access`, `risk`, `impact_poverty`, `impact_employment`, `impact_inclusion`, `agriculture_trade`, `demography` |
| `entity_type` | `national`, `region`, `crop`, `cooperative`, `coop_type`, `agro_input`, `asset_type`, `category` |
| `entity` | Region name, crop name, or `Tanzania` for national figures |
| `indicator` | Metric name; units are part of the name, e.g. `_TZS_Billions`, `_Pct`, `_Tonnes` |
| `period` | Calendar year, fiscal year (July to June), or month snapshot such as `Dec-2023` |
| `value` | Numeric value (a few are text, e.g. main crop per region) |
| `note` | Benchmark or data quality note |
| `source` | Originating institution or report |

### 2. `tanzania_ushirika_regional_analysis.csv`

One row per region, all 31 regions (26 Mainland plus 5 Zanzibar), with aligned indicators:

- Demography: 2022 Census population, area, density
- Cooperative coverage: total cooperatives (June 2025), new registrations FY2024/25, cooperatives per 100k people, cooperative employment (December 2023)
- SACCOS and loan access: registered vs licensed SACCOS (December 2023 and June 2025), SACCOS per 100k people, core capital, assets, loans outstanding and savings for 2023 in TZS billions, loans per capita
- Financial inclusion (FinScope 2023): percent banked, other formal, informal only and financially excluded, plus formal inclusion in 2017 and 2023
- Poverty (HBS 2017/18): basic needs poverty rate, food (extreme) poverty rate, poverty gap

## Questions this dataset can answer

- Where do cooperatives help? Correlate cooperative density or SACCOS loans per capita with poverty and financial inclusion by region.
- Where are the gaps? Some regions have both few cooperatives per 100k people and high financial exclusion. Singida sits at 53% formal inclusion with 41% excluded. Kigoma has about TZS 44 million in SACCOS loans for 2.47 million people.
- Who can get a loan? SACCOS loans outstanding reached TZS 1.11 trillion in 2023, but Dar es Salaam alone holds 70.4% of them. SACCOS serve roughly 1.8% of adults (0.6 million users in 2023, up from 0.4 million in 2017), while mobile money grew from 60% to 72% of adults.
- How risky is the sector? The SACCOS NPL ratio is 8.79% against a 5% prudential standard. Non-earning assets are 13% against a 10% maximum. 35 large SACCOS own 62.9% of all SACCOS assets, and only 69% of registered SACCOS are licensed (as low as 26 to 29% in Kigoma, Lindi and Tabora).
- What is the impact? Cooperative crop sales hit TZS 4.28 trillion in FY2024/25. The sector employs over 150,000 people. Women are 37.6% of SACCOS members, youth 36%.

## Verification

Figures were cross-checked against the original TCDC statistical bulletins (September 2021
through June 2025), the TCDC SACCOS Annual Performance Report 2023 and the FinScope
Tanzania 2023 report. Values that contradicted the primary source were corrected; values
that could not be confirmed were removed.

## Caveats

1. Cooperative data uses fiscal years (July to June); NBS and BoT use calendar years.
2. TCDC regional data covers Mainland only (26 regions); FinScope and the Census also cover Zanzibar.
3. Poverty rates come from HBS 2017/18, the latest published regional figures at compile time.
4. Two FinScope regional values (Dar es Salaam excluded %, Rukwa informal %) were adjusted so the access strand sums to 100; see the `note` column.
5. SACCOS financials reflect the 884 licensed SACCOS that reported to TCDC, not all 1,283 registered.
6. FY2024/25 figures are provisional (TCDC bulletin, June 2025).

## Sources

| Institution | Data |
|---|---|
| Tanzania Cooperative Development Commission (TCDC), ushirika.go.tz | Cooperative and SACCOS registration, licensing, crop sales, employment; SACCOS Annual Performance Report 2023 (financials, NPL, governance) |
| Bank of Tanzania, bot.go.tz | Banking supervision and financial inclusion reports, microfinance tiers |
| National Bureau of Statistics (NBS), nbs.go.tz | 2022 Population and Housing Census, Household Budget Survey 2017/18, Statistical Abstract 2024 |
| FinScope Tanzania 2023 (FSDT, BoT, NBS, OCGS), fsdt.or.tz | Financial inclusion and exclusion by region; uptake of SACCOS, mobile money and banks |
| Ministry of Agriculture, kilimo.go.tz | Agriculture annual report, crop production, inputs |
| Tanzania Coffee Board and Cashewnut Board of Tanzania | Coffee and cashew production and exports |
