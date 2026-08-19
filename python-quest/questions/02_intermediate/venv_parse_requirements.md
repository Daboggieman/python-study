# Venv Parse Requirements

Source: venv_parse_requirements

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Write a function that parses the contents of a `requirements.txt`-style string (one `package==version` per line, possibly with blank lines) into a dictionary mapping package name to version string.

Expected function
```python
def parse_requirements(text):
    pass
```


Here is a possible program to test your function :
```python
reqs = "requests==2.31.0\nnumpy==1.26.4\n\nflask==3.0.2\n"
print(parse_requirements(reqs))
```

And its output :
```text
{'requests': '2.31.0', 'numpy': '1.26.4', 'flask': '3.0.2'}
```
