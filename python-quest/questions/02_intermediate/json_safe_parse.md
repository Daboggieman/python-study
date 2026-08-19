# Json Safe Parse

Source: json_safe_parse

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Write a function that attempts to parse a JSON string with `json.loads`, catching `json.JSONDecodeError` and returning the string `"INVALID JSON"` instead of crashing if parsing fails.

Expected function
```python
import json

def safe_parse(json_string):
    pass
```


Here is a possible program to test your function :
```python
print(safe_parse('{"valid": true}'))
print(safe_parse("{not valid json}"))
```

And its output :
```text
{'valid': True}
INVALID JSON
```
