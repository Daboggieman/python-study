# Exercise 21: The json Module
# Run this script with: python exercises.py

import json


# TODO: Exercise 1
def round_trip(data):
    """Convert data to a JSON string (pretty-printed) and back, returning the result."""
    pass


# TODO: Exercise 3
def safe_parse(json_string):
    """Parse json_string; return the parsed value, or the string 'INVALID JSON' if parsing fails."""
    pass


if __name__ == "__main__":
    data = {"name": "Ada", "tags": ["dev", "admin"], "active": True}
    print(round_trip(data))

    print(safe_parse('{"valid": true}'))
    print(safe_parse("{not valid json}"))
