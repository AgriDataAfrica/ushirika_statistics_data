# Ushirika: Cooperatives and SACCOS in Tanzania

This dataset is about cooperatives in Tanzania (vyama vya ushirika). It covers AMCOS
(farmer marketing cooperatives), SACCOS (savings and credit cooperatives) and other
cooperative types. It also includes population, poverty and financial inclusion data
for each region, so you can study loan access, coverage gaps, risk and impact in one place.

All data comes from public official sources. They are listed at the bottom.

## Files

### 1. `tanzania_ushirika_master.csv`

Everything in one file, in long format. One row per observation, about 1,900 rows.
It holds the national numbers for 2019 to 2025 plus the regional tables: crop sales,
exports, jobs, risk and financial inclusion.

| Column | Meaning |
| ------ | ------- |
| `category` | `cooperatives`, `finance_access`, `risk`, `impact_poverty`, `impact_employment`, `impact_inclusion`, `agriculture_trade`, `demography` |
| `entity_type` | `national`, `region`, `crop`, `cooperative`, `coop_type`, `agro_input`, `asset_type`, `category` |
| `entity` | Region name, crop name, or `Tanzania` for national numbers |
| `indicator` | Name of the metric. Units are part of the name, like `_TZS_Billions`, `_Pct`, `_Tonnes` |
| `period` | Calendar year, fiscal year (July to June), or a month like `Dec-2023` |
| `value` | The number (a few are text, like the main crop of a region) |
| `note` | Benchmark or data quality note |
| `source` | Where the number comes from |

### 2. `tanzania_ushirika_regional_analysis.csv`

One row per region. All 31 regions (26 Mainland and 5 Zanzibar). Each row has:

- Population, area and density from the 2022 Census
- Number of cooperatives (June 2025), new ones in FY2024/25, cooperatives per 100k people, and cooperative jobs (December 2023)
- SACCOS numbers: registered vs licensed (December 2023 and June 2025), SACCOS per 100k people, capital, assets, loans and savings for 2023 in TZS billions, and loans per person
- Financial inclusion from FinScope 2023: percent banked, other formal, informal only, excluded, and formal inclusion in 2017 and 2023
- Poverty from HBS 2017/18: basic needs poverty, food poverty and the poverty gap

## Questions you can answer with this data

- Where do cooperatives help? Compare cooperative density or SACCOS loans per person with poverty and financial inclusion in each region.
- Where are the gaps? Some regions have few cooperatives and many excluded people. Singida has 53% formal inclusion and 41% excluded. Kigoma has about TZS 44 million in SACCOS loans for 2.47 million people.
- Who can get a loan? SACCOS loans reached TZS 1.11 trillion in 2023, but Dar es Salaam alone holds 70.4% of them. SACCOS serve about 1.8% of adults (0.6 million users in 2023, up from 0.4 million in 2017). Mobile money grew from 60% to 72% of adults in the same period.
- How risky is the sector? Bad loans (NPL) are 8.79% of all SACCOS loans. The rule says 5% at most. Assets that earn nothing are 13% against a 10% limit. Just 35 big SACCOS own 62.9% of all SACCOS assets. Only 69% of registered SACCOS have a licence, and in Kigoma, Lindi and Tabora it is below 30%.
- What is the impact? Cooperatives sold crops worth TZS 4.28 trillion in FY2024/25. The sector gives work to over 150,000 people. Women are 37.6% of SACCOS members and youth are 36%.

## How the data was checked

The numbers were checked against the original TCDC bulletins (September 2021 to June 2025),
the TCDC SACCOS Annual Report 2023 and the FinScope Tanzania 2023 report. Wrong values
were fixed. Values that could not be confirmed were removed.

## Things to keep in mind

1. Cooperative data uses fiscal years (July to June). NBS and BoT use calendar years.
2. TCDC regional data covers Mainland only (26 regions). FinScope and the Census also cover Zanzibar.
3. Poverty rates come from HBS 2017/18. Newer regional poverty numbers were not yet published.
4. Two FinScope regional values (Dar es Salaam excluded %, Rukwa informal %) were adjusted so each region sums to 100. See the `note` column.
5. SACCOS money figures cover the 884 licensed SACCOS that reported to TCDC, not all 1,283 registered ones.
6. FY2024/25 numbers are from the June 2025 TCDC bulletin and are not final.

## Sources

| Institution | Data |
| ----------- | ---- |
| Tanzania Cooperative Development Commission (TCDC), ushirika.go.tz | Cooperative and SACCOS registration, licences, crop sales, jobs; SACCOS Annual Report 2023 (money figures, bad loans, governance) |
| Bank of Tanzania, bot.go.tz | Banking supervision and financial inclusion reports, microfinance tiers |
| National Bureau of Statistics (NBS), nbs.go.tz | 2022 Census, Household Budget Survey 2017/18, Statistical Abstract 2024 |
| FinScope Tanzania 2023 (FSDT, BoT, NBS, OCGS), fsdt.or.tz | Financial inclusion and exclusion by region; use of SACCOS, mobile money and banks |
| Ministry of Agriculture, kilimo.go.tz | Agriculture annual report, crop production, inputs |
| Tanzania Coffee Board and Cashewnut Board of Tanzania | Coffee and cashew production and exports |
