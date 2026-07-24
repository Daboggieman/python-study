# OOP Circle Property

Source: oop_circle_property

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Define a `Circle` class with a validated `radius` property (getter + setter; setter must raise `ValueError` for negative values) and a read-only `area` property computed as `3.14159 * radius ** 2`.

Expected function
```python
class Circle:
    def __init__(self, radius):
        pass

    @property
    def radius(self):
        pass

    @radius.setter
    def radius(self, value):
        pass

    @property
    def area(self):
        pass
```


Here is a possible program to test your function :
```python
c = Circle(5)
print(c.radius, round(c.area, 2))
c.radius = 10
print(c.radius, round(c.area, 2))
```

And its output :
```text
5 78.54
10 314.16
```
