#!/usr/bin/env python
from landprices.offer import LandOffer

o = LandOffer("source", "id_from_source", "link", "title", "location", "price", "area", "date_listed")
print(o)
print(o.source + "\t" + o.id_as_from_source + "\t" + o.link + "\t" + o.title + "\t" + o.location + "\t" + o.price + "\t" + o.area + "\t" + o.date_listed)
