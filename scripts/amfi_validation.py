import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Convert codes to string for safe comparison
fund_master["amfi_code"] = fund_master["amfi_code"].astype(str)
nav_history["amfi_code"] = nav_history["amfi_code"].astype(str)

# Unique AMFI codes
master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Missing codes
missing_codes = master_codes - nav_codes

# Duplicate checks
duplicate_master = fund_master["amfi_code"].duplicated().sum()
duplicate_nav = nav_history["amfi_code"].duplicated().sum()

# Missing values
missing_master = fund_master.isnull().sum().sum()
missing_nav = nav_history.isnull().sum().sum()

print("\n========== DATA QUALITY SUMMARY ==========")

print(f"Total Fund Master Codes : {len(master_codes)}")
print(f"Total NAV Codes         : {len(nav_codes)}")
print(f"Missing Codes           : {len(missing_codes)}")

print(f"\nDuplicate Codes in Fund Master : {duplicate_master}")
print(f"Duplicate Codes in NAV History : {duplicate_nav}")

print(f"\nMissing Values in Fund Master : {missing_master}")
print(f"Missing Values in NAV History : {missing_nav}")

if len(missing_codes) > 0:
    print("\nMissing AMFI Codes:")
    for code in list(missing_codes)[:20]:
        print(code)

print("\nValidation Complete")