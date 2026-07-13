# Is Sorted

Source: is_sorted

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Write a function that returns true if the list is sorted according to a custom comparison function, otherwise, returns false.

Expected function
```python
def is_sorted(compare, values):
    pass
```


Here is a possible program to test your function :
```python
print(is_sorted(lambda a, b: (a > b) - (a < b), [1, 2, 3]))
```

And its output :
```text
True
```
