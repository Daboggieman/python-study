# OOP Singleton Pattern

Source: oop_singleton_pattern

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Implement the Singleton pattern using a classmethod: define a `Config` class where calling `Config.get_instance()` always returns the SAME object, creating it only the first time it's called (store it on a class attribute). Direct instantiation with `Config()` should still work normally and create a separate object -- only `get_instance()` guarantees a shared single instance.

Expected function
```python
class Config:
    _instance = None

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls):
        pass
```


Here is a possible program to test your function :
```python
a = Config.get_instance()
b = Config.get_instance()
print(a is b)

c = Config()
print(a is c)
```

And its output :
```text
True
False
```
