-- ============================================================
-- Project: Bank Customer Retention & Risk Intelligence Platform
-- File: 02_churn_kpi_analysis.sql
-- Purpose: Churn KPI analysis using MySQL
-- Table: cleaned_dashboard_data
-- ============================================================

USE bank_churn_db;

-- ============================================================
-- 1. Churn count
-- ============================================================

SELECT 
    `Churn Flag`,
    COUNT(*) AS customer_count
FROM cleaned_dashboard_data
GROUP BY `Churn Flag`;


-- ============================================================
-- 2. Churn rate by customer segment
-- ============================================================

SELECT
    `Customer Segment`,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN `Churn Flag` = 1 THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        100.0 * SUM(CASE WHEN `Churn Flag` = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM cleaned_dashboard_data
GROUP BY `Customer Segment`
ORDER BY churn_rate_percentage DESC;


-- ============================================================
-- 3. Churn rate by gender
-- ============================================================

SELECT
    Gender,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN `Churn Flag` = 1 THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        100.0 * SUM(CASE WHEN `Churn Flag` = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM cleaned_dashboard_data
GROUP BY Gender
ORDER BY churn_rate_percentage DESC;


-- ============================================================
-- 4. Churn rate by number of complaints
-- ============================================================

SELECT
    NumComplaints,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN `Churn Flag` = 1 THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        100.0 * SUM(CASE WHEN `Churn Flag` = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM cleaned_dashboard_data
GROUP BY NumComplaints
ORDER BY CAST(NumComplaints AS UNSIGNED);
