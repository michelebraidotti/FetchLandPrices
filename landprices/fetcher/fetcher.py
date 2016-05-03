class AbstractFetcher:
    def __init__(self):
        self.results = []

    def get_results(self):
        return self.results

    def get_fetcher_name(self):
        raise NotImplementedError('Abstract method should not be used directly')

    def fetch(self):
        raise NotImplementedError('Abstract method should not be used directly')