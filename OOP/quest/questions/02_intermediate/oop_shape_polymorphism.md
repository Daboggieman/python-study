# OOP Shape Polymorphism

Source: oop_shape_polymorphism

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Define a `Shape` base class with a method `area(self)` that raises `NotImplementedError`. Define `Circle(Shape)` and `Square(Shape)` subclasses that each override `area()` correctly. Write a function `total_area(shapes)` that sums the `.area()` of every shape in a list, regardless of which subclass each one is.

Expected function
```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        pass
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        pass
    def area(self):
        pass

def total_area(shapes):
    pass
```


Here is a possible program to test your function :
```python
shapes = [Circle(2), Square(3)]
print(round(total_area(shapes), 2))
```

And its output :
```text
21.57
```
