# OOP 02: The `__init__` Method — A Manual Walkthrough

**Prerequisite:** Lesson 01 (classes, objects, attributes, `self`).
**By the end you will be able to:** guarantee every object is born complete, use default parameter values safely, and explain exactly what `ClassName(...)` does step by step.

---

## Part 0 — The Problem Left Over From Lesson 01

Lesson 01 ended on an unsolved gap (Part 2.4 of that lecture). Here it is again:

```python
class Dog:
    pass

rex = Dog()
rex.name = "Rex"
# ...and we forgot rex.age
```

Nothing stops this. The `Dog` exists, it's just **half-built**, and you won't find out until something reaches for the missing piece:

```text
AttributeError: 'Dog' object has no attribute 'age'
```

Worse, that crash can happen thousands of lines away from the line that actually made the mistake. The bug is *created* at object-creation time but *reported* at use time.

Also notice the busywork — three lines to make one dog, every single time:

```python
rex = Dog()
rex.name = "Rex"
rex.age = 3
```

> **The core insight:** object creation and attribute setup should be **one single step** that cannot be half-done. If setting up the data is part of building the object, there is no window in which an incomplete object can exist.

`__init__` is how Python does exactly that.

---

## Part 1 — `__init__` Runs Automatically

### 1.1 The mechanics

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

rex = Dog("Rex", 3)          # one line, fully built
print(rex.name, rex.age)     # Rex 3
```

Three things changed from Lesson 01:

1. `Dog()` became `Dog("Rex", 3)` — the values now go in at creation.
2. A method named `__init__` receives them.
3. `__init__` copies them onto the object with `self.`.

The name has a specific shape: two underscores, `init`, two underscores. Python calls these **dunder** methods (short for **d**ouble **under**score). Dunder methods are how you hook into Python's built-in machinery — `__init__` is the hook for "a new object was just made."

### 1.2 The line that confuses everyone

```python
self.name = name
```

Left and right are **not** the same thing, despite looking almost identical:

| Side | What it is | Lives where |
|---|---|---|
| `self.name` | an **attribute** on the object | survives after `__init__` ends |
| `name` | the **parameter** that was passed in | a local variable, discarded when `__init__` ends |

So the line means: *"take the value that arrived in the parameter `name`, and store it permanently on this object under the attribute `name`."* You are copying from a temporary local into permanent storage.

They don't have to share a name — this is identical in behaviour, just uglier:

```python
def __init__(self, n, a):
    self.name = n         # attribute `name` from parameter `n`
    self.age = a
```

Same-naming is the universal convention, but understanding that they're two different things is what stops `self.` from feeling arbitrary.

### 1.3 State trace

For `rex = Dog("Rex", 3)`:

| Step | What happens | `rex` holds |
|---|---|---|
| 1 | A blank `Dog` object is created | *(nothing)* |
| 2 | `__init__` is called with `self`=that object, `name`="Rex", `age`=3 | *(nothing yet)* |
| 3 | `self.name = name` runs | `name → "Rex"` |
| 4 | `self.age = age` runs | `name → "Rex"`, `age → 3` |
| 5 | `__init__` returns; the object is handed to you | `name → "Rex"`, `age → 3` |

At no point does a caller ever see a half-built dog. That's the whole win.

---

## Part 2 — What `Dog("Rex", 3)` Actually Does

Written out in full, `Dog("Rex", 3)` is three steps:

1. **Create** a new blank `Dog` object.
2. **Call** `Dog.__init__(that_object, "Rex", 3)` — the new object arrives as `self`, exactly the mechanism from Lesson 01 Part 3.3.
3. **Return** the now-initialised object to you.

```python
rex = Dog("Rex", 3)
# roughly equivalent to:
#   rex = <a new blank Dog>
#   Dog.__init__(rex, "Rex", 3)
#   (hand rex back)
```

Two consequences worth internalising:

- **You never call `__init__` yourself.** `Dog(...)` calls it for you. Writing `rex.__init__("Rex", 3)` on an existing object is legal but re-initialises it in place — not what you want.
- **`__init__` must not `return` a value.** Its job is to *modify* `self`, not to produce something. Step 3 above returns the object for you. Adding `return self` is a mistake; returning anything other than `None` is a `TypeError`.

---

## Part 3 — Incomplete Objects Are Now Impossible

This is the payoff. Try to make the Part 0 mistake now:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

rex = Dog("Rex")     # forgot the age
```

```text
Traceback (most recent call last):
  File "dogs.py", line 6, in <module>
    rex = Dog("Rex")
TypeError: Dog.__init__() missing 1 required positional argument: 'age'
```

Compare this with Part 0's failure mode:

