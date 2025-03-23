"""
Factory module to create the appropriate downloader and processor based on user choice.
This module contains the `GainerFactory` class that is responsible for creating
and returning the correct downloader and processor for various gainer data sources 
such as Yahoo or WSJ. The correct classes are chosen based on the input choice provided
to the factory.
"""

#from .yahoo import GainerDownloadYahoo, GainerProcessYahoo
#from .wsj import GainerDownloadWSJ, GainerProcessWSJ
from bin.gainers.wsj import GainerDownloadWSJ, GainerProcessWSJ
from bin.gainers.yahoo import GainerDownloadYahoo, GainerProcessYahoo

class GainerFactory:
    """
    Factory class to create the appropriate downloader and processor
    based on the selected 'choice'. This class provides methods to 
    retrieve the correct downloader and processor for different types
    of gainer data sources.
    """
    def __init__(self, choice):
        """
        Initialize the GainerFactory with the given choice.

        :param choice: A string indicating the type of gainer ('yahoo', 'wsj', 'test')
        :raises AssertionError: If the choice is not one of the valid types.
        """
        assert choice in ['yahoo', 'wsj', 'test'], f"Unrecognized gainer type {choice}"
        self.choice = choice

    def get_downloader(self):
        """
        Returns the appropriate downloader based on the choice.

        :returns: The correct GainerDownload class (Yahoo or WSJ).
        """
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        if self.choice == 'wsj':
            return GainerDownloadWSJ()

    def get_processor(self):
        """
        Returns the appropriate processor based on the choice.

        :returns: The correct GainerProcess class (Yahoo or WSJ).
        """
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerProcessYahoo()
        if self.choice == 'wsj':
            return GainerProcessWSJ()
