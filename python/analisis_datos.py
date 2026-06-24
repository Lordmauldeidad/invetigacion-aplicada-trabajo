import pandas as pd
import numpy as np
import os

def inspect_file(filepath, nrows=1000):
    print(f"=== Inspecting: {os.path.basename(filepath)} ===")
    try:
        # Load a small sample first
        df_sample = pd.read_csv(filepath, nrows=nrows)
        print("Columns:")
        print(df_sample.columns.tolist())
        print("\nData Types:")
        print(df_sample.dtypes)
        print("\nShape (estimated/sample):", df_sample.shape)
        print("\nFirst 3 rows:")
        print(df_sample.head(3))
        print("\nMissing values in sample:")
        print(df_sample.isnull().sum())
        print("-" * 50)
    except Exception as e:
        print(f"Error inspecting {filepath}: {e}")

if __name__ == "__main__":
    data_dir = "../data" if os.path.exists("../data") else "data"
    
    files = [
        "CardMasterListSeason18_12082020.csv",
        "Wincons.csv",
        "battlesStaging_12282020_WL_tagged.csv"
    ]
    
    for f in files:
        path = os.path.join(data_dir, f)
        if os.path.exists(path):
            inspect_file(path)
        else:
            print(f"File not found: {path}")
