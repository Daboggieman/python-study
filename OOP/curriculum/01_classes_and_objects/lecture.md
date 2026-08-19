# OOP 01: Classes and Objects

**Object-Oriented Programming (OOP)** organizes code around **objects** — bundles of data (attributes) and behavior (methods) — instead of just functions operating on loose data. A **class** is the blueprint; an **object** (or *instance*) is a specific thing built from that blueprint.

---

## 1. The Blueprint Analogy

Think of a class like a cookie cutter, and objects like the cookies it makes. One cutter (class `Dog`), many cookies (objects `my_dog`, `your_dog`, `neighbors_dog`) — each cookie is shaped the same way but is its own separate cookie.

```python
class Dog:
    pass    # an empty blueprint for now

my_dog = Dog()          # an object (instance) of the Dog class
your_dog = Dog()         # a completely separate object

print(my_dog is your_dog)  # False -- two different objects
print(type(my_dog))          # <class '__main__.Dog'>
```

---

## 2. Attributes: The Data an Object Holds

```python
class Dog:
    pass

my_dog = Dog()
my_dog.name = "Rex"       # attach an attribute directly (works, but not the usual way -- see next lesson)
my_dog.age = 3
print(my_dog.name, my_dog.age)
```

This works, but it's fragile — nothing guarantees every `Dog` object actually has a `name` and `age`. The next lesson (`__init__`) fixes this by giving every object its attributes automatically, at creation time.

---

## 3. Methods: The Behavior an Object Has

A method is just a function defined inside a class:

```python
class Dog:
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.bark()   # Woof!
```

We'll unpack that mysterious `self` parameter in Lesson 03 — for now, just know it's required as the first parameter of every regular method.

---

## 4. Classes Group Related Data + Behavior Together

Compare the OOP approach to the "loose functions and dictionaries" approach:

```python
# Without OOP -- data and behavior are disconnected
def bark(dog_dict):
    print(f"{dog_dict['name']} says Woof!")

dog1 = {"name": "Rex"}
bark(dog1)

# With OOP -- data and behavior travel together on the object
class Dog:
    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog()
my_dog.name = "Rex"
my_dog.bark()
```

As programs grow, the OOP version scales better: it's harder to accidentally pass the wrong dictionary shape to `bark()`, and it's obvious where a dog's behavior "lives."

---

## 5. Everything in Python Is Already an Object

This isn't just a paradigm you opt into — Python is built on it:

```python
print(type(5))        # <class 'int'>
print(type("hi"))      # <class 'str'>
print(type([1,2]))      # <class 'list'>
print((5).bit_length())  # ints have methods too!
```

Every value you've ever used in Python — numbers, strings, lists, functions — is an object of some class. Writing your own classes just means adding your own custom types to that same system.

---

## 📚 Resources

- **W3Schools:** [Python Classes/Objects](https://www.w3schools.com/python/python_classes.asp)
- **YouTube:** [Corey Schafer — Python OOP Tutorial 1: Classes and Instances](https://www.youtube.com/watch?v=ZDa-Z5JzLYM) — one of the most-watched, time-tested Python OOP explainers
- **YouTube:** [Programming with Mosh — Python OOP Tutorial](https://www.youtube.com/watch?v=Ej_02ICOIgs)
- **Real Python:** [Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)

---

## 🧠 Try It Yourself

1. Create a `Car` class (empty for now), then create two separate `Car` objects and confirm `car1 is car2` is `False`.
2. Attach `make`, `model`, and `year` attributes directly to a `Car` object, then print a sentence describing the car using those attributes.
3. Add a `honk` method to `Car` that prints `"Beep beep!"`, then call it on an instance.
4. Run `type(3.14)`, `type(True)`, `type(None)`, and `type(print)` — note that even functions and `None` are objects of some class.
