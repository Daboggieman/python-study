# OOP Point Class

Source: oop_point_class

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Define an empty `Point` class. Write a function `distance(p1, p2)` that computes the Euclidean distance between two `Point` objects, where each point has `.x` and `.y` attributes attached directly (no `__init__` needed for this exercise).

Expected function
```python
class Point:
    pass

def distance(p1, p2):
    pass
```


Here is a possible program to test your function :
```python
a = Point()
a.x, a.y = 0, 0
b = Point()
b.x, b.y = 3, 4
print(distance(a, b))
```

And its output :
```text
5.0
```
