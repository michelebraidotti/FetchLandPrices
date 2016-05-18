import json
import re

from landprices.persistence.file_persistence import FilePersistence

p = FilePersistence()
offers = p.load_from_storage()
print("source\tid_as_from_source\tlink\ttitle\tlocation\tprice\tarea\tdate_retrieved\twas_updated")
for o in offers:
    print(o.to_tabbed_string())
