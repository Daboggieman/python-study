# OOP 04: Class Properties — A Manual Walkthrough

**Prerequisite:** Lessons 01–03.
**By the end you will be able to:** tell instance attributes from class attributes and predict which one you're touching, explain Python's attribute lookup rule, avoid the three sharing traps, and use `@property` to validate data without changing how callers write their code.

---

## Part 0 — Two Different Questions

So far every attribute has belonged to **one object**: `rex.name` is Rex's and nobody else's. That covers most data, but not all of it. Two questions have different answers:

| Question | Example | Belongs to |
|---|---|---|
| "What's *this dog's* name?" | `"Rex"` | one object |
| "What species are dogs?" | `"Canis familiaris"` | every dog, equally |

Storing the species on every object would duplicate the same string thousands of times, and updating it would mean visiting every dog. It isn't per-dog data — it's a fact about dogs *in general*.

There's also a second, unrelated problem this lesson solves. Right now attributes are wide open:

```python
rex.age = -50        # nothing stops this
```

An age of `-50` is nonsense, but a plain attribute accepts anything. We want validation — **without** forcing every caller to switch from `rex.age = 5` to `rex.set_age(5)`.

> **The core insight:** attributes come in two scopes — per-object and per-class — and Python lets a plain-looking attribute secretly run code, so you can add validation without changing how it's used.

---

## Part 1 — Instance Attributes (Per-Object)

You already know these. Set with `self.x = ...`, one independent copy per object:

```python
class Dog:
    def __init__(self, name):
        self.name = name        # instance attribute

rex  = Dog("Rex")
fido = Dog("Fido")
rex.name = "Rexy"

print(rex.name, fido.name)      # Rexy Fido -- changing one left the other alone
```

---

## Part 2 — Class Attributes (Shared)

### 2.1 Defined in the class body, not in `__init__`

```python
class Dog:
    species = "Canis familiaris"     # class attribute -- in the class body

    def __init__(self, name):
        self.name = name              # instance attribute -- in __init__
```

The **position in the file** is what decides which kind you get. Class body → one shared value. Inside `__init__` with `self.` → one per object.

```python
rex, fido = Dog("Rex"), Dog("Fido")
print(rex.species, fido.species)     # Canis familiaris Canis familiaris
print(Dog.species)                    # Canis familiaris -- readable on the class itself

Dog.species = "Updated"               # change it once...
print(rex.species, fido.species)     # Updated Updated -- ...every dog sees it
```

Note `Dog.species` works with **no object at all**. The value lives on the class, so you don't need a dog to read it.

### 2.2 The lookup rule — the mechanism behind everything in this lesson

When you write `rex.species`, Python searches in a fixed order:

1. Does the **object** have a `species` of its own? Use that.
2. Otherwise, does the **class** have one? Use that.
3. Otherwise → `AttributeError`.

You can watch this directly. Every object carries a `__dict__` holding only its *own* attributes:

```python
class Dog:
    species = "canine"

rex = Dog()
print(rex.species, rex.__dict__)     # canine {}
```

`rex.__dict__` is **empty** — yet `rex.species` returned a value. Step 1 found nothing, step 2 found it on the class. Now assign to it:

```python
rex.species = "wolf"
print(rex.species, rex.__dict__)     # wolf {'species': 'wolf'}
```

The assignment wrote into *the object's* dict. Now step 1 succeeds and the class's value is never consulted. Proof that the class value is untouched — delete the instance one:

```python
del rex.species
print(rex.species, rex.__dict__)     # canine {}   <-- the class attribute reappears
```

Nothing was destroyed. The instance attribute was merely sitting *in front of* the class attribute. Reads fall through to the class; **writes always land on the object.** Hold onto that sentence — the next three traps are all the same sentence in different costumes.

### 2.3 Trap 1 — shadowing

```python
class Dog:
    species = "Canis familiaris"

rex, fido = Dog(), Dog()
rex.species = "Rex only"

print(rex.species)      # Rex only
print(fido.species)     # Canis familiaris   <-- unaffected
print(Dog.species)      # Canis familiaris   <-- unaffected
```

If you *intended* to change the species for all dogs, you failed silently. `rex.species = ...` can never modify a class attribute — writes always land on the object (Part 2.2). To change it for everyone you must name the class: `Dog.species = ...`.

### 2.4 Trap 2 — the counter that never counts

The natural way to count objects is a shared class attribute. Here's the version that looks right and does nothing:

```python
class Dog:
    population = 0

    def __init__(self):
        self.population += 1        # BUG

Dog(); Dog(); Dog()
print(Dog.population)               # 0   <-- never moved
```

Unpack `self.population += 1`, which is really `self.population = self.population + 1`:

| Half | Which rule applies | Result |
|---|---|---|
| read `self.population` | falls through to the class | `0` |
| write `self.population` | lands on the **object** | creates an instance attribute `= 1` |

So every dog gets its own `population = 1`, and the class's counter sits at `0` forever. Confirm it:

```python
d = Dog()
print(d.__dict__)        # {'population': 1}   <-- the instance shadow
print(Dog.population)    # 0
```

