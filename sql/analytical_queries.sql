-- 1. Top 5 Funds by AUM

SELECT fund_house,
aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV by Fund

SELECT amfi_code,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Monthly Average NAV

SELECT strftime('%Y-%m', nav_date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 4. Total Transaction Amount by State

SELECT state,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 5. Funds with Expense Ratio < 1%

SELECT scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Average Return by Category

SELECT category,
AVG(return_3yr_pct) AS avg_return
FROM fact_performance
GROUP BY category;

-- 7. Top 10 Investors by Investment

SELECT investor_id,
SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY investor_id
ORDER BY total_investment DESC
LIMIT 10;

-- 8. Transaction Count by Type

SELECT transaction_type,
COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY transaction_type;

-- 9. Highest Rated Funds

SELECT scheme_name,
morningstar_rating
FROM fact_performance
ORDER BY morningstar_rating DESC;

-- 10. Average AUM by Fund House

SELECT fund_house,
AVG(aum_crore) AS avg_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY avg_aum DESC;
