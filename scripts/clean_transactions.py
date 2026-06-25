import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print("Original:", df.shape)

# Date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.upper()
)

mapping = {
    "SIP": "SIP",
    "LUMPSUM": "Lumpsum",
    "REDEMPTION": "Redemption"
}

df["transaction_type"] = (
    df["transaction_type"]
    .replace(mapping)
)

# Amount Validation
invalid_amount = (
    df["amount_inr"] <= 0
).sum()

print("Invalid Amounts:", invalid_amount)

# KYC Check
valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

invalid_kyc = (
    ~df["kyc_status"].isin(valid_kyc)
).sum()

print("Invalid KYC:", invalid_kyc)

# Save
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Saved")