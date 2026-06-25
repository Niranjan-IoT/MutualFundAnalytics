# Data Dictionary

## 01_fund_master.csv

| Column | Type | Description |
|----------|---------|------------|
| amfi_code | Integer | Unique fund identifier |
| fund_house | String | Mutual fund company |
| scheme_name | String | Fund name |
| category | String | Fund category |
| risk_category | String | Risk level |

## 02_nav_history.csv

| Column | Type | Description |
|----------|---------|------------|
| amfi_code | Integer | Fund identifier |
| date | Date | NAV date |
| nav | Float | Net Asset Value |