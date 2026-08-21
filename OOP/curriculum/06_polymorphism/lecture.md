# OOP 06: Polymorphism — A Manual Walkthrough

**Prerequisite:** Lessons 01–05.
**By the end you will be able to:** use inheritance to share behaviour, override methods, explain the method lookup rule, use `super()` to extend rather than replace, and choose between inheritance-based polymorphism and duck typing.

---

## Part 0 — The Problem: The `if/elif` Chain That Never Stops Growing

You have three kinds of animal and you want each to make its noise. With what you know so far:

```python
def make_noise(animal):
    if animal["kind"] == "dog":
        print(f"{animal['name']} says Woof!")
    elif animal["kind"] == "cat":
        print(f"{animal['name']} says Meow!")
    elif animal["kind"] == "bird":
        print(f"{animal['name']} says Tweet!")
    else:
        print("???")
```

This works. Now look at what it costs you:

- **Adding a fourth animal means editing this function.** And every other function shaped like it — `feed()`, `describe()`, `house()`. One new animal, a dozen edits scattered across the codebase.
- **The knowledge is in the wrong place.** "Dogs say Woof" is a fact about dogs, but it's stored in a function about noises. To learn what a dog does you must read every `if/elif` chain in the project.
- **Forgetting a branch fails silently.** Add `"fish"` and you print `???` rather than getting an error.

> **The core insight:** instead of one function that asks *"what kind of thing is this?"*, let each thing answer for itself. The caller stops choosing behaviour — it just asks, and each object responds in its own way.

**Polymorphism** ("many forms") is that idea: **one method name, many behaviours, selected automatically by the object.**

---

## Part 1 — Inheritance: The Usual Setup

### 1.1 A subclass gets the parent's behaviour for free

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"I am {self.name}"

class Dog(Animal):          # Dog inherits from Animal
    pass
```

`class Dog(Animal):` means *"a Dog is an Animal, plus whatever I add."* Even with an empty body, `Dog` already has everything `Animal` has:

```python
rex = Dog("Rex")            # Animal's __init__ ran
print(rex.describe())       # I am Rex   -- Animal's describe ran
```

Vocabulary: `Animal` is the **parent** / **base** / **superclass**; `Dog` is the **child** / **subclass**. All three words for each are in common use.

### 1.2 Overriding: replacing a parent's method

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclasses must implement speak()")

class Dog(Animal):
    def speak(self):                          # overrides Animal.speak
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
```

`Dog` and `Cat` both **inherit** `__init__` (neither rewrites it) and both **override** `speak`. Defining a method with the same name as the parent's replaces it for that subclass.

### 1.3 The method lookup rule — you already know this one

When you call `rex.speak()`, Python searches in a fixed order:

1. Does **`Dog`** define `speak`? Use it.
2. Otherwise, does **`Animal`**? Use it.
3. Otherwise `object`, then → `AttributeError`.

This is the **same rule as Lesson 04 Part 2.2**, extended one step. There, reads fell through from object → class. Here they keep falling: object → class → parent → grandparent. One mechanism explains attribute shadowing *and* method overriding. Overriding a method is shadowing, done deliberately.

Python will show you the exact chain it searches:

```python
print([c.__name__ for c in Dog.__mro__])     # ['Dog', 'Animal', 'object']
```

`__mro__` is the **M**ethod **R**esolution **O**rder — the search list, in order. `object` is at the end of every chain; every Python class inherits from it, which is why every object already has methods you never wrote.

### 1.4 `NotImplementedError` as a contract

Why did `Animal.speak` raise instead of returning something?

```python
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement speak()")
```

Because "animal in general" has no noise — only specific animals do. Raising states a **requirement**: *any subclass must provide this.* If someone forgets:

```python
class Fish(Animal):
    pass

Fish().speak()
```
```text
NotImplementedError: Subclasses must implement speak()
```

A loud, specific error naming exactly what's missing. Compare with returning `None` instead, which would quietly print `None` and leave you hunting. Compare also with Part 0's `else: print("???")` — same silent failure.

(Python has a stricter tool for this, `abc.ABC`, which refuses to even *create* an incomplete subclass. `NotImplementedError` is the lightweight version and is plenty here.)

---

## Part 2 — Polymorphism in Action

### 2.1 The loop

```python
animals = [Dog("Rex"), Cat("Whiskers"), Dog("Fido")]

for animal in animals:
    print(animal.speak())
```
```text
Rex says Woof!
Whiskers says Meow!
Fido says Woof!
```

