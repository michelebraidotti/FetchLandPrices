from landprices.offer import LandOffer


class AbstractFetcher:
    def __init__(self):
        self.results = []

    def get_results(self):
        return self.results

    def get_fetcher_name(self):
        raise NotImplementedError('Abstract method should not be used directly')

    def fetch(self):
        raise NotImplementedError('Abstract method should not be used directly')


class ImmobilienScout24Fetcher(AbstractFetcher):
    def fetch(self):
        o = LandOffer(self.get_fetcher_name(), "Buch", "1 buck", "30/4/2016")
        self.results.append(o)
        o1 = LandOffer(self.get_fetcher_name(), "Zepernick", "3 bucks", "30/4/2016")
        self.results.append(o1)

    def get_fetcher_name(self):
        return 'ImmobilienScout24'


class ImmonetFetcher(AbstractFetcher):
    def fetch(self):
        self.results.append(LandOffer(self.get_fetcher_name(), "asdfadfa", "fadsfa", "30/4/2016"))

    def get_fetcher_name(self):
        return 'Immonet'


class ImmoweltFetcher(AbstractFetcher):
    def fetch(self):
        self.results.append(LandOffer(self.get_fetcher_name(), "yeruu", "zzxsss", "10/4/2016"))

    def get_fetcher_name(self):
        return 'Immowelt'


class ImmobilioFetcher(AbstractFetcher):
    def fetch(self):
        self.results.append(LandOffer(self.get_fetcher_name(), "gasgf", "fffff", "29/4/2016"))

    def get_fetcher_name(self):
        return 'Immobilio'
