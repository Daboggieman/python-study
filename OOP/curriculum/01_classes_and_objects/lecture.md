# OOP 01: Classes and Objects — A Manual Walkthrough

**Prerequisite:** functions, loops, lists, and dictionaries.
**By the end you will be able to:** explain what a class and an object actually *are*, create objects, give them data and behaviour, and say precisely what `self` means — no loose ends left for later lessons.

> **How to read this lesson.** Every code block is runnable. When you see a **State** table, it shows what actually exists in memory at that moment. When you see a **Predict** box, cover the output with your hand and guess before reading on. That guessing step is where the learning happens.

---

## Part 0 — The One Problem OOP Exists To Solve

Don't start with the definition. Start with the pain, because the definition only makes sense once you've felt it.

### 0.1 One dog is easy

You want to track a dog's name and age:

```python
dog_name = "Rex"
dog_age = 3
```

Fine. Nothing wrong here.

### 0.2 Three dogs start to hurt

```python
dog1_name = "Rex"
dog1_age = 3
dog2_name = "Fido"
dog2_age = 5
dog3_name = "Buddy"
dog3_age = 2
```

Six variables for three dogs. For thirty dogs you'd need sixty. And notice the real damage: **nothing in the code says `dog1_name` and `dog1_age` belong together.** That pairing exists only in your head and in the naming convention. The computer sees six unrelated variables.

Now write a function that describes a dog:

```python
def describe(name, age):
    print(f"{name} is {age} years old")

describe(dog1_name, dog1_age)   # Rex is 3 years old
describe(dog2_age, dog2_name)   # 5 is Fido years old   <-- oops
```

That second call is a real bug, and Python raises no error at all. It happily prints nonsense, because as far as Python is concerned you passed two values in the order the function asked for. **The data has no glue.**

### 0.3 The dictionary attempt gets you halfway

You already know a fix for the glue problem:

```python
dog1 = {"name": "Rex", "age": 3}
dog2 = {"name": "Fido", "age": 5}

def describe(dog):
    print(f"{dog['name']} is {dog['age']} years old")

describe(dog1)   # Rex is 3 years old
```

This is genuinely better, and for small scripts it is often the right answer. Name and age now travel together as one value, and `describe` takes one argument instead of two-in-the-right-order.

### 0.4 Where the dictionary still fails

Three cracks show up as the program grows.

**Crack 1 — nothing guarantees the shape.** Any dictionary at all can be passed in:

```python
describe({"nmae": "Rex", "age": 3})   # typo in the key
```

```text
KeyError: 'name'
```

And you only find out at the moment `describe` runs, not when the bad dictionary was built.

**Crack 2 — the behaviour lives somewhere else.** `describe` is a loose function at module level. Six months later, `describe`, `feed`, `bark`, and `vaccinate` are scattered across three files, and nothing connects them to the thing they operate on. To find everything a dog can *do*, you have to grep.

**Crack 3 — every dog re-declares its own structure.** The knowledge "a dog has a name and an age" is repeated in every literal you write, instead of stated once.

### 0.5 The insight

> **The core insight:** you want to say *once* what a dog is — what data it holds and what it can do — and then stamp out as many dogs as you like from that single description.

That single description is a **class**. Each stamped-out dog is an **object**. That is the whole idea. Everything else in this module is mechanics.

---

## Part 1 — Class = The Description, Object = The Thing

### 1.1 The two words, precisely

| Term | What it is | How many exist |
|---|---|---|
| **Class** | The description: what data this kind of thing holds, what it can do | One, written once |
| **Object** (or **instance**) | One actual thing built from that description, with its own data | As many as you create |

The cookie analogy: the class is the **cookie cutter**, each object is a **cookie**. You own one cutter and it makes any number of cookies. Crucially, the cutter is not a cookie — you can't eat it. In the same way, the class `Dog` is not a dog; it's the description of what dogs are.

### 1.2 Your first class

```python
class Dog:
    pass          # `pass` = "this block is deliberately empty for now"

rex = Dog()       # <-- the parentheses BUILD an object
```

Two things to notice about that last line:

- `Dog` (no parentheses) is the class itself — the cutter.
- `Dog()` (with parentheses) **runs** the class and hands back a brand new object — a cookie.

```python
print(Dog)         # <class '__main__.Dog'>      the description
print(rex)         # <__main__.Dog object at 0x7f...>   an actual thing
```

