# Venv In Virtualenv Check

Source: venv_in_virtualenv_check

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Write a function that returns True if the current Python process is running inside an activated virtual environment, False otherwise. Hint: compare `sys.prefix` to `sys.base_prefix` -- they differ only when a venv is active.

Expected function
```python
import sys

def in_virtual_env():
    pass
```


Here is a possible program to test your function :
```python
print(isinstance(in_virtual_env(), bool))
```

And its output :
```text
True
```
