import json
import os

from landprices.offer import LandOffer
from os.path import expanduser
from os.path import exists

class FilePersistence:
    file_path = expanduser("~") + '/.fetch_land_and_prices_history.json'

    @staticmethod
    def as_offer(dct):
        return LandOffer(dct['source'], dct['id_as_from_source'], dct['link'], dct['title'], dct['location'],
                         dct['price'], dct['area'], dct['date_listed'])

    def load_from_storage(self):
        offers = []
        if not exists(self.file_path):
            open(self.file_path, 'w').close()
        else:
            if os.stat(self.file_path).st_size > 0:
                with open(self.file_path, 'r') as f:
                    offers = json.load(f, object_hook=self.as_offer)
        return offers

    def save_to_storage(self, offers):
        offers_dict = []
        for o in offers:
            offers_dict.append(o.__dict__)
        with open(self.file_path, 'w') as f:
            json.dump(offers_dict, f)
