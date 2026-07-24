# OOP 05: Class Methods (and Static Methods)

Python has three kinds of methods you can define inside a class, each with a different relationship to `self` and the class: **instance methods** (what you've used so far), **class methods**, and **static methods**.

---

## 1. Instance Methods (the default, review)

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):          # instance method -- takes `self`, operates on ONE object
        print(f"{self.name} says Woof!")
```

---

## 2. Class Methods — Operate on the Class Itself

A **class method** takes `cls` (the class itself) instead of `self` (a specific object), and is marked with `@classmethod`. It's used when a method needs to work with the class as a whole, rather than one instance — the most common use case is an **alternative constructor**.

```python
class Dog:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.population += 1

    @classmethod
    def from_birth_year(cls, name, birth_year, current_year=2026):
        age = current_year - birth_year
        return cls(name, age)          # cls(...) == Dog(...) here, but works correctly even in subclasses

    @classmethod
    def get_population(cls):
        return cls.population

rex = Dog.from_birth_year("Rex", 2022)    # an alternative way to build a Dog
print(rex.age)                              # 4
print(Dog.get_population())                  # 1
```

**Why `cls(...)` instead of `Dog(...)` directly?** If someone later creates a subclass `Puppy(Dog)`, calling `Puppy.from_birth_year(...)` will correctly create a `Puppy` (because `cls` is `Puppy` in that context), whereas hardcoding `Dog(...)` would always create a `Dog` even when called via `Puppy`.

---

## 3. Static Methods — Don't Need `self` OR `cls`

A **static method**, marked with `@staticmethod`, is a function that logically belongs inside the class (because it's related to what the class does) but doesn't need access to any instance or class data at all.

```python
class Dog:
    @staticmethod
    def is_valid_age(age):
        return 0 <= age <= 30

print(Dog.is_valid_age(5))     # True -- called on the class, no instance needed
print(Dog.is_valid_age(-2))    # False
```

Think of static methods as "just a regular function that happens to live inside the class namespace for organizational purposes."

---

## 4. Side-by-Side Comparison

```python
class Example:
    def instance_method(self):
        return f"instance method, called on {self}"

    @classmethod
    def class_method(cls):
        return f"class method, called on {cls}"

    @staticmethod
    def static_method():
        return "static method, doesn't know or care what class it's on"
```

| Type | First parameter | Access to instance data? | Access to class data? | Common use |
|---|---|---|---|---|
| Instance method | `self` | Yes | Yes (via `type(self)` or `self.__class__`) | Normal object behavior |
| Class method | `cls` | No | Yes | Alternative constructors, class-wide operations |
| Static method | (none) | No | No | Utility/helper functions grouped with the class |

---

## 📚 Resources

- **W3Schools:** [Python Classes/Objects](https://www.w3schools.com/python/python_classes.asp)
- **YouTube:** [Corey Schafer — Python OOP Tutorial 3: classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)
- **Real Python:** [Python's Instance, Class, and Static Methods Demystified](https://realpython.com/instance-class-and-static-methods-demystified/)

---

## 🧠 Try It Yourself

1. Add a `from_birth_year` classmethod to a `Dog` class as shown, and create a dog using it instead of the normal constructor.
2. Add a `get_population` classmethod that returns how many dogs have been created so far.
3. Add a static method `is_valid_age(age)` that returns `True` for ages between 0 and 30, and use it to validate age before creating a `Dog` in `__init__` (raise `ValueError` if invalid).
4. Explain in a comment, using your own words, why an alternative-constructor classmethod should use `cls(...)` rather than hardcoding the class name.
