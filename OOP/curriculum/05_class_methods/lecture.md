# OOP 05: Class Methods and Static Methods — A Manual Walkthrough

**Prerequisite:** Lessons 01–04 (especially class attributes, Lesson 04 Part 2).
**By the end you will be able to:** write alternative constructors with `@classmethod`, group helper functions with `@staticmethod`, explain why `cls(...)` beats hardcoding the class name, and predict which of the three method types a given call needs.

---

## Part 0 — Two Things Instance Methods Can't Do

Every method so far took `self`, because every method so far needed one specific object's data. Two ordinary requirements break that pattern.

### 0.1 "Build me a Dog, but from a birth year"

`__init__` takes an age. But your data source gives you birth years. You could make callers do the arithmetic:

```python
rex = Dog("Rex", 2026 - 2022)      # every caller repeats this
```

That's the conversion logic scattered across every call site. You want a **second way to build a Dog** that lives on the class:

```python
rex = Dog.from_birth_year("Rex", 2022)
```

Note what's being called: `Dog.from_birth_year(...)`. There is **no dog yet** — the whole point is to make one. So there's no object to be `self`. An instance method is structurally the wrong tool.

### 0.2 "Is this a plausible age?"

```python
def is_valid_age(age):
    return 0 <= age <= 30
```

This clearly belongs *with* `Dog` — it encodes a fact about dogs. But it needs no dog and no class data; it just checks a number. Putting it at module level works but scatters dog-related logic outside the class.

> **The core insight:** a method's first parameter tells you what it needs. `self` = one object. `cls` = the class. Neither = nothing at all. Python gives you all three.

---

## Part 1 — Instance Methods (Recap)

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):              # needs ONE dog
        print(f"{self.name} says Woof!")
```

Instance methods need an object, and Python enforces it. Call one on the class and the missing object is reported plainly:

```python
Dog.bark()
```
```text
TypeError: Dog.bark() missing 1 required positional argument: 'self'
```

Unlike the confusing errors in Lesson 01, this one names `self` outright, because you called through the class and no binding happened.

---

## Part 2 — `@classmethod`: Methods That Receive the Class

### 2.1 `cls` instead of `self`

```python
class Dog:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.population += 1

    @classmethod
    def get_population(cls):
        return cls.population
```

Two changes from an instance method: the `@classmethod` decorator, and the first parameter is named `cls` instead of `self`.

| Parameter | Receives | Convention |
|---|---|---|
| `self` | the **object** it was called on | instance methods |
| `cls` | the **class** itself | class methods |

`cls` is a convention exactly like `self` (Lesson 03 Part 4) — the decorator is what actually changes the behaviour. And `cls` really is the class, so `cls.population` is the same thing as `Dog.population`.

### 2.2 The killer use case: alternative constructors

This solves Part 0.1:

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
        return cls(name, age)           # cls(...) builds a Dog
```

```python
rex = Dog.from_birth_year("Rex", 2022)
print(rex.age)                  # 4
print(Dog.get_population())     # 1
```

Trace it: `cls` is `Dog`, so `cls(name, age)` is `Dog("Rex", 4)` — which runs `__init__` normally and returns a finished dog. The method **returns** the new object, unlike `__init__` which must return `None` (Lesson 02 Part 2).

You now have two doors into the same class:

| Call | Takes | Use when |
|---|---|---|
| `Dog("Rex", 4)` | an age | you already have an age |
| `Dog.from_birth_year("Rex", 2022)` | a birth year | your data has birth years |

Both end up running `__init__`, so there's exactly one place where a `Dog`'s attributes are actually set. The alternative constructor only converts its inputs and delegates.

> **A note on that `current_year=2026` default:** it's a hardcoded value that will be wrong next year — a *rotting default*. It's fine for this exercise, but real code would use `datetime.date.today().year` computed **inside** the body (not as the default, which would freeze at import time — the same evaluate-once trap as Lesson 02 Part 4.2).

### 2.3 Why `cls(...)` and not `Dog(...)`?

Inside `from_birth_year`, `cls` is `Dog`. So why not just write `Dog(name, age)`? Because `cls` is *whatever class the call came through* — and that matters the moment anyone subclasses you.

**With `cls(name, age)`:**

```python
class Puppy(Dog):
    pass

p = Puppy.from_birth_year("Bit", 2025)
print(type(p).__name__)      # Puppy   ✔ correct
```

**With `Dog(name, age)` hardcoded:**

```python
    @classmethod
    def from_birth_year(cls, name, birth_year, current_year=2026):
        return Dog(name, current_year - birth_year)      # hardcoded

p = Puppy.from_birth_year("Bit", 2025)
print(type(p).__name__)      # Dog   ✘ wrong -- asked for a Puppy, got a Dog
```

