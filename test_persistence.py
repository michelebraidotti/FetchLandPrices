#!/usr/bin/env python
import time
from landprices.offer import LandOffer
from landprices.persistence.file_persistence import FilePersistence

offers = []
o = LandOffer("source", "id_from_source", "link", "title", "location", "price", "area", time.strftime("%Y-%m-%d"),
              False)
offers.append(o)
o1 = LandOffer("source1", "id_from_source1", "link1", "title1", "location1", "price1", "area1",
               time.strftime("%Y-%m-%d"), False)
offers.append(o1)
p = FilePersistence()
p.save_to_storage(offers)
loaded_offers = p.load_from_storage()
for o in loaded_offers:
    print(
        o.source + "\t" + o.id_as_from_source + "\t" + o.link + "\t" + o.title + "\t" + o.location + "\t" + o.price
        + "\t" + o.area + "\t" + o.date_retrived + "\t" + o.was_updated)
