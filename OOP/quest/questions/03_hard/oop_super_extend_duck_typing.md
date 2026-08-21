# OOP — Super, Extend, and Duck Typing

**Tier:** 03_hard
**Write your answer in:** `OOP/quest/answers/oop_super_extend_duck_typing.py`
**Allowed:** builtins only — no imports needed.

---

## Goal

Build a small payroll model that shows the **two different ways** Python lets unrelated
objects respond to the same method call:

| Route | How it works | Which classes here |
|---|---|---|
| **Inheritance polymorphism** | A subclass overrides a parent's method | `Employee` → `Manager` |
| **Duck typing** | An unrelated class just *has* the same method name | `Contractor` |

The payoff: one loop calls `p.pay_summary()` on all three, and each responds correctly —
even though `Contractor` shares no parent with the other two.

**Concepts used:** inheritance, method overriding, `super()`, duck typing
— see [`curriculum/06_polymorphism/lecture.md`](../../../curriculum/06_polymorphism/lecture.md).

---

## Build It In Steps

Do these in order and run after each one. Don't write all three classes at once.

### Step 1 — `Employee` (the base class)

```python
class Employee:
    def __init__(self, name, base_salary): ...
    def pay_summary(self): ...
```

- `__init__` stores `name` and `base_salary` on `self`.
- `pay_summary()` **returns** (does not print) the string:
  `"Sam: base $50000"` for `Employee("Sam", 50000)`

  Format: `f"{self.name}: base ${self.base_salary}"`

**Checkpoint:** `print(Employee("Sam", 50000).pay_summary())` → `Sam: base $50000`

### Step 2 — `Manager` (subclass, uses `super()` twice)

```python
class Manager(Employee):
    def __init__(self, name, base_salary, bonus): ...
    def pay_summary(self): ...
```

This is the heart of the exercise — `super()` is used in **two separate places**:

1. In `__init__`, call `super().__init__(name, base_salary)` to let the parent store
   `name` and `base_salary`, then store `bonus` yourself. Don't re-assign
   `self.name` by hand — the whole point of `super()` is to not repeat the parent's work.
2. In `pay_summary`, call `super().pay_summary()` to get the parent's string,
   then **append** to it:

   `f" + bonus ${self.bonus}"`

**Checkpoint:** `print(Manager("Ada", 70000, 5000).pay_summary())`
→ `Ada: base $70000 + bonus $5000`

Notice you never rewrote `"...: base $..."` in `Manager` — you reused it. That reuse
is what `super()` buys you: change the format once in `Employee` and `Manager` follows.

### Step 3 — `Contractor` (no parent at all)

```python
class Contractor:            # <-- note: does NOT inherit from Employee
    def __init__(self, name, hourly_rate): ...
    def pay_summary(self): ...
```

- `__init__` stores `name` and `hourly_rate`.
- `pay_summary()` returns:
  `f"{self.name}: contractor at ${self.hourly_rate}/hr"`

`Contractor` has **no relationship** to `Employee` — no shared parent, no inheritance.
The only thing it shares is a method *name*. That is enough for the loop below to work,
and that is duck typing: *"if it has a `pay_summary()`, I can call `pay_summary()` on it."*

---

## Test Program

```python
people = [
    Employee("Sam", 50000),
    Manager("Ada", 70000, 5000),
    Contractor("Lee", 80),
]
for p in people:
    print(p.pay_summary())
```

## Expected Output

```text
Sam: base $50000
Ada: base $70000 + bonus $5000
Lee: contractor at $80/hr
```

---

## Hints

<details>
<summary>Hint 1 — `super()` in <code>__init__</code></summary>

```python
class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)   # parent sets self.name, self.base_salary
        self.bonus = bonus                    # then add what's new to Manager
```
Note there's no `self` inside the `super().__init__(...)` call — `super()` already
knows which object it's working on.
</details>

<details>
<summary>Hint 2 — `super()` in an overriding method</summary>

`super().pay_summary()` runs `Employee`'s version and hands you back its **return value**.
Capture it, then build on it:

```python
def pay_summary(self):
    base = super().pay_summary()      # "Ada: base $70000"
    return base + f" + bonus ${self.bonus}"
```
</details>

<details>
<summary>Hint 3 — why the loop works at all</summary>

Python does not check types before calling `p.pay_summary()`. At each iteration it looks
up `pay_summary` on whatever object `p` currently is, and calls what it finds. Three
different classes, three different method bodies, one call site.
</details>

---

## Common Mistakes

- **Printing instead of returning.** Every `pay_summary` must `return` a string. If it
  prints, the test loop's `print()` will show `None` on each line.
- **Making `Contractor` inherit from `Employee`.** That defeats the entire point — the
  exercise exists to show a class with *no* shared parent still works.
- **Re-writing the base string inside `Manager.pay_summary`.** If your `Manager` contains
  the literal text `": base $"`, you skipped `super()`. Build on the parent's return value.
- **Calling `super().__init__(self, name, base_salary)`.** Passing `self` explicitly to
  `super()` is a `TypeError` — `super()` supplies it for you.
- **Forgetting `Employee` in the parentheses:** `class Manager(Employee):`, not
  `class Manager:`. Without it `super()` has no parent to reach and `Manager` has no
  inherited `pay_summary`.

---

## Stretch Goal (optional)

Add a fourth class `Intern` that duck-types `pay_summary()` returning
`"<name>: unpaid intern"`, append one to the `people` list, and confirm the loop needs
**no changes at all** to handle it. That "no changes at all" is the practical value of
polymorphism: new types plug into existing loops.