You called it on `Puppy` and got a `Dog`. Every `Puppy`-specific method is missing from the result, and nothing errored — it just silently handed back the wrong type.

`cls` makes the method **inherit correctly**: `Dog.from_birth_year` builds Dogs, `Puppy.from_birth_year` builds Puppies, from one definition. Hardcoding the name throws that away.

### 2.4 Class-wide operations

The other use for `@classmethod` is anything that reads or writes shared class state:

```python
    @classmethod
    def get_population(cls):
        return cls.population

    @classmethod
    def reset_population(cls):
        cls.population = 0
```

These need the class, not an object — asking one dog "how many dogs exist?" is the wrong question to the wrong entity.

---

## Part 3 — `@staticmethod`: Methods That Receive Nothing

### 3.1 The mechanics

This solves Part 0.2:

```python
class Dog:
    @staticmethod
    def is_valid_age(age):
        return 0 <= age <= 30

print(Dog.is_valid_age(5))     # True
print(Dog.is_valid_age(-2))    # False
```

No `self`, no `cls`, no decorator parameter at all. `@staticmethod` tells Python: *"don't insert anything — pass the arguments through untouched."*

### 3.2 What the decorator is actually doing for you

Watch it break without the decorator. This looks like it should be the same thing:

```python
class Dog:
    def is_valid_age(age):        # no decorator
        return 0 <= age <= 30

print(Dog.is_valid_age(5))       # True    -- works!
```

It works — via the class. Now via an object:

```python
d = Dog()
print(d.is_valid_age(5))
```
```text
TypeError: Dog.is_valid_age() takes 1 positional argument but 2 were given
```

Exactly the Lesson 01 Part 3.4 failure. The dot bound `d` in as the first argument, so `age` received the *dog* and `5` had nowhere to go. The method works from the class and breaks from an instance — a landmine that fires depending on how it's called.

`@staticmethod` fixes precisely that: it switches off the binding, so the method behaves identically either way.

### 3.3 Static method or plain module function?

Honest answer: a `@staticmethod` is a plain function that happens to live in the class namespace. The difference is organisational, not technical.

| Prefer `@staticmethod` | Prefer a module-level function |
|---|---|
| Logic is meaningless without the class's context | Genuinely reusable elsewhere |
| You want `Dog.is_valid_age(...)` to read as a fact about dogs | Nothing to do with any one class |
| Subclasses might want to override it | No inheritance story |

Where it pays off is using it *inside* the class to keep `__init__` clean:

```python
class Dog:
    def __init__(self, name, age):
        if not Dog.is_valid_age(age):
            raise ValueError(f"invalid age: {age}")
        self.name = name
        self.age = age

    @staticmethod
    def is_valid_age(age):
        return 0 <= age <= 30
```

```python
Dog("Bad", -5)      # ValueError: invalid age: -5
```

The validation rule is stated once, named clearly, and reusable by callers *before* they attempt to build a dog.

---

## Part 4 — All Three, Side by Side

```python
class Example:
    def instance_method(self):
        return f"instance method — got the object: {self}"

    @classmethod
    def class_method(cls):
        return f"class method — got the class: {cls}"

    @staticmethod
    def static_method():
        return "static method — got nothing"
```

| Type | Decorator | 1st param | Sees instance data | Sees class data | Typical use |
|---|---|---|---|---|---|
| Instance | *(none)* | `self` | ✔ | ✔ (via `type(self)`) | normal object behaviour |
| Class | `@classmethod` | `cls` | ✘ | ✔ | alternative constructors, shared state |
| Static | `@staticmethod` | *(none)* | ✘ | ✘ | helpers grouped with the class |

**One thing that surprises people:** class methods and static methods can be called on an *instance* too, and it works fine:

```python
rex = Dog("Rex", 3)
print(rex.get_population())    # works -- Python finds the class from the object
print(rex.is_valid_age(5))     # works
```

Only the reverse is forbidden — an instance method genuinely needs an object, so `Dog.bark()` fails (Part 1). Calling class/static methods on the class is still clearer about intent, and is what you should write.

**How to choose,** in one question: *what does this method need in order to work?*

- One specific object's data → instance method.
- The class (to build one, or to touch shared state) → `@classmethod`.
- Only its own arguments → `@staticmethod`.

---

## Part 5 — Predict, Then Run

1. ```python
   class Counter:
       total = 0
       @classmethod
       def bump(cls): cls.total += 1
   Counter.bump(); Counter.bump()
   print(Counter.total)
   ```

