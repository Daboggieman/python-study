# Json Round Trip

Source: json_round_trip

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Write a function that converts a Python dictionary to a JSON string (using `json.dumps`) and back to a Python object (using `json.loads`), and returns the final round-tripped object.

Expected function
```python
import json

def round_trip(data):
    pass
```


Here is a possible program to test your function :
```python
data = {"name": "Ada", "tags": ["dev", "admin"], "active": True}
print(round_trip(data))
```

And its output :
```text
{'name': 'Ada', 'tags': ['dev', 'admin'], 'active': True}
```
