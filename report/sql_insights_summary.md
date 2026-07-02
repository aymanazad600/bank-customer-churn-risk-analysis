# SQL Insights Summary

## 1. Overall Churn
The dataset contains 115,640 customers. Out of these, 14,094 customers churned and 101,546 customers did not churn. The overall churn rate is 12.19%.

## 2. Complaint Risk
Complaint volume appears to be one of the strongest churn indicators. Customers with no complaints have a churn rate of 2.98%, while customers with 10 complaints have a churn rate of 23.58%.
Customers with high complaint volume have a churn rate of 19.97%, compared with 4.20% for low-complaint customers. This means high-complaint customers are approximately 4.75 times more likely to churn.

## 3. Credit Score Risk
Poor-credit customers show the highest churn rate at 17.26%, compared with 3.84% for excellent-credit customers. This suggests credit score is a strong churn-risk indicator.
However, average balance and outstanding loans are similar across credit groups, so balance and loan amount alone do not appear to explain churn in this analysis.

## 4. Product Engagement
Product engagement is strongly related to churn. Customers with only one product have a churn rate of 20.87%, compared with 4.40% for customers with five products.
This suggests that deeper product relationships may improve retention, and single-product customers should be targeted for cross-sell or engagement campaigns.

## 5. Combined Risk Profile
Customers with high complaints, poor credit, and low product engagement have the highest churn rate at 34.59%.
In contrast, customers with low/medium complaints, non-poor credit, and high product engagement churn at only 0.96%.
This means the highest-risk customers are about 36 times more likely to churn.

## 6. Risk Tier System
The churn risk scoring system successfully separates customers into clear risk tiers:
| Risk Level    | Customers | Churned Customers | Churn Rate |
| ------------- | --------: | ----------------: | ---------: |
| High Risk     |     8,502 |             2,941 |     34.59% |
| Medium Risk   |    36,119 |             7,394 |     20.47% |
| Low Risk      |    49,392 |             3,552 |      7.19% |
| Very Low Risk |    21,627 |               207 |      0.96% |
This shows that complaints, poor credit score, and low product engagement together create a strong churn-risk profile.

## 7. Business Recommendations
The bank should prioritize the 8,502 high-risk customers for immediate retention action.

Recommended actions include:

* Resolve complaints quickly for high-complaint customers.
* Target single-product customers with cross-sell or engagement campaigns.
* Use poor credit score as a churn-risk warning signal.
* Assign relationship manager outreach to high-risk customers.
* Build a dashboard to monitor churn risk by complaint level, credit score, and product engagement.
