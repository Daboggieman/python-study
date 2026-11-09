# use this to load a json file and return a dictionary
import json

with open("file_name.json", "r") as whatever_u_want_to_call_it:
    loaded_file = json.load(whatever_u_want_to_call_it)

# then u can do whatever u want to do with this file, u can print, or use its data for anyother thing u intended it for
# there is a difference between json.load, and json.loads, the first one is used to load a json file, and the second one is used to load a json string
