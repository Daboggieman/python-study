# Write your solution here
import json

def round_trip(data):
    if data == None:
        return "Empty dictionary"
    dict_to_json = json.dumps(data)

    json_to_dict = json.loads(dict_to_json)

    return json_to_dict


data = {"name": "Ada", "tags": ["dev", "admin"], "active": True}
print(round_trip(data))