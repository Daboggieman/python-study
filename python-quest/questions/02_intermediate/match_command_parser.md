# Match Command Parser

Source: match_command_parser

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Using a `match` statement with list patterns, write a function that interprets simple text-adventure commands given as lists of strings: `["go", direction]` -> `"Moving {direction}"`, `["take", item]` -> `"Taking {item}"`, `["look"]` -> `"Looking around"`, anything else -> `"I don't understand"`.

Expected function
```python
def handle_command(command):
    pass
```


Here is a possible program to test your function :
```python
print(handle_command(["go", "north"]))
print(handle_command(["take", "sword"]))
print(handle_command(["look"]))
print(handle_command(["dance"]))
```

And its output :
```text
Moving north
Taking sword
Looking around
I don't understand
```
