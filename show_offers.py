import json

from landprices.persistence.file_persistence import FilePersistence

p = FilePersistence()
offers = p.load_from_storage()
for o in offers:
    print(
        o.source + "\t" + o.id_as_from_source + "\t" + o.link + "\t" + o.title + "\t" + o.location + "\t" + o.price + "\t" + o.area + "\t" + o.date_listed)

# offers_dict = []
# for o in offers:
#     offers_dict.append(o.__dict__)
# pretty_json_str = json.dumps(offers_dict, sort_keys=True, indent=4)
# print(pretty_json_str)