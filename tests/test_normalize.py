
import sys
from pathlib import Path
sys.path.append('.')
from bin.gainers.wsj import GainerProcessWSJ
from bin.gainers.yahoo import GainerProcessYahoo
import os
from datetime import datetime
import pandas as pd
download_dir = 'downloaded_data'

def test_wsj_normalize():
    # Given a GainerProcessWSJ instance
    processor = GainerProcessWSJ()

    # When the normalize method is called
    processor.normalize()
    output_file = f'{download_dir}/norm_wsjgainers.csv'

    # Then a normalized CSV file should be created
    assert os.path.exists(output_file), "Normalize method did not create norm_wsjgainers.csv"

    # And the file should have the expected columns
    df = pd.read_csv(output_file)
    expected_columns = ["Name", "Volume", "Price", "Price Change", "Price Percent Change"]
    assert list(df.columns) == expected_columns, "Normalize method did not produce expected columns"


def test_wsj_save_with_timestamp_creates_timed_csv():
    # Given a GainerProcessWSJ instance
    processor = GainerProcessWSJ()

    # When the save_with_timestamp method is called
    processor.save_with_timestamp()

    # Then a CSV file with the current date in its name should be created
    files = os.listdir(download_dir)
    timestamped_files = [f for f in files if 'wsjgainers' in f and datetime.now().strftime('%Y%m%d') in f]
    assert len(timestamped_files) > 0, "Save with timestamp method did not create a timestamped file"
