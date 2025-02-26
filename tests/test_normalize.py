
import sys
from pathlib import Path
sys.path.append('.')

import bin.normalize_csv as normalize

def test_normalize():
    csv_path = Path(__file__).parent.parent / "ygainers.csv"
#    csv_path = '/home/runner/work/SP25_DS5111_nnx3ue/ygainers.csv'
    df = normalize.normalize_csv(str(csv_path))
    #df = normalize.normalize_csv("ygainers.csv")

    # Expected columns after normalization
    expected_columns = ["symbol", "price", "price_change", "price_percent_change"]
    assert list(df.columns) == expected_columns, f"Unexpected columns: {df.columns}"



