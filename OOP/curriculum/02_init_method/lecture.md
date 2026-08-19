# OOP 02: The `__init__` Method

`__init__` is a special method (Python calls these **"dunder" methods**, short for "double underscore") that runs **automatically** every time you create a new object from a class. It's where you set up an object's starting attributes, so you never end up with an object missing data it needs.

---

## 1. Why We Need It

Lesson 01 attached attributes manually, after creating the object:

```python
my_dog = Dog()
my_dog.name = "Rex"   # easy to forget this line!
```

`__init__` guarantees every object gets its required attributes the moment it's created — no separate step to remember.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Rex", 3)     # __init__ runs automatically here
print(my_dog.name, my_dog.age)   # Rex 3
```

---

## 2. What's Actually Happening

When you write `Dog("Rex", 3)`, Python:
1. Creates a new, empty `Dog` object.
2. Calls `__init__(the_new_object, "Rex", 3)` automatically — with `self` bound to that new object.
3. Hands you back the fully-initialized object.

```python
my_dog = Dog("Rex", 3)
# is roughly equivalent to:
#   my_dog = <a new blank Dog object>
#   Dog.__init__(my_dog, "Rex", 3)
```

You never call `__init__` yourself directly — Python calls it for you as part of `ClassName(...)`.

---

## 3. Default Parameter Values

`__init__` is a regular function under the hood, so it supports default arguments just like any function:

```python
class Dog:
    def __init__(self, name, age=0, breed="Unknown"):
        self.name = name
        self.age = age
        self.breed = breed

d1 = Dog("Rex")                       # age=0, breed="Unknown"
d2 = Dog("Fido", 2, "Labrador")        # all three provided
d3 = Dog("Buddy", breed="Poodle")      # keyword argument, skips age
```

---

## 4. `__init__` Is Not a Constructor (Technically)

In some languages the setup method also *creates* the object. In Python, object creation is actually handled by a different, rarer-to-touch method called `__new__`; `__init__` only *initializes* an object that already exists. For everyday Python, you'll almost never need `__new__` — just know the name `__init__` reflects this precisely (**init**ialize, not construct).

---

## 5. Common Pitfall: Forgetting `self`

```python
class Dog:
    def __init__(name, age):    # BUG: missing `self`!
        name = name
        age = age
```

This looks like it should work but breaks in confusing ways because Python passes the new object as the first argument no matter what you name it — if you forget to catch it as `self`, your actual `name` argument silently receives the object instead of the string you passed in. Always include `self` first.

---

## 📚 Resources

- **W3Schools:** [Python Classes/Objects — `__init__`](https://www.w3schools.com/python/python_classes.asp)
- **YouTube:** [Corey Schafer — Python OOP Tutorial 1: Classes and Instances](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)
- **YouTube:** [Tech With Tim — Python OOP Explained](https://www.youtube.com/watch?v=JeznW_7DlB0)
- **Docs:** [Python Data Model — `__init__`](https://docs.python.org/3/reference/datamodel.html#object.__init__)

---

## 🧠 Try It Yourself

1. Rewrite the `Car` class from Lesson 01 to use `__init__` with `make`, `model`, and `year` parameters, then create two different cars in one line each.
2. Add a default value for `year` (e.g. `2024`) and create a car without specifying a year to confirm the default kicks in.
3. Deliberately remove `self` from `__init__` and run the code — read the error message carefully and explain in a comment what went wrong.
4. Add a fourth parameter `mileage=0` and a method `drive(self, miles)` that adds to `self.mileage` — call it a few times and print the running total.
