# OOP 03: The `self` Parameter — A Manual Walkthrough

**Prerequisite:** Lessons 01–02.
**By the end you will be able to:** use `self` to read and write an object's data, call one method from another, work with two objects of the same class in a single method, and recognise the two `self`-related bugs that silently do nothing.

---

## Part 0 — What You Already Know, and What's Left

Lesson 01 Part 3.2 already answered *what* `self` is:

> **`self` is the object the method was called on** — an ordinary first parameter that the dot fills in for you.

Nothing about that is going to change. This lesson is about *using* it, and about the specific ways people get it wrong. If the sentence above still feels shaky, re-read Lesson 01 Part 3.2–3.4 before continuing — everything here builds on it.

---

## Part 1 — `self` Is Genuinely Just a Parameter

### 1.1 The equivalence, once more

```python
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name} says Woof!")

rex = Dog("Rex")

rex.bark()       # Rex says Woof!
Dog.bark(rex)    # Rex says Woof!   -- identical
```

### 1.2 Proof: look at what the dot actually produces

This is the demonstration that removes the last of the magic. Print the method **without calling it** — leave the parentheses off:

```python
print(Dog.bark)     # <function Dog.bark at 0x7a5a3771dee0>
print(rex.bark)     # <bound method Dog.bark of <__main__.Dog object at 0x7a5a37730350>>
```

Read those two lines carefully, because they are different kinds of thing:

| Expression | What you get | `self` |
|---|---|---|
| `Dog.bark` | a plain **function** | not supplied — you must pass it |
| `rex.bark` | a **bound method** | already attached to `rex` |

The word **bound** is literal: `rex.bark` is a package containing *the function* plus *the object to feed it as `self`*. The dot performed that binding. Calling `rex.bark()` unwraps the package and runs `bark(rex)`.

You can even carry the bound method around, and it remembers its object:

```python
f = rex.bark        # no call yet -- just grabbing the bound method
f()                 # Rex says Woof!   -- still knows it belongs to rex
```

`f` took no arguments, yet it printed Rex's name. The object came along inside the binding. **That** is `self`.

---

## Part 2 — Reading and Writing Attributes Through `self`

### 2.1 Reading

```python
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def show(self):
        print(f"{self.owner}'s balance: {self.balance}")
```

Any method needing this object's data goes through `self.`.

### 2.2 Writing

```python
    def deposit(self, amount):
        self.balance = self.balance + amount
```

Both halves matter, and they do different jobs:

| Part | Direction | Meaning |
|---|---|---|
| `self.balance` on the right | **read** | fetch the current stored value |
| `self.balance` on the left | **write** | store the new value back onto the object |

Drop either `self.` and it breaks. Which brings us to the two bugs.

### 2.3 Bug 1 — the loud one: `UnboundLocalError`

```python
    def deposit(self, amount):
        balance = balance + amount      # both `self.` omitted
```
```text
UnboundLocalError: cannot access local variable 'balance' where it is not associated with a value
```

Because you assigned to a bare `balance`, Python treats it as a **brand-new local variable** for the whole method — so the `balance` on the right refers to that same local, which doesn't have a value yet. The object's `self.balance` was never consulted. Python isn't confused; it's telling you that you invented a local variable and then read it before setting it.

### 2.4 Bug 2 — the silent one, and the nastier of the two

```python
    def deposit(self, amount):
        balance = self.balance + amount     # reads correctly, stores nowhere
```

```python
a = Account("Alice", 100)
a.deposit(50)
print(a.balance)      # 100   <-- the deposit vanished
```

**No error at all.** The right-hand side read the object correctly and computed `150`. But the result went into a local variable named `balance`, which is discarded the instant `deposit` returns. The object was never touched.

This is the bug to fear. It doesn't crash, it doesn't warn, and the money quietly disappears.

> **The rule:** to change an object, the thing on the **left of the `=`** must start with `self.`. A bare name on the left always creates a throwaway local.

