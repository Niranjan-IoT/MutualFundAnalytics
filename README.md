# Mutual Fund Analytics

## Project Overview

Mutual Fund Analytics is a data engineering and analytics project focused on collecting, validating, and analyzing Indian mutual fund data.

The project demonstrates:

* Data ingestion using Python and Pandas
* Mutual fund NAV data collection through APIs
* AMFI code validation
* Data quality assessment
* Fund category and risk analysis
* Git and GitHub project management

---

## Project Structure

MutualFundAnalytics/

├── data/

│ ├── raw/

│ └── processed/

├── scripts/

│ ├── data_ingestion.py

│ ├── live_nav_fetch.py

│ ├── fund_master_analysis.py

│ └── amfi_validation.py

├── reports/

├── notebooks/

├── dashboard/

├── sql/

├── requirements.txt

└── README.md

---

## Datasets

### fund_master.csv

Contains:

* AMFI Code
* Fund House
* Scheme Name
* Category
* Sub Category
* Expense Ratio
* Fund Manager
* Risk Category

### nav_history.csv

Contains:

* AMFI Code
* NAV
* Date

---

## Technologies Used

* Python
* Pandas
* NumPy
* Requests
* Jupyter Notebook
* Git
* GitHub

---

## Data Ingestion

The data_ingestion.py script:

* Loads all datasets
* Displays dataset shape
* Displays column data types
* Displays sample records
* Helps identify anomalies

---

## Live NAV Collection

The live_nav_fetch.py script retrieves historical NAV information using mutual fund APIs.

Schemes fetched:

* SBI Bluechip
* ICICI Bluechip
* Nippon Large Cap
* Axis Bluechip
* Kotak Bluechip

---

## Fund Master Analysis

The fund_master_analysis.py script explores:

* Fund Houses
* Categories
* Sub Categories
* Risk Categories
* Scheme distribution

---

## AMFI Validation

The amfi_validation.py script:

* Validates AMFI codes
* Identifies missing codes
* Checks duplicates
* Evaluates data quality

---

## Key Findings

* Multiple fund houses available
* Equity and Debt categories dominate the dataset
* Large Cap, Mid Cap, Small Cap and ELSS schemes identified
* Risk categories successfully classified
* AMFI validation performed successfully

---

## Future Enhancements

* Power BI Dashboard
* SQL Data Warehouse
* Automated ETL Pipeline
* Portfolio Recommendation Engine
* Mutual Fund Performance Analytics

---

## Author

Niranjan

GitHub:
https://github.com/Niranjan-IoT
