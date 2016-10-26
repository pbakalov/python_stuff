from pylab import *

import json

#name_str = '\"name" : "Self_Energy\"'
name_str = '"name" : "Self_Energy"'
name_str = '{'+name_str+'}'
print  name_str
name_json= json.loads(name_str)
print  name_json
name = name_json["name"]
print  name
