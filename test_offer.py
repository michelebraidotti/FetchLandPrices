#!/usr/bin/env python
from landprices.offer import LandOffer

o = LandOffer("source", "id_from_source", "link", "title", "location", "price", "area", "date_retrieved", False)
print(o)
print(o.source + "\t" + o.id_as_from_source + "\t" + o.link + "\t" + o.title + "\t" + o.location + "\t" + o.price
      + "\t" + o.area + "\t" + o.date_retrieved + "\t" + str(o.was_updated))
o1 = LandOffer("source", "id_from_source", "link1", "title1", "location1", "price", "area1", "date_retrieved1", False)
o2 = LandOffer("source2", "id_from_source2", "link2", "title2", "location2", "price2", "area2", "date_retrieved2", False)
o3 = LandOffer("source", "id_from_source", "link3", "title3", "location3", "price3", "area3", "date_retrieved3", False)

s = "A String"
print("o1 = o1? " + str(o1.__eq__(o1)))
print("o = o1? " + str(o.__eq__(o1)))
print("o hash = o1 hash? " + str(o.__hash__() == o1.__hash__()))
print("o1 = o2? " + str(o1.__eq__(o2)))
print("o1 hash = o2 hash? " + str(o1.__hash__() == o2.__hash__()))
print("o = o3? " + str(o1.__eq__(o2)))
print("o hash = o3 hash? " + str(o1.__hash__() == o2.__hash__()))
print("o = s? " + str(o.__eq__(s)))
