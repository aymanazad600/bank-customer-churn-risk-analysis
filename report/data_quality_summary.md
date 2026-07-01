# Data Quality Summary

## Dataset Overview

Dataset: Botswana Bank Customer Churn  
Rows: 115,640  
Dashboard columns: 20  
Modeling columns: 18  
Target variable: Churn Flag  

## Data Quality Checks

| Check | Result |
|---|---:|
| Total rows | 115,640 |
| Dashboard columns | 20 |
| Modeling columns | 18 |
| Duplicate CustomerId count | 0 |
| Missing Churn Flag count | 0 |
| Missing Income count | 0 |
| Missing Credit Score count | 0 |
| Missing Balance count | 0 |
| Missing Customer Tenure count | 0 |
| Churned customers | 14,094 |
| Non-churned customers | 101,546 |
| Churn rate | 12.19% |

## Initial Findings

The dataset is clean overall. There are no duplicate customer IDs and no missing values in the key analytical columns. Churn Reason and Churn Date should be used only for dashboard and business explanation, not for predictive modeling, because they create data leakage.

Personal fields such as names, address, and contact information were excluded from the cleaned analytical datasets.
