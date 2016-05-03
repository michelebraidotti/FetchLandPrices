#!/usr/bin/env python
import landprices.fetcher
import landprices.fetcher.immobilien_scout24_fetcher
import landprices.fetcher.immobilio_fetcher
import landprices.fetcher.immonet_fetcher
import landprices.fetcher.immowelt_fetcher
import landprices.offer

fetchers = [landprices.fetcher.immobilien_scout24_fetcher.ImmobilienScout24Fetcher(),
            landprices.fetcher.immonet_fetcher.ImmonetFetcher(),
            landprices.fetcher.immowelt_fetcher.ImmoweltFetcher(),
            landprices.fetcher.immobilio_fetcher.ImmobilioFetcher()]
offers = []
for fetcher in fetchers:
    fetcher.fetch()
    offers += fetcher.get_results()
for o in offers:
    print(o.source + "\t" + o.location + "\t" + o.price + "\t" + o.date_listed)
