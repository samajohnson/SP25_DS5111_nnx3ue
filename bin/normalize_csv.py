"""
normalize_csv.py

This module normalizes input csvs to be the same format.

Author: Sam Johnosn
Date: 2000-02-17
"""



import sys
from pathlib import Path
import pandas as pd

def normalize_csv(input_csv_path: str):
    '''
    Reads a raw CSV file, extracts and renames relevant columns,
    enforces data types, and saves a normalized version with `_norm` appended.

    Parameters:
    -----------
    input_csv_path: str
    Path to the input csv trying to normalize (ex: ygainers.csv, wjsgainers.csv)

    '''
    # Ensure file exists
    input_path = Path(input_csv_path)
    assert input_path.exists(), f"File not found: {input_csv_path}"

    # Define expected columns mapping
    column_mapping = {
        "Symbol": "symbol",
        "Price": "price",
        "Change": "price_change",
        "Change %": "price_percent_change"
    }

    # Read raw CSV
    df = pd.read_csv(input_csv_path, usecols=column_mapping.keys())

    # Rename columns
    df.rename(columns=column_mapping, inplace=True)

    # Enforce data types
    df["symbol"] = df["symbol"].astype(str)
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["price_change"] = pd.to_numeric(df["price_change"], errors="coerce")
    df["price_percent_change"] = pd.to_numeric(df["price_percent_change"], errors="coerce")

    # Define output path
    output_csv_path = input_path.with_stem(input_path.stem + "_norm")

    # Save normalized CSV
    df.to_csv(output_csv_path, index=False)
    print(f"Normalized file saved: {output_csv_path}")
    return df

if __name__ == "__main__":
    assert len(sys.argv) == 2, "Usage: python bin/normalize_csv.py <path to raw gainers csv>"
    normalize_csv(sys.argv[1])
