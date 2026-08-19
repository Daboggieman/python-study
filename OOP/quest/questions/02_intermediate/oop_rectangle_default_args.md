# OOP Rectangle Default Args

Source: oop_rectangle_default_args

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Define a `Rectangle` class with `__init__(self, width, height=None)`. If `height` is not given, treat the rectangle as a square (`height = width`). Add a method `area(self)` returning `width * height`.

Expected function
```python
class Rectangle:
    def __init__(self, width, height=None):
        pass

    def area(self):
        pass
```


Here is a possible program to test your function :
```python
square = Rectangle(4)
rect = Rectangle(4, 6)
print(square.area())
print(rect.area())
```

And its output :
```text
16
24
```