---

## Part 3 — Calling One Method From Another

`self` is your handle on this object, so it's also how a method calls the object's *other* methods:

```python
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        self.show()              # call another method on the same object

    def show(self):
        print(f"{self.owner}'s balance: {self.balance}")
```

Note it's `self.show()`, not `show()`. A bare `show()` looks for a *module-level function* called `show` and raises `NameError`. Methods are not automatically in scope inside other methods — you always reach them through `self`.

| You write | Python looks for |
|---|---|
| `self.show()` | a method `show` on this object's class ✔ |
| `show()` | a plain function `show` at module level ✘ `NameError` |

---

## Part 4 — `self` Is a Convention, Not a Keyword

Nothing in the language enforces the name. The rule is purely positional: **the first parameter receives the object**, whatever you call it.

```python
class Dog:
    def bark(this):                  # works fine
        print(f"{this.name} says Woof!")

class Dog2:
    def bark(banana):                # also works. please never do this
        print(f"{banana.name} says Woof!")
```

Both run. But every Python codebase, tutorial, error message, and colleague on Earth says `self` — so deviating buys nothing and costs readability. Note how even Python's own error messages assume it:

```text
TypeError: Dog.bark() takes 0 positional arguments but 1 was given
```

Use `self`. The reason it's worth *knowing* it's a convention is that it explains why forgetting it produces an arity error rather than a "missing self" error — Python never knew you meant `self` in the first place.

---

## Part 5 — Two Objects of the Same Class, One Method

Here's where `self` stops being obvious. A method can take **another object of its own class** as a normal parameter:

```python
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount

    def transfer(self, other, amount):
        if self.withdraw(amount) == "Insufficient funds":
            return "Insufficient funds"
        other.deposit(amount)          # `other` is a whole separate Account

    def show(self):
        print(f"{self.owner}: {self.balance}")
```

```python
alice = Account("Alice", 100)
bob   = Account("Bob", 50)

alice.transfer(bob, 30)
alice.show()      # Alice: 70
bob.show()        # Bob: 80
```

Inside that one `transfer` call:

| Name | Refers to | How it got there |
|---|---|---|
| `self` | the `alice` object | supplied by the dot in `alice.transfer(...)` |
| `other` | the `bob` object | passed explicitly as an argument |

Both are `Account` objects. Both have `.balance`. The *only* difference is how they arrived. `self` isn't special because of what it holds — it's special because of **where it comes from**.

This is also why `transfer` can call `self.withdraw(amount)` and `other.deposit(amount)` in the same breath: two objects, same class, same methods available on each.

---

## Part 6 — When There Is No `self`

Every method so far has taken `self`, because every method so far needed *one specific object's* data. But some methods genuinely don't:

```python
class Dog:
    def is_valid_age(age):     # doesn't need any dog at all -- just checks a number
        return 0 <= age <= 30
```

Written like that it's broken as an instance method, for exactly the Lesson 01 Part 3.4 reason: calling `some_dog.is_valid_age(5)` passes the dog in as `age`. Python offers proper tools for methods that need no instance (`@staticmethod`) or that need the class rather than an instance (`@classmethod`).

**That's Lesson 05.** For now, the takeaway: `self` is required for every method that touches one object's data, which is the vast majority — and there's a documented mechanism for the exceptions.

---

## Part 7 — Predict, Then Run

1. ```python
   class Counter:
       def __init__(self): self.n = 0
       def bump(self): n = self.n + 1
   c = Counter(); c.bump(); c.bump()
   print(c.n)
   ```

2. ```python
   class Dog:
       def __init__(self, name): self.name = name
       def rename(self, new): self.name = new
       def shout(self): print(self.name.upper())
   a = Dog("Rex"); b = a
   b.rename("Fido")
   a.shout()
   ```

3. ```python
   class Dog:
       def __init__(self, name): self.name = name
       def bark(self): print(f"{self.name}!")
   rex = Dog("Rex")
   Dog.bark("not a dog")
   ```

