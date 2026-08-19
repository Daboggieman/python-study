# Modules Sys Path Check

Source: modules_sys_path_check

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Write a function that checks whether a given directory string is present anywhere in `sys.path`.

Expected function
```python
import sys

def is_in_sys_path(directory):
    pass
```


Here is a possible program to test your function :
```python
import sys
sys.path.append("/some/custom/dir")
print(is_in_sys_path("/some/custom/dir"))
print(is_in_sys_path("/not/added"))
```

And its output :
```text
True
False
```
