import os
from .base import GainerDownload, GainerProcess
from datetime import datetime
from pathlib import Path
import pandas as pd



class GainerDownloadWSJ(GainerDownload):
    def __init__(self):
        self.url = 'www.wsj.com/market-data/stocks/us/movers'

    def download(self):
        # Step 1: Use headless Chrome to download the HTML page
        print(f"Downloading WSJ Gainers from {self.url} using headless Chrome...")
        # Run the headless chrome command using os.system
        command = f"sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 '{self.url}' > wsjgainers.html"
        os.system(command)

        # Check if the file was created
        if not os.path.exists('wsjgainers.html'):
            raise Exception("Failed to download the HTML page from WSJ")

        print("Successfully downloaded WSJ Gainers HTML to wsjgainers.html")
        raw = pd.read_html('wsjgainers.html')
        raw[0].to_csv('downloaded_data/wsjgainers.csv', index=False)
        print("Successfully saved WSJ Gainers HTML to wsjgainers.csv")


class GainerProcessWSJ(GainerProcess):
    def __init__(self):
        pass

    def normalize(self):
        print("Normalizing WSJ gainers")
        raw = pd.read_csv('downloaded_data/wsjgainers.csv')


    # Define expected columns mapping
        column_mapping = {
            "Unnamed: 0": "Name",
            "Last": "Price",
            "Chg": "Price Change",
            "% Chg": "Price Percent Change"
        }

    # Rename columns
        raw.rename(columns=column_mapping, inplace=True)

    # Enforce data types
        raw["Name"] = raw["Name"].astype(str)
        raw["Price"] = pd.to_numeric(raw["Price"], errors="coerce")
        raw["Price Change"] = pd.to_numeric(raw["Price Change"], errors="coerce")
        raw["Price Percent Change"] = pd.to_numeric(raw["Price Percent Change"], errors="coerce")

    # Save normalized CSV
        try:
            raw.to_csv('downloaded_data/norm_wsjgainers.csv', index=False)
            print(f"Normalized file saved")
        except Exception as e:
            print(f"Error saving the CSV file: {e}")
            return None


    def save_with_timestamp(self):
        print("Saving WSJ gainers")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        normalized_data = pd.read_csv('downloaded_data/norm_wsjgainers.csv')
        normalized_data.to_csv(f"downloaded_data/{timestamp}_norm_wsjgainers.csv", index=False)
        print(f"WSJ gainers saved with timestamp")