**The fix — name the class explicitly:**

```python
class Dog:
    population = 0

    def __init__(self):
        Dog.population += 1        # writes to the class

Dog(); Dog(); Dog()
print(Dog.population)              # 3
```

This is the one place where writing `Dog.` instead of `self.` is not just acceptable but required. `self.` cannot reach a class attribute for writing.

### 2.5 Trap 3 — a mutable class attribute is shared by everyone

Traps 1 and 2 relied on **assignment**. This one is worse because it involves no assignment at all:

```python
class Dog:
    tricks = []                          # BUG: one list, on the class

    def __init__(self, name):
        self.name = name

    def learn(self, t):
        self.tricks.append(t)            # no `=` anywhere here

rex, fido = Dog("Rex"), Dog("Fido")
rex.learn("sit")

print(rex.tricks)      # ['sit']
print(fido.tricks)     # ['sit']   <-- Fido knows it too
print(rex.__dict__)    # {'name': 'Rex'}   <-- no `tricks` here at all
```

`self.tricks.append(t)` **reads** `self.tricks` (falling through to the class list) and then mutates that list in place. There's no assignment, so the "writes land on the object" rule never fires — nothing shadows anything, and every dog is appending to the same list.

This is the exact same shape as the mutable-default bug in Lesson 02 Part 4.2: one mutable object created once, shared by everything.

**The fix** — per-object data belongs in `__init__`:

```python
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []          # a fresh list per dog
```

**The rule:** class attributes should be **immutable** (numbers, strings, tuples) or deliberately shared. If each object needs its own list or dict, build it in `__init__`.

---

## Part 3 — When to Use Which

| Use a **class attribute** for | Use an **instance attribute** for |
|---|---|
| Constants shared by every instance (`species`) | Data unique to each object (`name`, `age`) |
| A counter of how many objects exist | Anything set from an `__init__` parameter |
| Default configuration values | Any mutable per-object list or dict |

Quick test: ask *"if I change this, should every existing object see the change?"* Yes → class attribute. No → instance attribute.

---

## Part 4 — Controlled Access with `@property`

### 4.1 The problem

Back to Part 0's second question. You want validation:

```python
c.radius = -5      # should be rejected
```

The classic fix is getter/setter methods — but that changes every call site to `c.get_radius()` / `c.set_radius(-5)`, which is noisy, and in Python it's unnecessary. `@property` lets an attribute **look** identical while secretly running a method.

### 4.2 The getter

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

c = Circle(5)
print(c.radius)     # 5   -- no parentheses, yet a method ran
```

`c.radius` has no `()` but `radius` is a method. That's what `@property` does: it makes attribute *access* trigger a method call.

The leading underscore in `_radius` is a **convention**, not enforcement: *"internal, don't touch from outside."* Nothing stops `c._radius = -5`; the underscore just tells other programmers not to. The names must differ — a property called `radius` storing to `self.radius` would call itself forever.

### 4.3 The setter

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
```

Note the decorator is `@radius.setter` — it attaches to the property created by the getter, so **the getter must be defined first** and both must share the name.

```python
c = Circle(5)
c.radius = 10        # runs the setter, passes validation
print(c.radius)      # 10
c.radius = -3        # ValueError: radius cannot be negative
```

### 4.4 The bug almost every tutorial ships

Look hard at `__init__` above:

```python
    def __init__(self, radius):
        self._radius = radius        # writes the private attribute DIRECTLY
```

It assigns to `self._radius`, not `self.radius` — so it **bypasses the setter entirely**. The validation you just wrote doesn't apply at construction time:

```python
c = Circle(-5)
print(c.radius)      # -5    <-- accepted!
```

Your class rejects `c.radius = -5` but happily accepts `Circle(-5)`. Validation with a hole in it.

**The fix — assign through the property in `__init__`:**

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius         # note: NO underscore -- routes through the setter

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius cannot be negative")
        self._radius = value
```

```python
Circle(-5)      # ValueError: radius cannot be negative
```

`self.radius = radius` looks like it would recurse, but it doesn't: the *setter* runs and stores to `self._radius`, a different name. One validation rule, enforced everywhere.

> **The rule:** in `__init__`, assign to `self.<property_name>`, not `self._<private_name>`, so construction obeys the same rules as later assignment.

### 4.5 Read-only computed properties

Omit the setter and the attribute becomes read-only — and it can be **computed** rather than stored:

```python
    @property
    def area(self):
        return 3.14159 * self._radius ** 2