The `0x7f...` is the memory address where that object lives. Yours will differ, and it will change every run. That's expected — it's a location, not a value.

### 1.3 Each object is genuinely separate

This is the point people most often take on faith without checking. Check it.

```python
class Dog:
    pass

rex  = Dog()
fido = Dog()

print(rex is fido)   # False
print(rex == fido)   # False
print(rex is rex)    # True
```

**Predict first, then read:** why is `rex == fido` `False` when both objects are completely empty and therefore look identical?

Because for objects you write yourself, Python's default answer to "are these equal?" is *"only if they are literally the same object."* Two separate empty dogs are two different things, the same way two blank sheets of paper are two sheets, not one. (You can teach a class to compare by content instead — that's the `__eq__` dunder method, listed in the cheatsheet — but you have to ask for it.)

`is` asks **"same object?"**. `==` asks **"equal value?"**. For your own classes they behave the same until you override `__eq__`, which is why the distinction is easy to miss here and painful to miss later.

---

## Part 2 — Attributes: Giving an Object Data

An **attribute** is a piece of data stored on an object. You reach it with a dot: `rex.name`.

### 2.1 Attaching attributes directly

```python
class Dog:
    pass

rex = Dog()
rex.name = "Rex"
rex.age = 3

print(rex.name, rex.age)    # Rex 3
```

Read `rex.name = "Rex"` as: *"on the object `rex`, create a slot called `name` and put `"Rex"` in it."*

### 2.2 State trace, line by line

Here is what actually exists after each line:

| After line | `rex` holds |
|---|---|
| `rex = Dog()` | *(nothing — an empty object)* |
| `rex.name = "Rex"` | `name → "Rex"` |
| `rex.age = 3` | `name → "Rex"`, `age → 3` |

The object starts empty and you bolt data onto it as you go. Nothing pre-declared the slots.

### 2.3 Objects really don't share data

```python
rex  = Dog()
fido = Dog()

rex.name = "Rex"
fido.name = "Fido"

print(rex.name)    # Rex
print(fido.name)   # Fido      <-- setting one did not touch the other
```

| Object | its own `name` |
|---|---|
| `rex` | `"Rex"` |
| `fido` | `"Fido"` |

Each object carries its own private set of attributes. This is exactly the "glue" that Part 0.2 was missing: `name` and `age` are now welded to a specific dog rather than floating in the module.

### 2.4 But this approach is fragile — here's the proof

Attaching attributes by hand means **nothing guarantees you did it**:

```python
class Dog:
    pass

rex = Dog()
rex.name = "Rex"
# ...forgot rex.age entirely

print(rex.age)
```

```text
Traceback (most recent call last):
  File "dogs.py", line 8, in <module>
    print(rex.age)
AttributeError: 'Dog' object has no attribute 'age'
```

That is the same **Crack 1** from Part 0.4, wearing a different hat. We swapped `KeyError` for `AttributeError` and gained nothing on this front.

This is a real, unsolved limitation of what you've learned so far — not hand-waving. **Lesson 02 (`__init__`) fixes it properly** by making Python demand a name and an age at the moment the object is built, so an incomplete `Dog` becomes impossible to create. For now, know that attaching attributes by hand works and is what you'll do in this lesson's exercises, but it is not how real code does it.

---

## Part 3 — Methods: Giving an Object Behaviour

A **method** is a function defined inside a class. It is the "what it can do" half of the description.

### 3.1 Your first method

```python
class Dog:
    def bark(self):
        print("Woof!")

rex = Dog()
rex.bark()      # Woof!
```

`bark` is written once, on the class, and every `Dog` object can call it.

### 3.2 What `self` is — answered now, not later

Most tutorials tell you to accept `self` on faith here. You don't have to. Here is the entire answer:

> **`self` is the object the method was called on.**

That's it. When you write `rex.bark()`, Python passes `rex` into `bark` as the `self` parameter, automatically. You never pass it yourself — it's filled in for you by the dot.

Why is it needed at all? Because `bark` is defined **once on the class**, but shared by **every** object. So when the method body needs the data of one specific dog, it needs some way to say "whichever dog I was called on":

```python
class Dog:
    def bark(self):
        print(f"{self.name} says Woof!")

rex  = Dog()
rex.name = "Rex"
fido = Dog()
fido.name = "Fido"

rex.bark()    # Rex says Woof!
fido.bark()   # Fido says Woof!
```

