import sys
from bin.gainers.factory import GainerFactory

class ProcessGainer:
    def __init__(self, gainer_downloader, gainer_normalizer):
        self.downloader = gainer_downloader
        self.normalizer = gainer_normalizer

    def _download(self):
        return self.downloader.download()

    def _normalize(self):
        self.normalizer.normalize()

    def _save_to_file(self):
        self.normalizer.save_with_timestamp()

    def process(self):
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
