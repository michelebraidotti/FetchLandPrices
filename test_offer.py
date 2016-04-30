#!/usr/bin/env python
from landprices.offer import LandOffer

o = LandOffer("gadsfadsf", "fasdfad", "fadfa", "fadsfa")
print(o)
print(o.source + "\t" + o.location + "\t" + o.price + "\t" + o.date_listed)