```

```python
c = Circle(5)
print(round(c.area, 2))     # 78.54
c.radius = 10
print(round(c.area, 2))     # 314.16   <-- recalculated, never stale
```

`area` isn't stored anywhere. It's derived on every access, so it can't drift out of sync with `radius` — a whole class of bug removed by not storing the value twice.

And because there's no setter, assigning is refused:

```python
c.area = 100
```
```text
AttributeError: property 'area' of 'Circle' object has no setter
```

That message is exactly what you want: the class is telling callers `area` is derived, not owned.

---

## Part 5 — Predict, Then Run

1. ```python
   class Dog:
       legs = 4
   a, b = Dog(), Dog()
   a.legs = 3
   Dog.legs = 5
   print(a.legs, b.legs)
   ```

2. ```python
   class Basket:
       items = []
       def add(self, x): self.items.append(x)
   b1, b2 = Basket(), Basket()
   b1.add("apple")
   print(len(b2.items))
   ```

3. ```python
   class Temp:
       def __init__(self, c): self._c = c
       @property
       def f(self): return self._c * 9/5 + 32
   t = Temp(100)
   t.f = 50
   ```

4. ```python
   class P:
       def __init__(self, v): self.v = v
       @property
       def v(self): return self._v
       @v.setter
       def v(self, val): self._v = val * 2
   print(P(10).v)
   ```

<details>
<summary>Answers (predict first)</summary>

1. `3 5`. `a.legs = 3` created an instance attribute shadowing the class one, so `a` keeps `3`. `b` never got its own, so it falls through to the class and sees the updated `5`.
2. `1`. Trap 3 (Part 2.5) — `items` is one list on the class, shared by both baskets. `b2` sees the apple.
3. `AttributeError: property 'f' of 'Temp' object has no setter`. Getter only → read-only.
4. `20`. `self.v = v` in `__init__` routes through the setter (Part 4.4), which doubles the value before storing. This is the mechanism that makes the 4.4 fix work — and a reminder that a setter can transform, not just validate.

</details>

---

## Part 6 — Cheat Sheet Summary

```python
class Dog:
    species = "Canis familiaris"     # class attribute: shared, immutable
    population = 0                    # class attribute used as a counter

    def __init__(self, name):
        self.name = name              # instance attribute: per object
        self.tricks = []              # mutable per-object data belongs HERE
        Dog.population += 1           # `Dog.`, not `self.`, to write the class attr


class Circle:
    def __init__(self, radius):
        self.radius = radius          # through the property, so validation applies

    @property                         # getter -- defined first
    def radius(self):
        return self._radius

    @radius.setter                    # setter -- same name as the getter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius cannot be negative")
        self._radius = value

    @property                         # no setter => read-only, computed fresh
    def area(self):
        return 3.14159 * self._radius ** 2
```

| Idea | One-line version |
|---|---|
| Instance attribute | Set via `self.x` in `__init__`; one per object |
| Class attribute | Set in the class body; one shared by all |
| **Lookup rule** | Read: object first, then class. **Write: always the object** |
| `rex.species = x` | Creates an instance shadow; never changes the class value |
| `self.count += 1` | Silently makes a per-object shadow — counter stays at 0 |
| `Dog.count += 1` | Correct way to update a shared counter |
| Mutable class attribute | Shared by everyone, no assignment needed to leak. Put it in `__init__` |
| `@property` | Makes attribute access run a method; caller syntax unchanged |
| `@x.setter` | Adds validation on write; getter must be defined first |
| Getter with no setter | Read-only: `AttributeError: property 'x' ... has no setter` |
| **`__init__` gotcha** | Assign `self.radius`, not `self._radius`, or validation is bypassed |
| `_name` | Convention for "internal" — advisory only, not enforced |

---

## Self-Check

- [ ] What decides whether an attribute is per-object or shared — a keyword, or where you wrote it?
- [ ] State the lookup rule for reads, and the rule for writes.
- [ ] Why does `self.population += 1` leave `Dog.population` at `0`?
- [ ] Why is a class-level `tricks = []` shared even though `learn()` contains no `=`?
- [ ] How can `Circle(-5)` succeed when `c.radius = -5` raises? What's the fix?
- [ ] How do you make a property read-only, and what error does assigning give?

---

## 📚 Resources

- **W3Schools:** [Python Classes/Objects](https://www.w3schools.com/python/python_classes.asp)
- **YouTube:** [Corey Schafer — Class Variables](https://www.youtube.com/watch?v=BJ-VvGyQxho) — pairs with Part 2
- **YouTube:** [Corey Schafer — Property Decorator](https://www.youtube.com/watch?v=jCzT9XFZ5bw) — pairs with Part 4
- **Real Python:** [Python's property(): Add Managed Attributes](https://realpython.com/python-property/)

---

## 🧠 Try It Yourself

Open `exercises.py` in this folder:

1. Add a class attribute `species` to `Dog`, confirm two dogs share it, then override it on one and check the other and the class are untouched (Part 2.3).
2. Add a `population` counter incremented in `__init__`. Do it with `self.population += 1` first, print `Dog.population`, and see it stuck at `0` — then fix it with `Dog.population += 1` (Part 2.4).
3. Implement `Circle` with a validated `radius` property and a read-only `area`. Confirm a negative radius raises `ValueError` (Part 4.3, 4.5).
4. Now try `Circle(-5)`. If it succeeds, you have the Part 4.4 bug — fix `__init__` to assign through the property, and confirm it now raises.
5. Try `c.area = 100` and record the exact error message in a comment (Part 4.5).
6. In a comment, explain the difference between `self.species = "X"` and `Dog.species = "X"` inside a method, and what each actually affects (Part 2.3).
