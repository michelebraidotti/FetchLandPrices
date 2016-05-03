from landprices.fetcher.fetcher import AbstractFetcher
from landprices.offer import LandOffer


class ImmonetFetcher(AbstractFetcher):
    def fetch(self):
        self.results.append(LandOffer(self.get_fetcher_name(), "asdfadfa", "fadsfa", "30/4/2016"))

    def get_fetcher_name(self):
        return 'Immonet'