2. ```python
   class A:
       @classmethod
       def make(cls): return cls()
   class B(A): pass
   print(type(B.make()).__name__)
   ```

3. ```python
   class Tool:
       @staticmethod
       def double(x): return x * 2
   t = Tool()
   print(Tool.double(4), t.double(4))
   ```

4. ```python
   class Dog:
       def speak(self): return "woof"
   print(Dog.speak())
   ```

<details>
<summary>Answers (predict first)</summary>

1. `2`. `cls.total += 1` writes to the class, because `cls` **is** the class — this is the correct counter idiom, and it's why `@classmethod` avoids the `self.count += 1` trap from Lesson 04 Part 2.4.
2. `B`. `cls` is `B` when called as `B.make()`, so `cls()` builds a `B` (Part 2.3).
3. `8 8`. `@staticmethod` switches off binding, so both call routes behave identically (Part 3.2, Part 4).
4. `TypeError: Dog.speak() missing 1 required positional argument: 'self'` — an instance method needs an object (Part 1).

</details>

---

## Part 6 — Cheat Sheet Summary

```python
class Dog:
    population = 0

    def __init__(self, name, age):
        if not Dog.is_valid_age(age):
            raise ValueError(f"invalid age: {age}")
        self.name = name
        self.age = age
        Dog.population += 1

    def bark(self):                     # INSTANCE: needs one dog
        print(f"{self.name} says Woof!")

    @classmethod                        # CLASS: needs the class
    def from_birth_year(cls, name, birth_year, current_year=2026):
        return cls(name, current_year - birth_year)      # cls(), never Dog()

    @classmethod
    def get_population(cls):
        return cls.population

    @staticmethod                       # STATIC: needs nothing
    def is_valid_age(age):
        return 0 <= age <= 30
```

| Idea | One-line version |
|---|---|
| `self` vs `cls` | the object vs the class; both are conventions, decorators do the work |
| `@classmethod` | first param is the class; use for alternative constructors and shared state |
| Alternative constructor | converts its inputs, then `return cls(...)` — delegates to `__init__` |
| Why `cls(...)` | so subclasses build *themselves*; hardcoding `Dog(...)` silently returns the wrong type |
| `@staticmethod` | no `self`, no `cls` — switches off argument binding |
| Helper with no decorator | works via the class, `TypeError` via an instance — fix with `@staticmethod` |
| Class/static via an instance | allowed and works; instance method via the class does **not** |
| Choosing | needs an object → instance; needs the class → class; needs neither → static |
| Rotting defaults | `current_year=2026` freezes; compute "now" inside the body instead |

---

## Self-Check

- [ ] Why can't `from_birth_year` be an instance method?
- [ ] What does `cls` receive, and what does the decorator (not the name) actually do?
- [ ] Show what goes wrong if an alternative constructor hardcodes `Dog(...)` instead of `cls(...)`.
- [ ] A helper without `@staticmethod` works as `Dog.f(5)` but fails as `d.f(5)`. Why?
- [ ] Can you call a `@classmethod` on an instance? Can you call an instance method on the class?
- [ ] Which of the three needs nothing but its own arguments?

---

## 📚 Resources

- **W3Schools:** [Python Classes/Objects](https://www.w3schools.com/python/python_classes.asp)
- **YouTube:** [Corey Schafer — classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)
- **Real Python:** [Python's Instance, Class, and Static Methods Demystified](https://realpython.com/instance-class-and-static-methods-demystified/)
- **Docs:** [`classmethod`](https://docs.python.org/3/library/functions.html#classmethod) · [`staticmethod`](https://docs.python.org/3/library/functions.html#staticmethod)

---

## 🧠 Try It Yourself

Open `exercises.py` in this folder. **Do Exercise 3 first** — `__init__` calls `is_valid_age`, so until that returns a real boolean every `Dog(...)` will raise:

1. Implement `is_valid_age(age)` as a `@staticmethod` returning `True` for `0 <= age <= 30` (Part 3.1).
2. Implement `from_birth_year` as a `@classmethod` that computes the age and returns `cls(name, age)` (Part 2.2).
3. Implement `get_population` as a `@classmethod` returning `cls.population` (Part 2.4).
4. Confirm `Dog("Bad", -5)` raises `ValueError` (Part 3.3).
5. Add `class Puppy(Dog): pass` at the bottom, call `Puppy.from_birth_year("Bit", 2025)`, and print `type(...).__name__`. Then temporarily change `cls(...)` to `Dog(...)` and watch it return the wrong type (Part 2.3).
6. Call `get_population()` and `is_valid_age(5)` on an *instance* rather than the class, and confirm both still work (Part 4).
