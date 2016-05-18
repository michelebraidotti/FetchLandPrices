from landprices.offer import LandOffer

old_offers = []
new_offers = []
merged_offers = LandOffer.merge_offers(old_offers, new_offers)
assert len(merged_offers) == 0

old = LandOffer("source", "id_from_source", "link", "title", "location", "price", "area", "date_retrieved", False)
old1 = LandOffer("source1", "id_from_source1", "link1", "title1", "location1", "price1", "area1", "date_retrieved1", False)
old2 = LandOffer("source2", "id_from_source2", "link2", "title2", "location2", "price2", "area2", "date_retrieved2", False)
old3 = LandOffer("source3", "id_from_source3", "link3", "title3", "location3", "price3", "area3", "date_retrieved3", False)
old_offers = [old, old1, old2, old3]
merged_offers = LandOffer.merge_offers(old_offers, new_offers)
assert len(merged_offers) == len(old_offers)

new = LandOffer("source", "id_from_source", "link", "title", "location", "price", "area", "date_retrieved", False)
new1 = LandOffer("source1", "id_from_source1", "link1", "title1", "location1", "updated_price1", "area1", "date_retrieved1", False)
new4 = LandOffer("source4", "id_from_source4", "link4", "title4", "location4", "price4", "area4", "date_retrieved4", False)
new_offers = [new, new1, new4]
merged_offers = LandOffer.merge_offers(old_offers, new_offers)
assert new1 in merged_offers
assert new4 in merged_offers
assert old1 not in merged_offers
for offer in merged_offers:
    if offer.source == new1.source and offer.id_as_from_source == new1.id_as_from_source:
        assert offer.was_updated is True
assert len(merged_offers) == len(old_offers) + 1
for o in merged_offers:
    print(o.to_tabbed_string())


