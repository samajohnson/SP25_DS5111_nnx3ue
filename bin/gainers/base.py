"""
This module defines abstract base classes for gainer data processing.

It provides two abstract classes:
1. `GainerDownload` - Defines a blueprint for downloading gainer data.
2. `GainerProcess` - Defines a blueprint for processing and saving gainer data.
"""

from abc import ABC, abstractmethod

# DOWNLOADER
class GainerDownload(ABC):
    """
    Abstract base class for downloading gainer data.

    Attributes:
        url (str): The URL from which data will be downloaded.
    """
    def __init__(self, url: str):
        """
        Initializes the GainerDownload class with a URL.

        Args:
            url (str): The URL for downloading gainer data.
        """
        self.url = url

    @abstractmethod
    def download(self):
        """Abstract method to be implemented for downloading gainer data."""
        pass


# PROCESSOR
class GainerProcess(ABC):
    """
    Abstract base class for processing gainer data.

    This class defines the required methods for normalizing and saving data.
    """
    def __init__(self):
        """Initializes the GainerProcess class."""
        pass

    @abstractmethod
    def normalize(self):
        """Abstract method to be implemented for normalizing gainer data."""
        pass

    @abstractmethod
    def save_with_timestamp(self):
        """Abstract method to be implemented for saving data with a timestamp."""
        pass