4. ```python
   class Greeter:
       def hello(self): print("hi")
       def twice(self): hello(); hello()
   Greeter().twice()
   ```

<details>
<summary>Answers (predict first)</summary>

1. `0`. Part 2.4's silent bug: `n = self.n + 1` computes `1` into a local and throws it away. Needed `self.n = self.n + 1`.
2. `FIDO`. `b = a` copied the reference, not the object (Lesson 01 Part 6.1) — `a` and `b` are one dog, so renaming via `b` is visible via `a`.
3. `AttributeError: 'str' object has no attribute 'name'`. `Dog.bark` is a plain function (Part 1.2), so it accepts *anything* as `self` — Python never type-checks it. The call itself succeeds; it only fails when the body reaches for `self.name` and the string hasn't got one.
4. `NameError: name 'hello' is not defined. Did you mean: 'self.hello'?` — Part 3. Methods aren't in scope inside other methods, and Python's suggestion is exactly the fix.

</details>

---

## Part 8 — Cheat Sheet Summary

```python
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner                    # write via self.
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount  # read AND write via self.
        self.show()                           # call sibling method via self.

    def transfer(self, other, amount):        # `other` = another Account
        self.withdraw(amount)
        other.deposit(amount)

    def show(self):
        print(f"{self.owner}: {self.balance}")
```

| Idea | One-line version |
|---|---|
| What `self` is | The object the method was called on |
| Who supplies it | The dot: `rex.bark()` → `Dog.bark(rex)` |
| `Dog.bark` vs `rex.bark` | plain function vs **bound method** (function + its object) |
| Read an attribute | `self.balance` |
| Write an attribute | `self.balance = ...` — **left side must have `self.`** |
| Bare name on the left | Creates a throwaway local; object unchanged, **no error** |
| Bare name on both sides | `UnboundLocalError` |
| Call a sibling method | `self.show()`, never `show()` |
| Is `self` a keyword? | No — convention only. First parameter wins regardless of name |
| Another object of the same class | Just a normal parameter; `self` is only special in *how it arrives* |
| Methods needing no object | `@staticmethod` / `@classmethod` — Lesson 05 |

---

## Self-Check

- [ ] What's the difference between `Dog.bark` and `rex.bark`?
- [ ] Why does `f = rex.bark; f()` print the right dog's name with no arguments?
- [ ] Give the two bugs from omitting `self.`, and which one is more dangerous.
- [ ] Why is `show()` inside a method a `NameError` when `self.show()` works?
- [ ] In `transfer(self, other, amount)`, what actually distinguishes `self` from `other`?
- [ ] Is `self` a reserved word in Python?

---

## 📚 Resources

- **W3Schools:** [Python Classes — The self Parameter](https://www.w3schools.com/python/python_classes.asp)
- **YouTube:** [mCoding — What is `self`, really?](https://www.youtube.com/watch?v=mfM-3PQ2mMc) — pairs directly with Part 1.2
- **YouTube:** [Corey Schafer — Python OOP Tutorial 1: Classes and Instances](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)
- **Real Python:** [Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)

---

## 🧠 Try It Yourself

Open `exercises.py` in this folder:

1. Implement `deposit`, `withdraw`, and `print_balance` on `BankAccount`, using `self` to read and write `self.balance` (Part 2).
2. Deliberately write `balance = self.balance + amount` in `deposit`, run it, and confirm the balance doesn't change. Then fix it and note in a comment why nothing errored (Part 2.4).
3. Make `deposit` call `self.print_balance()` at the end. Then try it as bare `print_balance()` and read the `NameError` (Part 3).
4. Implement `transfer(self, other_account, amount)` that withdraws from `self` and deposits into `other_account` — note that both are `BankAccount` objects in the same method (Part 5).
5. Print `BankAccount.deposit` and `acc1.deposit` without calling them, and compare the two lines of output (Part 1.2).
