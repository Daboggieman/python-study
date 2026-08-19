# 🧱 OOP Cheatsheet

A comprehensive quick-reference for Object-Oriented Programming in Python. Pairs with `OOP/curriculum/` (theory) and `OOP/quest/` (practice problems).

---

## 1. Classes and Objects

```python
class Dog:
    pass

my_dog = Dog()             # an instance (object) of class Dog
print(type(my_dog))          # <class '__main__.Dog'>
print(isinstance(my_dog, Dog))  # True
```
A **class** is a blueprint. An **object**/**instance** is a specific thing built from it. Every value in Python (int, str, list, even functions) is an object of some class.

## 2. The `__init__` Method

```python
class Dog:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

rex = Dog("Rex", 3)    # __init__ runs automatically at creation
```
- Runs automatically when you call `ClassName(...)`.
- Supports default arguments like any function.
- Always include `self` as the first parameter, or things silently break.

## 3. The `self` Parameter

```python
class Dog:
    def bark(self):
        print(f"{self.name} says Woof!")

rex.bark()          # shorthand for...
Dog.bark(rex)         # ...this: `rex` is passed automatically as `self`
```
`self` = "the specific object this method was called on." It's a naming convention, not a keyword — but never deviate from it.

## 4. Class Properties (Attributes)

```python
class Dog:
    species = "Canis familiaris"   # CLASS attribute -- shared by all instances

    def __init__(self, name):
        self.name = name             # INSTANCE attribute -- unique per object
```

| | Class attribute | Instance attribute |
|---|---|---|
| Defined | In the class body | Inside `__init__` via `self.x = ...` |
| Shared? | Yes, by all instances | No, unique per object |
| Update for everyone | `ClassName.attr = x` | n/a |
| Pitfall | `instance.attr = x` creates a NEW instance attribute, shadowing the class one | — |

**`@property` — controlled attribute access:**
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius cannot be negative")
        self._radius = value

    @property
    def area(self):              # read-only, no setter
        return 3.14159 * self._radius ** 2
```

## 5. Class Methods and Static Methods

```python
class Dog:
    population = 0

    def __init__(self, name, age):
        self.name, self.age = name, age
        Dog.population += 1

    @classmethod
    def from_birth_year(cls, name, birth_year, current_year=2026):
        return cls(name, current_year - birth_year)   # alternative constructor

    @staticmethod
    def is_valid_age(age):
        return 0 <= age <= 30                            # no self/cls needed
```

| Type | First param | Sees instance data | Sees class data | Typical use |
|---|---|---|---|---|
| Instance method | `self` | Yes | Yes | Normal behavior |
| `@classmethod` | `cls` | No | Yes | Alternative constructors, class-wide counters |
| `@staticmethod` | (none) | No | No | Grouped utility functions |

## 6. Polymorphism (and Inheritance)

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

for a in [Dog("Rex"), Cat("Whiskers")]:
    print(a.speak())    # same call, different behavior per object
```

**`super()`** — call the parent's version of a method (extend, don't replace):
```python
class Dog(Animal):
    def describe(self):
        return super().describe() + ", a good dog"
```

**Duck typing** — no shared parent class required:
```python
class Robot:
    def speak(self):
        return "BEEP BOOP"

for thing in [Dog("Rex"), Robot()]:
    print(thing.speak())   # works fine, Python only cares that speak() exists
```

---

## Dunder (Magic) Methods Quick Reference

| Method | Triggered by | Example use |
|---|---|---|
| `__init__(self, ...)` | `ClassName(...)` | Set up instance attributes |
| `__str__(self)` | `str(obj)`, `print(obj)` | Human-readable string |
| `__repr__(self)` | `repr(obj)`, console echo | Unambiguous developer-facing string |
| `__len__(self)` | `len(obj)` | Custom length |
| `__eq__(self, other)` | `obj1 == obj2` | Custom equality |
| `__add__(self, other)` | `obj1 + obj2` | Custom `+` behavior |
| `__lt__(self, other)` | `obj1 < obj2` | Custom ordering |
| `__getitem__(self, key)` | `obj[key]` | Custom indexing |
| `__iter__(self)` | `for x in obj:` | Make an object iterable |

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1, p2 = Point(1, 2), Point(1, 2)
print(p1)              # Point(1, 2)  -- uses __str__
print(p1 == p2)        # True         -- uses __eq__
```

---

## Encapsulation Quick Reference (naming conventions)

| Prefix | Convention meaning |
|---|---|
| `name` | Public — freely accessible |
| `_name` | "Internal use" — please don't touch directly, but not enforced |
| `__name` | Name-mangled to `_ClassName__name` — a stronger (but not absolute) privacy hint |

Python doesn't have true `private` attributes like some languages — these are conventions the whole community respects, not hard restrictions.

---

## 📚 More Resources

See `OOP/resources/links.md` for the full curated list of W3Schools pages, YouTube videos, and articles referenced throughout every `OOP/curriculum/` lesson.
