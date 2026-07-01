-- 1. Total rows
SELECT COUNT(*) AS total_rows
FROM cleaned_dashboard_data;

-- 2. Churned vs non-churned customers
SELECT 
    "Churn Flag",
    COUNT(*) AS customer_count
FROM cleaned_dashboard_data
GROUP BY "Churn Flag";

-- 3. Churn rate
SELECT 
    ROUND(
        100.0 * SUM(CASE WHEN "Churn Flag" = 'Yes' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM cleaned_dashboard_data;

-- 4. Duplicate customer IDs
SELECT 
    CustomerId,
    COUNT(*) AS duplicate_count
FROM cleaned_dashboard_data
GROUP BY CustomerId
HAVING COUNT(*) > 1;

-- 5. Missing value check
SELECT
    SUM(CASE WHEN Income IS NULL THEN 1 ELSE 0 END) AS missing_income,
    SUM(CASE WHEN "Credit Score" IS NULL THEN 1 ELSE 0 END) AS missing_credit_score,
    SUM(CASE WHEN Balance IS NULL THEN 1 ELSE 0 END) AS missing_balance,
    SUM(CASE WHEN "Customer Tenure" IS NULL THEN 1 ELSE 0 END) AS missing_customer_tenure
FROM cleaned_dashboard_data;
