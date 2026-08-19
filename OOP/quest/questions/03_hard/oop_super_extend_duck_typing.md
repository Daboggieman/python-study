# OOP Super Extend Duck Typing

Source: oop_super_extend_duck_typing

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Define an `Employee` base class with `__init__(self, name, base_salary)` and a method `pay_summary(self)` returning `f"{self.name}: base ${self.base_salary}"`. Define a `Manager(Employee)` subclass with `__init__(self, name, base_salary, bonus)` that calls the parent's `__init__` via `super()`, and overrides `pay_summary` to call the parent's version via `super()` and then append `f" + bonus ${self.bonus}"`. Separately, define an unrelated `Contractor` class (no shared parent) that also has its own `pay_summary(self)` method, to demonstrate duck typing works alongside inheritance-based polymorphism.

Expected function
```python
class Employee:
    def __init__(self, name, base_salary):
        pass
    def pay_summary(self):
        pass

class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        pass
    def pay_summary(self):
        pass

class Contractor:
    def __init__(self, name, hourly_rate):
        pass
    def pay_summary(self):
        pass
```


Here is a possible program to test your function :
```python
people = [Employee("Sam", 50000), Manager("Ada", 70000, 5000), Contractor("Lee", 80)]
for p in people:
    print(p.pay_summary())
```

And its output :
```text
Sam: base $50000
Ada: base $70000 + bonus $5000
Lee: contractor at $80/hr
```
