#!/usr/bin/env python
import json
import time
from landprices.offer import LandOffer
from io import StringIO

def as_offer(dct):
    return LandOffer(dct['source'], dct['id_as_from_source'], dct['link'], dct['title'], dct['location'], dct['price'], dct['area'], dct['date_listed'])

offers = []
o = LandOffer("source", "id_from_source", "link", "title", "location", "price", "area", time.strftime("%Y-%m-%d"))
offers.append(o)
o1 = LandOffer("source1", "id_from_source1", "link1", "title1", "location1", "price1", "area1",
               time.strftime("%Y-%m-%d"))
offers.append(o1)
offers_dict = []
for o in offers:
    offers_dict.append(o.__dict__)
pretty_json_str = json.dumps(offers_dict, sort_keys=True, indent=4)
print(pretty_json_str)
io = StringIO(pretty_json_str)
read_back_offers = json.load(io, object_hook=as_offer)
for o in read_back_offers:
    print(
        o.source + "\t" + o.id_as_from_source + "\t" + o.link + "\t" + o.title + "\t" + o.location + "\t" + o.price + "\t" + o.area + "\t" + o.date_listed)

# The Last bit :)
# # Writing JSON data
# with open('data.json', 'w') as f:
#      json.dump(data, f)
#
# # Reading data back
# with open('data.json', 'r') as f:
#      data = json.load(f)
