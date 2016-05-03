from landprices.fetcher.fetcher import AbstractFetcher
from landprices.offer import LandOffer


class ImmobilioFetcher(AbstractFetcher):
    def fetch(self):
        self.results.append(LandOffer(self.get_fetcher_name(), "gasgf", "fffff", "29/4/2016"))

    def get_fetcher_name(self):
        return 'Immobilio'