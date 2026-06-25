import pandas as pd
from sqlalchemy import create_engine, text

# Create database connection
engine = create_engine(
    "sqlite:///data/database/mutual_fund.db"
)

# Load tables

pd.read_csv(
    "data/raw/01_fund_master.csv"
).to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/nav_history_clean.csv"
).to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
).to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
).to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
).to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("All Tables Loaded")

# Validation

print("\n===== ROW COUNT VALIDATION =====")

with engine.connect() as conn:

    tables = [
        "dim_fund",
        "fact_nav",
        "fact_transactions",
        "fact_performance",
        "fact_aum"
    ]

    for table in tables:

        count = conn.execute(
            text(f"SELECT COUNT(*) FROM {table}")
        ).scalar()

        print(f"{table}: {count}")

        