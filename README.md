# Bank Customer Churn & Risk analysis

## Project Overview

This project analyzes banking customer churn using SQL, Python, and Power BI. The goal is to identify customer churn drivers, build a simple churn risk scoring system, and provide business recommendations for customer retention.

The project simulates a real banking analytics workflow: data cleaning, data quality checks, SQL analysis, Python validation, dashboard development, and executive reporting.

## Business Problem

Customer churn is a major issue for banks because losing existing customers can reduce long-term revenue, product usage, and customer lifetime value. This project investigates which customer characteristics are associated with churn and how the bank can identify high-risk customers before they leave.

## Tools Used

* Excel
* SQL / MySQL
* Python / Pandas
* Power BI
* GitHub

## Dataset

The dataset contains banking customer records with demographic, financial, product, complaint, and churn information.

Cleaned datasets were created for:

* Dashboard analysis
* Modeling/analytical use
* Summary outputs

Sensitive or unnecessary personal fields were excluded from cleaned analytical datasets.

## Key Metrics

| Metric                |   Value |
| --------------------- | ------: |
| Total Customers       | 115,640 |
| Churned Customers     |  14,094 |
| Non-Churned Customers | 101,546 |
| Churn Rate            |  12.19% |

## Key Findings

### 1. Complaint Risk

Customers with high complaint volume churn at 19.97%, compared with 4.20% for low-complaint customers. High-complaint customers are approximately 4.75 times more likely to churn.

### 2. Credit Score Risk

Poor-credit customers churn at 17.26%, compared with 3.84% for excellent-credit customers. This suggests credit score is a strong churn-risk indicator.

### 3. Product Engagement

Customers with only one product churn at 20.87%, while customers with five products churn at 4.40%. This suggests deeper product engagement is associated with stronger retention.

### 4. Risk Scoring System

A simple risk scoring system was created using:

* Complaint volume
* Credit score
* Number of products

| Risk Level    | Customers | Churned Customers | Churn Rate |
| ------------- | --------: | ----------------: | ---------: |
| High Risk     |     8,502 |             2,941 |     34.59% |
| Medium Risk   |    36,119 |             7,394 |     20.47% |
| Low Risk      |    49,392 |             3,552 |      7.19% |
| Very Low Risk |    21,627 |               207 |      0.96% |

High-risk customers churn at 34.59%, while very-low-risk customers churn at only 0.96%.

## Dashboard Pages

1. Executive Summary
2. Risk Driver Deep Dive
3. Risk Tier Action Plan
4. Business Recommendations

## Business Recommendations

The bank should prioritize high-risk customers for retention actions. Recommended actions include:

* Immediate complaint resolution for customers with 7+ complaints
* Cross-sell and onboarding campaigns for single-product customers
* Use poor credit score as a churn-risk warning signal
* Relationship manager outreach for high-risk customers
* Monitor churn risk by complaint level, credit score, and product engagement

## Repository Structure

```text
data/
dashboard/
python/
report/
screenshots/
sql/
```

## Project Notes and Limitations

* This dataset was selected because it contains diverse banking-related features, including customer demographics, income, credit score, outstanding loans, product usage, complaints, churn reason, and churn status. This made it suitable for SQL analysis, Python validation, and Power BI dashboard development.
* The raw dataset was large, so the file was stored in compressed format on GitHub. Cleaned datasets and summary output files were created separately to make the project easier to analyze and use in Power BI.
* This version of the project focuses on churn patterns, risk groups, and business recommendations. Outlier treatment was not deeply optimized in the first version. Future improvements could include outlier analysis for income, balance, credit score, and outstanding loans before advanced modeling.

## Project Status

Completed Version 1.0 — End-to-end banking churn analytics project using Excel, SQL, Python, Power BI, and GitHub.

## AI Assistance and Project Ownership

AI tools was used as a learning and development assistant for brainstorming, explaining technical concepts, reviewing and drafting code, debugging, and refining documentation. I directed the project work, selected the methods, executed and tested the workflows, reviewed the outputs, validated the reported results, and take responsibility for the final repository.
