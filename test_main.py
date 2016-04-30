#!/usr/bin/env python
import landprices.fetcher

fetchers = [landprices.fetcher.ImmobilienScout24Fetcher(), landprices.fetcher.ImmonetFetcher(),
            landprices.fetcher.ImmoweltFetcher(), landprices.fetcher.ImmobilioFetcher()]
offers = []
for fetcher in fetchers:
    fetcher.fetch()
    offers += fetcher.get_results()
for o in offers:
    print(o.source + "\t" + o.location + "\t" + o.price + "\t" + o.date_listed)
