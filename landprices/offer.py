class LandOffer:
    def __init__(self, source, id_as_from_source, link, title, location, price, area, date_listed):
        self.source = source
        self.id_as_from_source = id_as_from_source
        self.link = link
        self.title = title
        self.location = location
        self.area = area
        self.price = price
        self.date_listed = date_listed

    def __key(self):
        return self.source, self.id_as_from_source

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__key() == other.__key()
        else:
            return False

    def __hash__(self):
        return hash(self.__key())
