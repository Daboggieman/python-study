# OOP 06: Polymorphism

**Polymorphism** ("many forms") means objects of different classes can be used through the **same interface** — the same method name behaves differently depending on which object it's actually called on. This is what lets you write code like `shape.area()` without caring whether `shape` is a `Circle`, `Square`, or `Triangle`.

---

## 1. A Quick Prerequisite: Inheritance

Polymorphism in Python usually shows up alongside **inheritance** — one class (a "subclass") building on another (a "parent"/"base" class), reusing and extending its behavior.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement speak()")

class Dog(Animal):          # Dog inherits from Animal
    def speak(self):          # Dog overrides speak() with its own version
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
```

`Dog` and `Cat` both **inherit** `__init__` from `Animal` (no need to rewrite it), but each **overrides** `speak()` with its own behavior. That's the setup polymorphism relies on.

---

## 2. Polymorphism in Action

```python
animals = [Dog("Rex"), Cat("Whiskers"), Dog("Fido")]

for animal in animals:
    print(animal.speak())    # same method name, different behavior per object
```
```text
Rex says Woof!
Whiskers says Meow!
Fido says Woof!
```

The calling code (`animal.speak()`) never needs an `if isinstance(animal, Dog): ... elif isinstance(animal, Cat): ...` chain — it just trusts that every `Animal` knows how to `speak()`, however it chooses to. This is the entire point: **code that works with the general `Animal` interface automatically works with every specific subclass**, including ones written later.

---

## 3. Duck Typing: Python's Looser Flavor of Polymorphism

Python doesn't actually require a shared parent class for polymorphism to work — if an object has the right method, Python is happy to call it. This is often summarized as **"If it walks like a duck and quacks like a duck, it's a duck."**

```python
class Duck:
    def speak(self):
        return "Quack!"

class Robot:                # totally unrelated class, no shared parent with Duck/Animal
    def speak(self):
        return "BEEP BOOP I AM SPEAKING"

for thing in [Duck(), Robot()]:
    print(thing.speak())     # works fine -- Python never checked what class `thing` "really" is
```

---

## 4. Built-In Polymorphism You Already Use

```python
print(len("hello"))     # 5    -- len() works differently on strings...
print(len([1,2,3]))       # 3    -- ...lists...
print(len({"a":1,"b":2})) # 2    -- ...and dicts, via the same function name

print(1 + 2)              # 3        -- + means numeric addition...
print("a" + "b")          # "ab"     -- ...and here it means concatenation
print([1,2] + [3,4])       # [1,2,3,4] -- ...and here it means combining lists
```

`+` and `len()` are polymorphic: the same operator/function name adapts its behavior to whatever type it's given. Under the hood, this works because each type defines its own version of methods like `__len__` and `__add__` — the exact same override mechanism as `speak()` above.

---

## 5. `super()` — Calling the Parent's Version

Sometimes a subclass wants to *extend* the parent's behavior rather than fully replace it:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"I am {self.name}"

class Dog(Animal):
    def describe(self):
        base = super().describe()          # call Animal's version first
        return base + ", a good dog"

print(Dog("Rex").describe())   # I am Rex, a good dog
```

---

## 📚 Resources

- **W3Schools:** [Python Polymorphism](https://www.w3schools.com/python/python_polymorphism.asp) · [Python Inheritance](https://www.w3schools.com/python/python_inheritance.asp)
- **YouTube:** [Corey Schafer — Python OOP Tutorial 4: Inheritance](https://www.youtube.com/watch?v=RSl87lqOXDE)
- **YouTube:** [Programming with Mosh — Polymorphism in Python](https://www.youtube.com/watch?v=A1eYh1a5aTQ)
- **Real Python:** [Inheritance and Composition: A Python OOP Guide](https://realpython.com/inheritance-composition-python/)

---

## 🧠 Try It Yourself

1. Create an `Animal` base class and `Dog`/`Cat` subclasses as shown, put several of each in one list, and loop through calling `.speak()` on each.
2. Add a `Bird` class that overrides `speak()` differently, and add it to the same list without changing the loop at all — confirm it still works.
3. Write a `Robot` class with no shared parent with `Animal` but with its own `speak()` method, and show it working in the same loop via duck typing.
4. Implement `describe()` on `Animal` and override it on `Dog` using `super().describe()` to extend (not replace) the parent's message.
