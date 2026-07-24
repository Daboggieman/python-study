# 21: The `json` Module

**JSON** (JavaScript Object Notation) is the universal data format for web APIs, config files, and data interchange between different programming languages. Python's `json` module converts between JSON text and native Python objects (dicts, lists, strings, numbers).

---

## 1. The Two Directions

| Direction | Function | Memory device |
|---|---|---|
| Python object → JSON string | `json.dumps()` | **d**ump **s**tring |
| JSON string → Python object | `json.loads()` | **l**oad **s**tring |
| Python object → JSON file | `json.dump()` | dump (to a file object) |
| JSON file → Python object | `json.load()` | load (from a file object) |

```python
import json

data = {"name": "Ada", "age": 30, "active": True, "tags": ["dev", "admin"]}

json_string = json.dumps(data)
print(json_string)
print(type(json_string))     # <class 'str'>

parsed = json.loads(json_string)
print(parsed["name"])          # Ada
print(type(parsed))              # <class 'dict'>
```

---

## 2. Working with Files

```python
import json

data = {"name": "Ada", "age": 30}

with open("person.json", "w") as f:
    json.dump(data, f)          # writes directly to the file, no intermediate string needed

with open("person.json", "r") as f:
    loaded = json.load(f)        # reads and parses directly from the file
print(loaded)
```

---

## 3. Formatting Options

```python
data = {"b": 2, "a": 1, "c": [1, 2, 3]}

print(json.dumps(data, indent=2))          # pretty-printed, human-readable
print(json.dumps(data, sort_keys=True))     # alphabetically ordered keys
print(json.dumps(data, indent=2, sort_keys=True))
```

---

## 4. Type Conversion Table

| Python | JSON |
|---|---|
| `dict` | object `{}` |
| `list`, `tuple` | array `[]` |
| `str` | string |
| `int`, `float` | number |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

**Important gotcha:** JSON has no `tuple` type — Python tuples get converted to JSON arrays, and when you load them back, you get a `list`, not a `tuple`. JSON also requires **double quotes** for strings, not single quotes.

---

## 5. Handling Errors: `JSONDecodeError`

```python
import json

bad_json = "{name: 'Ada'}"   # invalid JSON -- missing quotes around key, single quotes for value

try:
    data = json.loads(bad_json)
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
```

Always wrap `json.loads()`/`json.load()` in a `try/except` when the JSON comes from an external, untrusted, or unpredictable source (a network request, a user-uploaded file) — malformed JSON is extremely common in the real world.

---

## 6. Custom Objects: `default` and `object_hook`

`json.dumps()` doesn't know how to serialize arbitrary Python objects (like your own classes) by default — you need to tell it how:

```python
import json
from datetime import date

class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

def person_encoder(obj):
    if isinstance(obj, Person):
        return {"name": obj.name, "birthday": obj.birthday.isoformat()}
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

p = Person("Ada", date(1990, 1, 1))
print(json.dumps(p, default=person_encoder))
```

---

## 📚 Resources

- **W3Schools:** [Python JSON](https://www.w3schools.com/python/python_json.asp)
- **Docs:** [`json` — JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- **YouTube:** [Corey Schafer — Working with JSON Data using the json module](https://www.youtube.com/watch?v=9N6a-VLBa2I)
- **Real Python:** [Working With JSON Data in Python](https://realpython.com/python-json/)

---

## 🧠 Try It Yourself

1. Convert a nested dictionary (with lists and booleans inside) to a JSON string with `indent=2`, then parse it back and confirm the round trip preserves the data.
2. Write a small config file to disk with `json.dump()`, then read it back with `json.load()` in a separate run of your script.
3. Deliberately pass malformed JSON to `json.loads()` and catch the `JSONDecodeError`, printing a friendly error message instead of crashing.
4. Write a `default` encoder function that can serialize a custom `Person` class (with a `name` and a `date` birthday) into JSON.
