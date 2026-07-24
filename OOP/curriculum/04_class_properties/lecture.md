# OOP 04: Class Properties (Attributes)

"Properties" (more precisely called **attributes** in Python) are the data that lives on a class or its objects. This lesson covers the two flavors — **instance attributes** vs **class attributes** — and introduces the `@property` decorator for controlled access.

---

## 1. Instance Attributes (Per-Object Data)

These are set in `__init__` via `self.x = ...` and belong to **one specific object**. Every object gets its own independent copy.

```python
class Dog:
    def __init__(self, name):
        self.name = name    # instance attribute -- unique per object

rex = Dog("Rex")
fido = Dog("Fido")
rex.name = "Rexy"
print(rex.name, fido.name)   # Rexy Fido -- changing one doesn't affect the other
```

---

## 2. Class Attributes (Shared Across All Objects)

These are defined directly inside the class body (not inside `__init__`) and are **shared** by every instance of the class, unless an instance overrides it.

```python
class Dog:
    species = "Canis familiaris"    # class attribute -- shared by ALL dogs

    def __init__(self, name):
        self.name = name             # instance attribute -- unique per dog

rex = Dog("Rex")
fido = Dog("Fido")
print(rex.species, fido.species)      # Canis familiaris Canis familiaris
print(Dog.species)                     # also accessible on the class itself

Dog.species = "Updated"                # changes it for EVERY dog at once
print(rex.species, fido.species)      # Updated Updated
```

**Danger zone:** if you do `rex.species = "Something else"`, you don't change the shared class attribute — you create a brand-new *instance* attribute on `rex` alone that shadows the class one. This is a very common source of subtle bugs.

```python
rex.species = "Just Rex's species now"
print(rex.species)    # Just Rex's species now
print(fido.species)   # Updated -- unaffected!
```

---

## 3. When to Use Which

| Use a **class attribute** for... | Use an **instance attribute** for... |
|---|---|
| Constants shared by every instance | Data unique to each object |
| A counter tracking how many objects exist | Names, ages, balances — anything object-specific |
| Default configuration values | Anything set through `__init__` parameters |

```python
class Dog:
    population = 0    # class attribute used as a shared counter

    def __init__(self, name):
        self.name = name
        Dog.population += 1    # note: Dog.population, not self.population, to update the SHARED value

Dog("Rex")
Dog("Fido")
print(Dog.population)   # 2
```

---

## 4. Controlled Access with `@property`

Sometimes you want an attribute to *look* like a plain attribute from the outside, but actually run a method behind the scenes (e.g. to validate a value or compute it on the fly).

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius     # convention: leading underscore = "internal, please don't touch directly"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius cannot be negative")
        self._radius = value

    @property
    def area(self):               # a read-only computed property -- no setter defined
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(c.radius)     # 5 -- looks like a plain attribute, but it's a method call
print(c.area)        # 78.53975 -- computed on the fly, always up to date
c.radius = 10          # goes through the setter's validation
print(c.area)          # recalculated automatically: 314.159
c.radius = -3           # raises ValueError
```

---

## 📚 Resources

- **W3Schools:** [Python Classes/Objects](https://www.w3schools.com/python/python_classes.asp)
- **YouTube:** [Corey Schafer — Python OOP Tutorial 2: Class Variables](https://www.youtube.com/watch?v=BJ-VvGyQxho)
- **YouTube:** [Corey Schafer — Python Property Decorator](https://www.youtube.com/watch?v=jCzT9XFZ5bw)
- **Real Python:** [Python Properties](https://realpython.com/python-property/)

---

## 🧠 Try It Yourself

1. Add a class attribute `species` to a `Dog` class, create two dogs, and confirm both share the same value until you override it on one instance.
2. Add a class attribute `population` that increments in `__init__` every time a new `Dog` is created, and print the total after creating three dogs.
3. Implement the `Circle` class above with a validated `radius` property and a read-only `area` property, then confirm setting a negative radius raises `ValueError`.
4. Explain in a comment the difference between `self.species = "X"` and `Dog.species = "X"` inside a method, and what each one actually affects.
