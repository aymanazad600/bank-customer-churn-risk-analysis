import pandas as pd
from pathlib import Path


# Updated to use your new Desktop path
file_path = "/Users/ayman/Desktop/cleaned_dashboard_data.csv"

df = pd.read_csv(file_path)
df.head()

# Run the quality checks
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Value Counts:\n{df['Churn Flag'].value_counts()}")
print(f"Churn Rate: {df['Churn Flag'].mean() * 100:.2f}%")

# Complaint risk analysis

complaint_summary = (
    df.groupby("NumComplaints")
    .agg(
        total_customers=("CustomerId", "count"),
        churned_customers=("Churn Flag", "sum"),
        churn_rate_percentage=("Churn Flag", lambda x: round(x.mean() * 100, 2))
    )
    .reset_index()
)

print(complaint_summary)


# Complaint risk groups

df["Complaint Risk Group"] = df["NumComplaints"].apply(
    lambda x: "Low Complaints" if x <= 2
    else "Medium Complaints" if x <= 6
    else "High Complaints"
)

complaint_group_summary = (
    df.groupby("Complaint Risk Group")
    .agg(
        total_customers=("CustomerId", "count"),
        churned_customers=("Churn Flag", "sum"),
        churn_rate_percentage=("Churn Flag", lambda x: round(x.mean() * 100, 2))
    )
    .reset_index()
    .sort_values("churn_rate_percentage", ascending=False)
)

print(complaint_group_summary)


# Credit score risk analysis

def credit_group(score):
    if score < 580:
        return "Poor Credit"
    elif score <= 669:
        return "Fair Credit"
    elif score <= 739:
        return "Good Credit"
    elif score <= 799:
        return "Very Good Credit"
    else:
        return "Excellent Credit"

df["Credit Score Group"] = df["Credit Score"].apply(credit_group)

credit_summary = (
    df.groupby("Credit Score Group")
    .agg(
        total_customers=("CustomerId", "count"),
        churned_customers=("Churn Flag", "sum"),
        churn_rate_percentage=("Churn Flag", lambda x: round(x.mean() * 100, 2)),
        avg_balance=("Balance", lambda x: round(x.mean(), 2)),
        avg_outstanding_loans=("Outstanding Loans", lambda x: round(x.mean(), 2))
    )
    .reset_index()
    .sort_values("churn_rate_percentage", ascending=False)
)

print(credit_summary)
print(credit_summary.to_string(index=False))


# Product engagement analysis

product_summary = (
    df.groupby("NumOfProducts")
    .agg(
        total_customers=("CustomerId", "count"),
        churned_customers=("Churn Flag", "sum"),
        churn_rate_percentage=("Churn Flag", lambda x: round(x.mean() * 100, 2)),
        avg_complaints=("NumComplaints", lambda x: round(x.mean(), 2)),
        avg_credit_score=("Credit Score", lambda x: round(x.mean(), 2)),
        avg_balance=("Balance", lambda x: round(x.mean(), 2))
    )
    .reset_index()
    .sort_values("NumOfProducts")
)

print(product_summary.to_string(index=False))


# Combined churn risk profile

df["Complaint Group"] = df["NumComplaints"].apply(
    lambda x: "High Complaints" if x >= 7 else "Low/Medium Complaints"
)

df["Credit Group"] = df["Credit Score"].apply(
    lambda x: "Poor Credit" if x < 580 else "Non-Poor Credit"
)

df["Product Group"] = df["NumOfProducts"].apply(
    lambda x: "Low Product Engagement" if x <= 2 else "High Product Engagement"
)

risk_profile_summary = (
    df.groupby(["Complaint Group", "Credit Group", "Product Group"])
    .agg(
        total_customers=("CustomerId", "count"),
        churned_customers=("Churn Flag", "sum"),
        churn_rate_percentage=("Churn Flag", lambda x: round(x.mean() * 100, 2))
    )
    .reset_index()
    .sort_values("churn_rate_percentage", ascending=False)
)

print(risk_profile_summary.to_string(index=False))

# Churn risk scoring system

df["Risk Score"] = (
    (df["NumComplaints"] >= 7).astype(int)
    + (df["Credit Score"] < 580).astype(int)
    + (df["NumOfProducts"] <= 2).astype(int)
)

def risk_level(score):
    if score == 3:
        return "High Risk"
    elif score == 2:
        return "Medium Risk"
    elif score == 1:
        return "Low Risk"
    else:
        return "Very Low Risk"

df["Risk Level"] = df["Risk Score"].apply(risk_level)

risk_tier_summary = (
    df.groupby(["Risk Score", "Risk Level"])
    .agg(
        total_customers=("CustomerId", "count"),
        churned_customers=("Churn Flag", "sum"),
        churn_rate_percentage=("Churn Flag", lambda x: round(x.mean() * 100, 2))
    )
    .reset_index()
    .sort_values("Risk Score", ascending=False)
)

print(risk_tier_summary.to_string(index=False))


output_dir = Path("data/analysis_outputs")
output_dir.mkdir(parents=True, exist_ok=True)
complaint_group_summary.to_csv(output_dir / "complaint_group_summary.csv", index=False)
credit_summary.to_csv(output_dir / "credit_score_summary.csv", index=False)
product_summary.to_csv(output_dir / "product_engagement_summary.csv", index=False)
risk_profile_summary.to_csv(output_dir / "risk_profile_summary.csv", index=False)
risk_tier_summary.to_csv(output_dir / "risk_tier_summary.csv", index=False)