| | Lesson 01 approach | With `__init__` |
|---|---|---|
| **Error type** | `AttributeError` | `TypeError` |
| **When you find out** | Later, whenever something reads `.age` | Immediately, at the creation line |
| **Where the traceback points** | The innocent code that *used* the dog | The actual line that built it wrong |
| **Can a broken object exist?** | Yes, and it circulates | No — creation fails outright |

That third row is the real prize. The error now points at the line you need to fix.

---

## Part 4 — Default Parameter Values

### 4.1 The basics

`__init__` is an ordinary function, so it takes defaults like any other:

```python
class Dog:
    def __init__(self, name, age=0, breed="Unknown"):
        self.name = name
        self.age = age
        self.breed = breed

d1 = Dog("Rex")                     # age=0,  breed="Unknown"
d2 = Dog("Fido", 2, "Labrador")     # all three given
d3 = Dog("Buddy", breed="Poodle")   # keyword arg skips over age
```

| Call | `name` | `age` | `breed` |
|---|---|---|---|
| `Dog("Rex")` | `"Rex"` | `0` | `"Unknown"` |
| `Dog("Fido", 2, "Labrador")` | `"Fido"` | `2` | `"Labrador"` |
| `Dog("Buddy", breed="Poodle")` | `"Buddy"` | `0` | `"Poodle"` |

`d3` is why keyword arguments matter: `breed` is third, but naming it lets you skip `age` without passing a placeholder.

One hard rule — parameters **with** defaults must come after parameters **without** them:

```python
def __init__(self, age=0, name):    # SyntaxError
```
```text
SyntaxError: parameter without a default follows parameter with a default
```

### 4.2 The mutable default trap — read this twice

This is the single most notorious bug in Python, and it bites hardest in `__init__`. It looks completely reasonable:

```python
class Dog:
    def __init__(self, name, tricks=[]):     # <-- BUG
        self.name = name
        self.tricks = tricks

rex  = Dog("Rex")
fido = Dog("Fido")

rex.tricks.append("sit")

print(rex.tricks)     # ['sit']
print(fido.tricks)    # ['sit']   <-- Fido learned it too?!
```

Only Rex was taught to sit, yet Fido knows the trick. Confirm the cause:

```python
print(rex.tricks is fido.tricks)    # True -- ONE list, shared by both dogs
```

**Why:** the default value `[]` is evaluated **once**, when the `def` line is first executed — not once per call. Every `Dog` created without an explicit `tricks` argument receives *the very same list object*. They aren't copies. They're one list with two names.

**The fix** — default to `None`, then build a fresh list inside the body:

```python
class Dog:
    def __init__(self, name, tricks=None):
        self.name = name
        self.tricks = [] if tricks is None else tricks   # a NEW list per object
```

```python
rex, fido = Dog("Rex"), Dog("Fido")
rex.tricks.append("sit")
print(rex.tricks, fido.tricks)      # ['sit'] []
print(rex.tricks is fido.tricks)    # False -- separate lists at last
```

**The rule:** immutable defaults (`0`, `""`, `None`, `True`, tuples) are safe. Mutable defaults (`[]`, `{}`, `set()`) are a bug. Use `None` as the signal and construct the real value in the body.

---

## Part 5 — `__init__` Is Not Technically a Constructor

In some languages the setup method also *creates* the object. In Python those are two separate jobs:

| Method | Job | How often you write it |
|---|---|---|
| `__new__` | **Creates** the blank object | Almost never |
| `__init__` | **Initialises** the object that already exists | Constantly |

That's why the name is `__init__` (**init**ialise) and not `__construct__`. By the time your `__init__` runs, `self` already exists — it's just empty. This also explains why `__init__` doesn't return the object: it never made it.

You will likely never need `__new__`. It matters only for exotic cases like subclassing immutable types. Know the name so the word "constructor" doesn't mislead you.

---

## Part 6 — The Missing-`self` Pitfall, Done Properly

Forgetting `self` is the most common `__init__` error, and it has **two different failure modes**. Most tutorials only describe one, which is why the error is confusing when you meet the other.

### 6.1 Loud failure — the usual case

```python
class Dog:
    def __init__(name, age):     # no self
        name = name
        age = age

rex = Dog("Rex", 3)
```
```text
TypeError: Dog.__init__() takes 2 positional arguments but 3 were given
```

Do the arithmetic, because that's what makes the message readable. `__init__` declares 2 slots (`name`, `age`). You passed 2 values, and the dot machinery added the new object in front — 3 values for 2 slots. Hence *"3 were given."*

### 6.2 Silent failure — the dangerous case

Now pass **one** argument instead of two:

```python
class Dog:
    def __init__(name, age):     # still no self
        name = name
        age = age

rex = Dog("Rex")        # no error whatsoever
```

Nothing is raised. The counts happen to line up: 1 value passed + 1 object inserted = 2 values for 2 slots. So:

