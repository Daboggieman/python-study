# Modules Dynamic Import

Source: modules_dynamic_import

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Using the `importlib` module, write a function that dynamically imports a standard library module by name (given as a string) and returns the value of a named attribute from it. Return `None` if the module or attribute doesn't exist.

Expected function
```python
import importlib

def get_module_attribute(module_name, attribute_name):
    pass
```


Here is a possible program to test your function :
```python
print(get_module_attribute("math", "pi"))
print(get_module_attribute("math", "does_not_exist"))
print(get_module_attribute("not_a_real_module", "pi"))
```

And its output :
```text
3.141592653589793
None
None
```
