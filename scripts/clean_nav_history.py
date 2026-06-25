import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Date conversion
df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

# Sort
df = df.sort_values(
    ["amfi_code", "date"]
)

# Forward fill NAV
df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
)

# Remove duplicates
df = df.drop_duplicates()

# NAV validation
invalid_nav = df[df["nav"] <= 0]

print("Invalid NAV Records:", len(invalid_nav))

# Save
df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("Clean Shape:", df.shape)
print("Saved Successfully")