One call site, `animal.speak()`, produced three different behaviours. At each iteration Python applies Part 1.3's lookup to whatever object `animal` currently is, and runs what it finds.

### 2.2 Compare against Part 0 directly

| | `if/elif` chain | Polymorphism |
|---|---|---|
| Who picks the behaviour | the caller, by inspecting a tag | the object, by being itself |
| Where "dogs say Woof" lives | inside a noise function | inside `Dog` |
| Adding a new animal | edit every chain | add one class |
| Forgetting a case | silent `???` | loud `NotImplementedError` |

The calling code no longer contains a single `if` about animal types. It doesn't know how many kinds exist, and doesn't need to.

### 2.3 The real payoff: extension without modification

Add a `Bird` — and change **nothing** else:

```python
class Bird(Animal):
    def speak(self):
        return f"{self.name} says Tweet!"

animals = [Dog("Rex"), Cat("Whiskers"), Bird("Tweety")]
for animal in animals:
    print(animal.speak())      # the loop is untouched
```
```text
Rex says Woof!
Whiskers says Meow!
Tweety says Tweet!
```

The loop was written before `Bird` existed and works with it anyway. That's the practical value: **code that works with the general interface automatically works with subclasses written later** — including ones written by other people, after your code shipped.

---

## Part 3 — Duck Typing: Python's Looser Version

### 3.1 No shared parent required

Here's the part that surprises people coming from other languages: Python never checked that `animal` was an `Animal`. It only tried to call `.speak()`. So a completely unrelated class works too:

```python
class Robot:                 # no parent, no relation to Animal at all
    def speak(self):
        return "BEEP BOOP I AM SPEAKING"

for thing in [Dog("Fido"), Robot()]:
    print(thing.speak())
```
```text
Fido says Woof!
BEEP BOOP I AM SPEAKING
```

This is **duck typing**: *"if it walks like a duck and quacks like a duck, treat it as a duck."* Python cares about **what an object can do**, not what it *is*. Having a `speak` method is the entire qualification.

### 3.2 What it costs — the failure is deferred

Flexibility has a price. Nothing verifies the method exists until the instant you call it:

```python
class Rock:
    pass                     # no speak method

for thing in [Duck(), Rock()]:
    print(thing.speak())
```
```text
Quack!
Traceback (most recent call last):
  ...
AttributeError: 'Rock' object has no attribute 'speak'
```

Note it printed `Quack!` **first**. Half the loop ran, then it died partway through — leaving whatever it had already done in place. With a shared base class raising `NotImplementedError`, you get a clearer message naming the contract; with `abc.ABC` you'd have been stopped at class-creation time. Duck typing pushes the check as late as possible.

### 3.3 Which should you use?

| Use **inheritance** when | Use **duck typing** when |
|---|---|
| The classes genuinely are a kind of the same thing | They're unrelated but happen to share an ability |
| You want shared code in a base class (`__init__`, `describe`) | Each implementation is entirely its own |
| You want a written contract via `NotImplementedError` / `ABC` | You're accepting objects from code you don't control |

In practice both appear together constantly: a base class for your own family of types, and duck typing at the boundary so other people's objects can join in. The `people` loop in the `oop_super_extend_duck_typing` quest does exactly this — `Manager` inherits, `Contractor` ducks.

**A note on `isinstance`:** you *can* check types explicitly:

```python
print(isinstance(Dog("Rex"), Animal))    # True -- a Dog is an Animal
```

It's occasionally necessary, but reaching for it inside a loop over mixed types usually means you've rebuilt Part 0's `if/elif` chain with fancier syntax. Prefer calling the method.

---

## Part 4 — `super()`: Extending Instead of Replacing

### 4.1 The problem with a plain override

Overriding **replaces** the parent's method entirely. Often you want the parent's work *plus* something extra:

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def describe(self):
        return f"I am {self.name}"

class Dog(Animal):
    def describe(self):
        return f"I am {self.name}, a good dog"     # duplicates the parent's wording
```

That literal `"I am ..."` is now written twice. Change the format in `Animal` and `Dog` silently disagrees with it.

### 4.2 `super()` calls the parent's version

```python
class Dog(Animal):
    def describe(self):
        base = super().describe()      # run Animal's version, keep its return value
        return base + ", a good dog"

