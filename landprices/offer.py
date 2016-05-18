import re


class LandOffer:
    def __init__(self, source, id_as_from_source, link, title, location, price, area, date_retrieved, was_updated):
        self.source = source
        self.id_as_from_source = id_as_from_source
        self.link = link
        self.title = title
        self.location = location
        self.area = area
        self.price = price
        self.date_retrieved = date_retrieved
        self.was_updated = was_updated

    def to_tabbed_string(self):
        price = self.price
        price = re.sub(",\d+", "", price)
        price = re.sub(r"\.", "", price)
        return self.source + "\t" + self.id_as_from_source + "\t" + self.link + "\t" + self.title + "\t" + self.location \
               + "\t" + price + "\t" + self.area + "\t" + self.date_retrieved + "\t" + str(self.was_updated)

    def __key(self):
        return self.source, self.id_as_from_source, self.price

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__key() == other.__key()
        else:
            return False

    def __hash__(self):
        return hash(self.__key())

    @staticmethod
    def merge_offers(old_offers, new_offers):
        output = []
        for old_offer in old_offers:
            found = False
            for new_offer in new_offers:
                if old_offer == new_offer:
                    output.append(old_offer)
                    found = True
                else:
                    if old_offer.source == new_offer.source \
                            and old_offer.id_as_from_source == new_offer.id_as_from_source \
                            and old_offer.price != new_offer.price:
                        new_offer.was_updated = True
                        found = True
                        output.append(new_offer)
            if not found:
                output.append(old_offer)
        for new_offer in new_offers:
            if new_offer not in output:
                output.append(new_offer)
        return output
