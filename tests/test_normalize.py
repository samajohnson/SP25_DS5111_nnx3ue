
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
    # would be nice to try out the given/when/then comment style, just so you can see what that feels like
    processor = GainerProcessWSJ()
    processor.normalize()
    output_file = f'{download_dir}/norm_wsjgainers.csv'

    assert os.path.exists(output_file), "Normalize method did not create norm_wsjgainers.csv"

    df = pd.read_csv(output_file)
    expected_columns = ["Name", "Volume", "Price", "Price Change", "Price Percent Change"]
    assert list(df.columns) == expected_columns, "Normalize method did not produce expected columns"


def test_wsj_save_with_timestamp_creates_timed_csv():
    processor = GainerProcessWSJ()
    processor.save_with_timestamp()

    files = os.listdir(download_dir)
    timestamped_files = [f for f in files if 'wsjgainers' in f and datetime.now().strftime('%Y%m%d') in f]
    assert len(timestamped_files) > 0, "Save with timestamp method did not create a timestamped file"
