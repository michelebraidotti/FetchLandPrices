import json
import re

from landprices.persistence.file_persistence import FilePersistence

p = FilePersistence()
offers = p.load_from_storage()
print("source\tid_as_from_source\tlink\ttitle\tlocation\tprice\tarea\tdate_retrieved\twas_updated")
for o in offers:
    price = o.price
    price = re.sub(",\d+", "", price)
    price = re.sub(r"\.", "", price)
    print(
        o.source + "\t" + o.id_as_from_source + "\t" + o.link + "\t" + o.title + "\t" + o.location
        + "\t" + price + "\t" + o.area + "\t" + o.date_retrieved + "\t" + str(o.was_updated))

# offers_dict = []
# for o in offers:
#     offers_dict.append(o.__dict__)
# pretty_json_str = json.dumps(offers_dict, sort_keys=True, indent=4)
# print(pretty_json_str)>