One method definition, two different outputs. The difference is entirely *which object arrived as `self`*:

| Call | `self` is bound to | `self.name` reads |
|---|---|---|
| `rex.bark()` | the `rex` object | `"Rex"` |
| `fido.bark()` | the `fido` object | `"Fido"` |

### 3.3 The equivalence that makes it click

These two lines do exactly the same thing:

```python
rex.bark()       # the normal way
Dog.bark(rex)    # what Python actually does under the hood
```

Run both. Identical output. `object.method()` is shorthand for `Class.method(object)` — the dot's job is to grab the thing on its left and slide it in as the first argument.

Once you see that, `self` stops being magic: **it is just an ordinary first parameter that the dot fills in for you.**

### 3.4 What happens if you leave `self` out

Don't take this on trust either — cause the error deliberately:

```python
class Dog:
    def bark():        # no self
        print("Woof!")

rex = Dog()
rex.bark()
```

```text
TypeError: Dog.bark() takes 0 positional arguments but 1 was given
```

Read that message closely, because it's confusing until you know Part 3.3. You wrote `rex.bark()` and passed *nothing*, yet Python complains that **1 argument was given**. That "1" is `rex` itself, slid in by the dot. `bark` declared room for zero arguments, so the object had nowhere to land.

Whenever you see *"takes 0 positional arguments but 1 was given"* on a method, the fix is almost always a missing `self`.

Lesson 03 goes further with `self` — using it to write attributes, and to call other methods on the same object — but there is no remaining mystery about what it *is*.

---

## Part 4 — The Payoff, Demonstrated Rather Than Asserted

Let's be honest about the trade-off instead of just claiming OOP wins.

**At this size, the dictionary version is genuinely fine:**

```python
dog = {"name": "Rex"}
def bark(d): print(f"{d['name']} says Woof!")
```

Nobody should feel bad about that code. So what actually changes as things grow? Three concrete things.

**1. The description lives in one place.** Everything a dog is and does sits inside `class Dog:`. To learn the full capability of a dog you read one block, rather than grepping for functions that happen to take a dog-shaped dictionary.

**2. Behaviour is attached to the data, so it can't be mismatched.** `rex.bark()` cannot possibly run against the wrong thing — you got `bark` *from* `rex`. Compare with `bark(some_dict)`, which will cheerfully accept a dictionary describing a *cat*, then fail deep inside the function.

**3. The bug from Part 0.2 becomes structurally impossible.** There is no argument order left to get wrong:

```python
describe(dog2_age, dog2_name)   # the old bug: silently prints nonsense
rex.describe()                  # no ordering to get wrong — nothing to swap
```

Those are the real wins. Not "OOP is better," but: *one home for the description, behaviour welded to its data, and fewer ways to hold it wrong.*

---

## Part 5 — You've Been Using Objects All Along

This isn't a paradigm you opt into. Python is already built this way:

```python
print(type(5))          # <class 'int'>
print(type("hi"))       # <class 'str'>
print(type([1, 2]))     # <class 'list'>
print(type(None))       # <class 'NoneType'>
print(type(print))      # <class 'builtin_function_or_method'>
```

Every value you have ever used is an object of some class. And that's why the dot syntax already feels familiar — you've been calling methods for ages:

```python
"hi".upper()        # a method on a str object
[3, 1, 2].sort()    # a method on a list object
(5).bit_length()    # 3  -- even integers have methods
```

`"hi".upper()` is `str.upper("hi")` by the rule from Part 3.3. Same mechanism, no exceptions.

One last mind-bender, worth running once:

```python
class Dog: pass
print(type(Dog))    # <class 'type'>
```

The class itself is an object too — an object of class `type`. You don't need this today, but it's why "everything is an object" is meant literally.

---

## Part 6 — Predict, Then Run

Write your predicted output next to each one *before* running it. Getting a prediction wrong is the fastest way to find the gap in your model.

1. ```python
   class Cat: pass
   a = Cat()
   b = a                 # note: no second Cat() call
   print(a is b)
   ```
   *(Think carefully — this one is not `False`. Why not?)*

2. ```python
   class Cat: pass
   a = Cat()
   a.name = "Tom"
   b = Cat()
   print(b.name)
   ```
   *(What error, and what does its message say exactly?)*

