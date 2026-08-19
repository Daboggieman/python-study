# Iter Custom Range

Source: iter_custom_range

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Implement a `CustomRange` class that mimics the built-in `range(start, stop, step)` by implementing the iterator protocol (`__iter__` and `__next__`), without using the built-in `range` internally.

Expected function
```python
class CustomRange:
    def __init__(self, start, stop, step=1):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass
```


Here is a possible program to test your function :
```python
print(list(CustomRange(0, 10, 2)))
```

And its output :
```text
[0, 2, 4, 6, 8]
```
