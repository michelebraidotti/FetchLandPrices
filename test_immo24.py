#!/usr/bin/env python
import landprices.fetcher.immobilien_scout24_fetcher

is24 = landprices.fetcher.immobilien_scout24_fetcher.ImmobilienScout24Fetcher()
is24.fetch();
for o in is24.get_results():
    print(o.source + "\t" + o.id_as_from_source + "\t" + o.link + "\t" + o.title + "\t" + o.location + "\t" + o.price + "\t" + o.area + "\t" + o.date_listed)
