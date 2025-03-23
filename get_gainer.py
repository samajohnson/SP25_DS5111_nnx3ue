"""
This module provides functionality to process gainer data by downloading, normalizing,
and saving it using a factory pattern.

The `ProcessGainer` class does this  by integrating a downloader and 
a normalizer, which are provided when the script is run.
"""

import sys
from bin.gainers.factory import GainerFactory


class ProcessGainer:
    """
    A class to handle the end-to-end processing of gainer data.

    This class:
    1. Downloads gainer data.
    2. Normalizes the data.
    3. Saves the processed data to a file with a timestamp.

    Attributes:
        downloader: An instance responsible for downloading gainer data.
        normalizer: An instance responsible for normalizing and saving data.
    """
    def __init__(self, gainer_downloader, gainer_normalizer):
        self.downloader = gainer_downloader
        self.normalizer = gainer_normalizer

    def _download(self):
        """Downloads gainer data."""
        return self.downloader.download()

    def _normalize(self):
        """Normalizes the downloaded gainer data."""
        self.normalizer.normalize()

    def _save_to_file(self):
        """Saves the normalized data to a file with a timestamp."""
        self.normalizer.save_with_timestamp()

    def process(self):
        """Executes the full gainer data processing pipeline."""
        input_csv_path = self._download()
        self._normalize()
        self._save_to_file()

if __name__=="__main__":
    choice = sys.argv[1]

    factory = GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()
    runner = ProcessGainer(downloader, normalizer)
    runner.process()
