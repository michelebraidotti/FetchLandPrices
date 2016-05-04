#!/usr/bin/env python

import landprices.fetcher.immobilien_scout24_fetcher
from landprices.persistence.file_persistence import FilePersistence

is24 = landprices.fetcher.immobilien_scout24_fetcher.ImmobilienScout24Fetcher()
is24.fetch();
p = FilePersistence()
previously_saved_offers = p.load_from_storage()
new_offers_set = set(list(is24.get_results() + previously_saved_offers))
p.save_to_storage(list(new_offers_set))
