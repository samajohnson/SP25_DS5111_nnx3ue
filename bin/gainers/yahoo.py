"""
Module for downloading, processing, and saving Yahoo Gainers data.
This module contains the `GainerDownloadYahoo` class for downloading the data 
using headless Chrome and the `GainerProcessYahoo` class for normalizing and 
saving the data.
"""
import os
import pandas as pd
from datetime import datetime
from .base import GainerDownload, GainerProcess


class GainerDownloadYahoo(GainerDownload):
    """
    A class to download the Yahoo Gainers data using headless Chrome.
    Inherits from GainerDownload and implements the download method.
    """
    def __init__(self):
        """
        Initializes the GainerDownloadYahoo with the Yahoo Finance URL.
        """
        self.url = 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200'

    def download(self):
        """
        Downloads the Yahoo Gainers HTML page using headless Chrome 
        and saves the content as an HTML file, then converts it to CSV.

        :raises Exception: If downloading the page fails.
        """
        # Step 1: Use headless Chrome to download the HTML page
        print(f"Downloading Yahoo Gainers from {self.url} using headless Chrome...")
        # Run the headless chrome command using os.system
        command = f"sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 '{self.url}' > ygainers.html"
        os.system(command)

        # Check if the file was created
        if not os.path.exists('ygainers.html'):
            raise Exception("Failed to download the HTML page from Yahoo Finance")

        print("Successfully downloaded Yahoo Gainers HTML to ygainers.html")
        raw = pd.read_html('ygainers.html')
        raw[0].to_csv('downloaded_data/ygainers.csv', index=False)
        print("Successfully saved Yahoo Gainers HTML to ygainers.csv")

        # Return the path to the CSV file
        return 'ygainers.csv'


class GainerProcessYahoo(GainerProcess):
    """
    A class to process the Yahoo Gainers data by normalizing and saving it.
    Inherits from GainerProcess and implements the normalize and save_with_timestamp methods.
    """
    def __init__(self):
        """
        Initializes the GainerProcessYahoo class.
        """
        pass

    def normalize(self):
        """
        Normalizes the Yahoo Gainers data by renaming columns, enforcing data types, 
        and saving it as a CSV.

        :raises Exception: If saving the normalized CSV file fails.
        """
        print("Normalizing yahoo gainers")
        raw = pd.read_csv('downloaded_data/ygainers.csv')

        raw = raw[["Name", "Volume", "Price", "Change", "Change %"]]
        raw['Price'] = raw['Price'].str.split(' ').str[0]
        raw['Change %'] = raw['Change %'].str[1:-1]
    # Define expected columns mapping
        column_mapping = {
            "Change": "Price Change",
            "Change %": "Price Percent Change"
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
            raw.to_csv('downloaded_data/norm_ygainers.csv', index=False)
            print(f"Normalized file saved")
        except Exception as e:
            print(f"Error saving the CSV file: {e}")
            return None


    def save_with_timestamp(self):
        """
        Saves the normalized Yahoo Gainers data with a timestamp in the filename.

        :raises Exception: If saving the timestamped file fails.
        """
        print("Saving Yahoo gainers")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        normalized_data = pd.read_csv('downloaded_data/norm_ygainers.csv')
        normalized_data.to_csv(f"downloaded_data/{timestamp}_norm_ygainers.csv", index=False)
        print(f"Yahoo gainers saved with timestamp")