print(Dog("Rex").describe())           # I am Rex, a good dog
```

`super()` gives you the *next class up the MRO* (Part 1.3), so `super().describe()` runs `Animal.describe`. No `self` is passed — `super()` already knows which object it's working with.

The parent's wording now exists in exactly one place. Change `Animal.describe` and `Dog` follows automatically.

### 4.3 `super()` in `__init__`

This is where you'll use it most. A subclass that adds data still wants the parent's setup:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)      # parent stores self.name
        self.breed = breed          # then add what's new to Dog

rex = Dog("Rex", "Labrador")
print(rex.name, rex.breed)          # Rex Labrador
```

Two rules that catch people:

- **No `self` in the call.** `super().__init__(name)`, not `super().__init__(self, name)` — the latter is a `TypeError` for exactly the arity reason from Lesson 02 Part 6.1.
- **Don't re-do the parent's work.** Writing `self.name = name` yourself instead of delegating defeats the point; if `Animal.__init__` later starts validating the name, your subclass would skip the validation.

### 4.4 Why `super()` and not `Animal.describe(self)`?

You *can* name the parent explicitly, and in a simple two-level chain it behaves identically:

```python
    def describe(self):
        return Animal.describe(self) + ", a good dog"    # works, but don't
```

Two reasons not to. The mundone one: it repeats the parent's name, so renaming the parent or inserting a class in between means editing every subclass.

The real one: with more than one parent, hardcoding **silently skips classes**. Given `Both(Left, Right)` where both inherit from `Base`:

```python
print([c.__name__ for c in Both.__mro__])
# ['Both', 'Left', 'Right', 'Base', 'object']
```

| Approach | Result |
|---|---|
| `super().go()` throughout | `Both->Left->Right->Base` ✔ every class ran |
| `Left.go(self)` / `Base.go(self)` hardcoded | `Both->Left->Base` ✘ **`Right` never ran** |

`super()` walks the MRO, which accounts for every class exactly once. Hardcoded names jump straight to a specific class and skip whatever sat between. You won't write diamond hierarchies soon, but the habit costs nothing and this is why the habit exists.

---

## Part 5 — Built-In Polymorphism You've Used All Along

You have been relying on this since your first Python lesson:

```python
print(len("hello"))         # 5
print(len([1, 2, 3]))       # 3
print(len({"a": 1, "b": 2}))  # 2

print(1 + 2)                # 3
print("a" + "b")            # ab
print([1, 2] + [3, 4])      # [1, 2, 3, 4]
```

One name, `len`, three behaviours. One operator, `+`, three meanings — numeric addition, string concatenation, list joining.

The mechanism is exactly Part 1.2's overriding. `len(x)` calls `x.__len__()`, and `a + b` calls `a.__add__(b)`; each type provides its own version of those dunder methods. `len` is polymorphic for the same reason `speak` is.

Which means you can join in. Give your class `__len__` and the built-in `len()` starts working on it:

```python
class Pack:
    def __init__(self, dogs):
        self.dogs = dogs
    def __len__(self):
        return len(self.dogs)

print(len(Pack(["Rex", "Fido"])))    # 2
```

`len()` had never heard of `Pack`, and needed no modification — the same "extension without modification" from Part 2.3, this time applied to Python's own built-ins. The cheatsheet in `resources/` lists the other dunders worth knowing (`__str__`, `__eq__`, `__add__`, …).

---

## Part 6 — Predict, Then Run

1. ```python
   class A:
       def hi(self): return "A"
   class B(A):
       pass
   class C(B):
       def hi(self): return "C"
   print(A().hi(), B().hi(), C().hi())
   ```

2. ```python
   class Animal:
       def __init__(self, name): self.name = name
   class Dog(Animal):
       def __init__(self, name, breed):
           self.breed = breed          # forgot super().__init__
   d = Dog("Rex", "Lab")
   print(d.name)
   ```

3. ```python
   class A:
       def greet(self): return "hello"
   class B(A):
       def greet(self): return super().greet().upper()
   print(B().greet())
   ```

4. ```python
   class Box:
       def __init__(self, items): self.items = items
   print(len(Box([1, 2, 3])))
   ```

<details>
<summary>Answers (predict first)</summary>

