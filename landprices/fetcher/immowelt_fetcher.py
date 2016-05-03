from landprices.fetcher.fetcher import AbstractFetcher
from landprices.offer import LandOffer


class ImmoweltFetcher(AbstractFetcher):
    def fetch(self):
        self.results.append(LandOffer(self.get_fetcher_name(), "yeruu", "zzxsss", "10/4/2016"))

    def get_fetcher_name(self):
        return 'Immowelt'