3. ```python
   class Cat:
       def speak(self):
           print("Meow")
   c = Cat()
   Cat.speak(c)
   ```

4. ```python
   class Cat:
       def speak(self):
           print(f"{self.name} says Meow")
   c = Cat()
   c.speak()
   ```
   *(Which line does the traceback blame — the call, or the `print` inside the method?)*

<details>
<summary>Answers (open only after committing to a prediction)</summary>

1. `True`. `b = a` copies the *reference*, not the object — both names point at one single cat. Only `Cat()` creates a new object.
2. `AttributeError: 'Cat' object has no attribute 'name'`. Setting `name` on `a` did nothing to `b`; attributes are per-object.
3. `Meow`. Explicit form of `c.speak()`, exactly as in Part 3.3.
4. `AttributeError: 'Cat' object has no attribute 'name'`, and the traceback blames **both** — it shows the `c.speak()` call line *and* the `print` line inside `speak`, because the error happened inside the method that the call reached. Reading tracebacks bottom-up tells you what broke; reading top-down tells you how you got there.

</details>

---

## Part 7 — Cheat Sheet Summary

```python
class Dog:                 # define the description (capitalised by convention)
    def bark(self):        # a method; `self` = the object it's called on
        print(f"{self.name} says Woof!")

rex = Dog()                # build an object   <- parentheses do the building
rex.name = "Rex"           # attach an attribute (temporary approach; see Lesson 02)
rex.bark()                 # call the method   <- the dot passes `rex` in as `self`
```

| Idea | One-line version |
|---|---|
| **Class** | The single description of what a kind of thing holds and does |
| **Object / instance** | One actual thing built from that description, with its own data |
| `Dog` vs `Dog()` | The description vs a new thing built from it |
| **Attribute** | Data on an object, reached with a dot: `rex.name` |
| **Method** | A function defined in the class, called on an object |
| `self` | The object the method was called on — an ordinary first parameter the dot fills in |
| `obj.meth()` | Shorthand for `Class.meth(obj)` |
| `is` vs `==` | "same object?" vs "equal value?" — identical for your classes until you write `__eq__` |
| Attributes are | **per-object**; setting one object's attribute never touches another's |

**Still open after this lesson** — nothing about `self`, and one real gap: attaching attributes by hand doesn't guarantee an object is complete (Part 2.4). That is precisely what Lesson 02 solves.

---

## Self-Check

You've got this lesson if you can answer these without scrolling up:

- [ ] What's the difference between `Dog` and `Dog()`?
- [ ] Why is `rex == fido` `False` for two empty objects?
- [ ] What exactly is `self`, and who supplies it?
- [ ] Rewrite `rex.bark()` without using the dot on `rex`.
- [ ] You see `takes 0 positional arguments but 1 was given` on a method. What's wrong?
- [ ] Why is attaching attributes by hand fragile, and what's the fix called?

---

## 📚 Resources

- **W3Schools:** [Python Classes/Objects](https://www.w3schools.com/python/python_classes.asp)
- **YouTube:** [Corey Schafer — Python OOP Tutorial 1: Classes and Instances](https://www.youtube.com/watch?v=ZDa-Z5JzLYM) — the most time-tested Python OOP explainer
- **YouTube:** [mCoding — What is `self`, really?](https://www.youtube.com/watch?v=mfM-3PQ2mMc) — pairs directly with Part 3
- **Real Python:** [Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)

---

## 🧠 Try It Yourself

Now open `exercises.py` in this folder and work through it. It follows the parts above in order:

1. Define an empty `Car` class, create two `Car` objects, and confirm `car1 is car2` is `False` (Part 1.3).
2. Attach `make`, `model`, and `year` to one car, then print a sentence describing it (Part 2.1).
3. Add a `honk` method that prints `"Beep beep!"`, and call it (Part 3.1).
4. Add a `describe` method that uses `self` to print `"<year> <make> <model>"` — then call it as both `car1.describe()` and `Car.describe(car1)` and confirm they match (Part 3.3).
5. Deliberately create a third car and call `describe()` on it *without* attaching attributes. Read the `AttributeError` and write a one-line comment explaining what Lesson 02 will do about it (Part 2.4).
6. Run `type()` on `3.14`, `True`, `None`, and `print` — note that even `None` and functions are objects (Part 5).