1. `A A C`. `B` defines no `hi`, so lookup falls through to `A` (Part 1.3). `C` overrides it, so `C` wins for `C`.
2. `AttributeError: 'Dog' object has no attribute 'name'`. Overriding `__init__` **replaced** the parent's entirely, so `self.name` was never set — the Part 4.3 mistake. Fix: `super().__init__(name)`.
3. `HELLO`. `super().greet()` returns the parent's string, then `.upper()` transforms it — extending rather than replacing (Part 4.2).
4. `TypeError: object of type 'Box' has no len()`. `len()` needs `__len__`, and `Box` doesn't define one (Part 5). Having an `items` list isn't enough — the dunder must be there.

</details>

---

## Part 7 — Cheat Sheet Summary

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):                              # the contract
        raise NotImplementedError("Subclasses must implement speak()")

    def describe(self):
        return f"I am {self.name}"


class Dog(Animal):                                # inherits
    def __init__(self, name, breed):
        super().__init__(name)                    # parent's setup, no `self` passed
        self.breed = breed

    def speak(self):                              # overrides
        return f"{self.name} says Woof!"

    def describe(self):                           # extends via super()
        return super().describe() + ", a good dog"


class Robot:                                      # unrelated -- duck typing
    def speak(self):
        return "BEEP BOOP"


for thing in [Dog("Rex", "Lab"), Robot()]:        # one call, many behaviours
    print(thing.speak())
```

| Idea | One-line version |
|---|---|
| Polymorphism | One method name, many behaviours, chosen by the object |
| `class Dog(Animal)` | Dog is an Animal plus extras; inherits everything |
| Overriding | Redefining a parent's method replaces it for that subclass |
| **Method lookup** | subclass → parent → grandparent → `object`; same rule as Lesson 04 |
| `__mro__` | The actual search order Python will use |
| `NotImplementedError` | States a contract: subclasses must supply this |
| Duck typing | Any object with the right method works; no shared parent needed |
| Duck typing's cost | Missing method → `AttributeError`, only when called, mid-loop |
| `super().method()` | Run the parent's version; extend instead of replace |
| `super().__init__(...)` | Parent's setup — pass **no** `self` |
| Override `__init__` without `super()` | Parent's attributes are never set → `AttributeError` |
| Why not `Parent.m(self)` | Repeats the name, and with multiple parents **skips classes** |
| `len`, `+` | Already polymorphic, via `__len__` / `__add__`; your classes can join in |

---

## Self-Check

- [ ] What three costs does the `if/elif` chain in Part 0 have?
- [ ] State the method lookup order, and say how it relates to Lesson 04's attribute lookup.
- [ ] Why does `Animal.speak` raise instead of returning `None`?
- [ ] What must an object have to work in a duck-typed loop, and when do you find out it doesn't?
- [ ] What breaks if a subclass overrides `__init__` and never calls `super().__init__()`?
- [ ] Give a case where `Parent.method(self)` and `super().method()` genuinely differ.

---

## 📚 Resources

- **W3Schools:** [Python Polymorphism](https://www.w3schools.com/python/python_polymorphism.asp) · [Python Inheritance](https://www.w3schools.com/python/python_inheritance.asp)
- **YouTube:** [Corey Schafer — Inheritance](https://www.youtube.com/watch?v=RSl87lqOXDE) — pairs with Parts 1 and 4
- **Real Python:** [Inheritance and Composition: A Python OOP Guide](https://realpython.com/inheritance-composition-python/)
- **Real Python:** [Supercharge Your Classes With `super()`](https://realpython.com/python-super/) — pairs with Part 4
- **Docs:** [`super()`](https://docs.python.org/3/library/functions.html#super)

---

## 🧠 Try It Yourself

Open `exercises.py` in this folder:

1. Implement `Dog.speak()` and `Cat.speak()` overriding `Animal.speak`, put several in one list, and loop calling `.speak()` (Parts 1.2, 2.1).
2. Implement `Bird.speak()` and add a bird to the same list **without touching the loop** (Part 2.3).
3. Before implementing them, run the file once and read the `NotImplementedError` from the base class (Part 1.4).
4. Implement `Robot.speak()` — note `Robot` has no parent — and confirm it works in the same loop via duck typing (Part 3.1).
5. Implement `DescriptiveDog.describe()` using `super().describe()` to extend rather than replace (Part 4.2).
6. Print `[c.__name__ for c in Dog.__mro__]` and check it matches the lookup order from Part 1.3.
7. Add a class with no `speak` method to the duck-typed list, run it, and note both the error **and** how much of the loop ran first (Part 3.2).
