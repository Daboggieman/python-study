# Match Http Status

Source: match_http_status

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Using a `match` statement (not if/elif), write a function that returns a short description for common HTTP status codes: 200 -> "OK", 201 -> "Created", 404 -> "Not Found", 500 -> "Server Error", anything else -> "Unknown".

Expected function
```python
def describe_status(code):
    pass
```


Here is a possible program to test your function :
```python
print(describe_status(200))
print(describe_status(404))
print(describe_status(999))
```

And its output :
```text
OK
Not Found
Unknown
```