| Parameter | What it actually received |
|---|---|
| `name` | the new `Dog` object |
| `age` | `"Rex"` |

Every parameter is silently shifted one position. And because the body says `name = name` (assigning a local to itself) rather than `self.name = name`, **nothing is stored on the object at all**. You get back a `Dog` with no attributes and no error message — the worst possible outcome, discovered much later as a baffling `AttributeError`.

This is also why `name = name` inside `__init__` is always a bug even *with* `self` present: it assigns a local variable to itself and throws the value away. Storage requires `self.`.

**The rule:** every instance method's first parameter is `self`. No exceptions in this whole module.

---

## Part 7 — Predict, Then Run

1. ```python
   class Dog:
       def __init__(self, name):
           self.name = name
           return self          # <-- what does this do?
   d = Dog("Rex")
   ```

2. ```python
   class Counter:
       def __init__(self, items={}):
           self.items = items
   a, b = Counter(), Counter()
   a.items["x"] = 1
   print(b.items)
   ```

3. ```python
   class Dog:
       def __init__(self, name, age=0):
           self.name = name
           self.age = age
   d = Dog(age=5, name="Rex")     # both as keywords, reversed order
   print(d.name, d.age)
   ```

4. ```python
   class Dog:
       def __init__(self, name):
           self.name = name
   d = Dog("Rex")
   d.__init__("Fido")
   print(d.name)
   ```

<details>
<summary>Answers (predict first)</summary>

1. `TypeError: __init__() should return None, not 'Dog'`. `__init__` initialises; it must not return a value. Part 2 explains why — returning the object is not its job.
2. `{'x': 1}`. The same mutable-default trap as Part 4.2, with a dict instead of a list. One dict shared by every `Counter`.
3. `Rex 5`. Keyword arguments are matched by name, so order is irrelevant when every argument is named.
4. `Fido`. Calling `__init__` by hand is legal — it just re-runs the setup on an existing object. Legal, but never how you should build objects.

</details>

---

## Part 8 — Cheat Sheet Summary

```python
class Dog:
    def __init__(self, name, age=0, tricks=None):   # self FIRST; defaults last
        self.name = name                            # attribute <- parameter
        self.age = age
        self.tricks = [] if tricks is None else tricks   # never tricks=[]

rex = Dog("Rex", 3)      # __init__ runs automatically; never call it yourself
```

| Idea | One-line version |
|---|---|
| What `__init__` is for | Setting up an object's starting attributes, automatically |
| When it runs | Automatically, as part of `ClassName(...)` |
| `self.name = name` | Copy the temporary parameter into permanent object storage |
| `ClassName(...)` does | create blank object → call `__init__` on it → return it |
| Must it return? | No — returning anything but `None` is a `TypeError` |
| Missing an argument | `TypeError: ... missing 1 required positional argument` — at the creation line |
| Defaults | Ordinary function defaults; must come after non-default parameters |
| **Mutable defaults** | `tricks=[]` is shared by every object. Use `None` and build inside |
| Missing `self` | Loud `TypeError` on arity mismatch, **silent corruption** when counts coincide |
| `__init__` vs `__new__` | Initialises vs creates. You write `__init__`; `__new__` is rare |

---

## Self-Check

- [ ] Why does `__init__` fix the `AttributeError` problem from Lesson 01?
- [ ] In `self.name = name`, what is each side, and which one survives the method call?
- [ ] Name the three steps `Dog("Rex", 3)` performs.
- [ ] Why is `def __init__(self, tricks=[])` a bug, and what's the fix?
- [ ] Give the two different things that can happen if you forget `self`.
- [ ] Why doesn't `__init__` return the new object?

---

## 📚 Resources

- **W3Schools:** [Python Classes/Objects — `__init__`](https://www.w3schools.com/python/python_classes.asp)
- **YouTube:** [Corey Schafer — Python OOP Tutorial 1: Classes and Instances](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)
- **Real Python:** [Python's Mutable Default Arguments](https://realpython.com/python-mutable-default-arguments/) — pairs with Part 4.2
- **Docs:** [Python Data Model — `__init__`](https://docs.python.org/3/reference/datamodel.html#object.__init__)

---

## 🧠 Try It Yourself

Open `exercises.py` in this folder:

1. Rewrite `Car` with `__init__(self, make, model, year=2024, mileage=0)` and build two cars in one line each (Part 1.1, 4.1).
2. Create a car without a year to confirm the default applies (Part 4.1).
3. Add `drive(self, miles)` that adds to `self.mileage`; call it twice and print the running total (Part 1.2).
4. Trigger `TypeError: ... missing 1 required positional argument` on purpose, and note which line the traceback blames (Part 3).
5. Add a `repairs=None` parameter that becomes a fresh empty list per car. Prove two cars don't share it with an `is` check — then try it with `repairs=[]` and watch the bug appear (Part 4.2).
