# Mutual Fund Analytics Capstone Project

# Day 3 Report – Performance Analytics

**Intern:** Niranjan S

**Project:** Mutual Fund Analytics Platform

**Technology Stack**
- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Jupyter Notebook
- Git & GitHub

---

# Objective

The objective of Day 3 was to perform quantitative performance analysis on mutual fund schemes using historical NAV data. The analysis focused on measuring return, risk, benchmark performance, and generating a comprehensive scorecard for all funds.

---

# Datasets Used

| Dataset | Purpose |
|----------|---------|
|02_nav_history.csv|Historical NAV of 40 mutual funds|
|07_scheme_performance.csv|Expense Ratio, Alpha, Beta and Risk Metrics|
|10_benchmark_indices.csv|NIFTY50 and NIFTY100 benchmark indices|

---

# Task 1 – Daily Return Calculation

Daily return was calculated using the percentage change in NAV.

Formula

Daily Return = (Today's NAV / Previous Day NAV) − 1

The calculation was performed separately for all 40 mutual fund schemes using the AMFI code as the grouping key.

Output

daily_returns.csv

---

# Task 2 – CAGR Calculation

Compound Annual Growth Rate (CAGR) was calculated for:

- 1 Year
- 3 Years
- 5 Years

Formula

CAGR = (Ending NAV / Beginning NAV)^(1/n) − 1

The results were consolidated into a comparison table.

Output

cagr_summary.csv

---

# Task 3 – Sharpe Ratio

The Sharpe Ratio measures risk-adjusted return.

Formula

Sharpe Ratio =
(Rp − Rf)
/ Standard Deviation
× √252

Where

Risk Free Rate = 6.5%

Annual Trading Days = 252

Output

sharpe_ratio.csv

---

# Task 4 – Sortino Ratio

Sortino Ratio improves Sharpe Ratio by considering only downside volatility.

Formula

Sortino Ratio =
(Rp − Rf)
/ Downside Standard Deviation
× √252

Output

sortino_ratio.csv

---

# Task 5 – Alpha & Beta

Fund performance was compared against the NIFTY100 benchmark.

Python scipy.stats.linregress() was used to compute:

• Alpha

• Beta

Annual Alpha

Alpha = Intercept × 252

Output

alpha_beta.csv

---

# Task 6 – Maximum Drawdown

Maximum Drawdown measures the largest decline from a historical peak.

Formula

Maximum Drawdown =
Minimum(NAV / Running Maximum NAV − 1)

Output

drawdown_summary.csv

---

# Task 7 – Fund Scorecard

A composite score was created using weighted rankings.

Weight Distribution

30% → 3-Year CAGR

25% → Sharpe Ratio

20% → Alpha

15% → Expense Ratio (Inverse)

10% → Maximum Drawdown (Inverse)

Output

fund_scorecard.csv

---

# Task 8 – Benchmark Comparison

The Top 5 mutual funds were compared with the NIFTY100 benchmark.

Outputs

benchmark_comparison.png

tracking_error.csv

---

# Results

Successfully analyzed

• 40 Mutual Funds

• 46,000 NAV Records

• Multiple Benchmark Indices

Generated

• Daily Returns

• CAGR

• Sharpe Ratio

• Sortino Ratio

• Alpha

• Beta

• Maximum Drawdown

• Fund Scorecard

• Benchmark Comparison

---

# Technologies Used

Python

Pandas

NumPy

SciPy

Matplotlib

Jupyter Notebook

Git

GitHub

SQLite

---

# Learning Outcomes

- Financial performance analysis using Python
- Risk-adjusted return calculations
- Benchmark comparison techniques
- Portfolio performance evaluation
- Regression-based Alpha and Beta estimation
- Data visualization using Matplotlib
- Professional project documentation

---

# Deliverables

✔ Performance_Analytics.ipynb

✔ daily_returns.csv

✔ cagr_summary.csv

✔ sharpe_ratio.csv

✔ sortino_ratio.csv

✔ alpha_beta.csv

✔ drawdown_summary.csv

✔ fund_scorecard.csv

✔ tracking_error.csv

✔ benchmark_comparison.png

---

# GitHub Repository

https://github.com/Niranjan-IoT/MutualFundAnalytics

---

# Conclusion

The Day 3 implementation successfully transformed raw NAV data into actionable investment insights using quantitative finance techniques. The generated performance metrics, benchmark analysis, and composite scorecard provide a comprehensive evaluation framework for comparing mutual funds based on return, risk, and consistency.