import os
import pandas as pd

files = os.listdir("data/raw")

for file in files:
    if file.endswith(".csv"):
        print("\n" + "="*50)
        print(file)

        df = pd.read_csv(f"data/raw/{file}")

        print("Shape:", df.shape)
        print("Columns:")
        print(df.columns.tolist())