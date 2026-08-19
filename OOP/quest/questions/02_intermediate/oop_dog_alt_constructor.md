# OOP Dog Alt Constructor

Source: oop_dog_alt_constructor

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Define a `Dog` class with `__init__(self, name, age)`, a class attribute `population` starting at 0 and incremented on every creation, a classmethod `from_birth_year(cls, name, birth_year, current_year=2026)` that computes age and returns a new `Dog`, and a classmethod `get_population(cls)`.

Expected function
```python
class Dog:
    population = 0

    def __init__(self, name, age):
        pass

    @classmethod
    def from_birth_year(cls, name, birth_year, current_year=2026):
        pass

    @classmethod
    def get_population(cls):
        pass
```


Here is a possible program to test your function :
```python
rex = Dog.from_birth_year("Rex", 2022)
fido = Dog("Fido", 1)
print(rex.age)
print(Dog.get_population())
```

And its output :
```text
4
2
```
