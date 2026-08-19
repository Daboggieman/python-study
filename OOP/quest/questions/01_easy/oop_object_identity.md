# OOP Object Identity

Source: oop_object_identity

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Define an empty `Box` class. Write a function `same_object(a, b)` that returns True only if `a` and `b` are literally the SAME object in memory (not just equal-looking) -- use `is`, not `==`.

Expected function
```python
class Box:
    pass

def same_object(a, b):
    pass
```


Here is a possible program to test your function :
```python
box1 = Box()
box2 = Box()
box3 = box1
print(same_object(box1, box2))
print(same_object(box1, box3))
```

And its output :
```text
False
True
```
