# Python OOP Practice — Beginner to Intermediate

A progression of 14 exercises. Do them roughly in order — each tier assumes you're comfortable with the previous one. For every exercise: write it with plain classes first, get it working, *then* go back and apply the "refactor notes" at the end of each exercise. That second pass is where OOP actually clicks.

---

## Tier 1 — Beginner (classes, methods, basic inheritance)

### 1. Bank Account

Build a `BankAccount` class that tracks a balance and a history of transactions.

**Requirements**
- `__init__(self, owner, balance=0)`
- `deposit(amount)` — rejects amounts ≤ 0
- `withdraw(amount)` — raises `ValueError` on insufficient funds or amount ≤ 0
- `get_balance()`
- `get_history()` — returns a list of strings like `"Deposited 50"`, `"Withdrew 20"`

**Starter skeleton**
```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self._history = []

    def deposit(self, amount):
        pass  # TODO

    def withdraw(self, amount):
        pass  # TODO
```

**Expected behavior**
```python
acc = BankAccount("Raph'el", 100)
acc.deposit(50)
acc.withdraw(30)
print(acc.get_balance())     # 120
print(acc.get_history())     # ["Deposited 50", "Withdrew 30"]
acc.withdraw(1000)           # raises ValueError
```

**Edge cases to handle:** negative deposit, negative withdrawal, withdrawal exceeding balance, depositing/withdrawing 0.

**Refactor note:** once it works, make `balance` "private" (`_balance`) and expose it through a `balance` property (see Tier 2, Exercise 8) so it can't be set directly from outside.

---

### 2. Shape: Rectangle → Square

**Requirements**
- `Rectangle` class with `width`, `height`, `area()`, `perimeter()`
- `Square(Rectangle)` subclass — constructor only takes `side`, calls `super().__init__(side, side)`

**Starter skeleton**
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        pass

    def perimeter(self):
        pass


class Square(Rectangle):
    def __init__(self, side):
        pass  # call super().__init__ correctly
```

**Expected behavior**
```python
r = Rectangle(4, 5)
print(r.area(), r.perimeter())   # 20 30

s = Square(4)
print(s.area(), s.perimeter())   # 16 16
print(isinstance(s, Rectangle))  # True
```

**Stretch:** add a `describe()` method on `Rectangle` that returns `"Rectangle 4x5, area=20"` — don't override it in `Square`, and notice it still works correctly because it reads `self.width`/`self.height`.

---

### 3. Library Book Tracker

**Requirements**
- `Book` class: `title`, `author`, `isbn`, `is_checked_out` (default `False`)
- `Library` class: holds a list of `Book` objects
  - `add_book(book)`
  - `checkout(isbn)` — marks checked out, raises `ValueError` if already out or not found
  - `return_book(isbn)`
  - `list_available()` — returns titles of books not checked out

**Expected behavior**
```python
lib = Library()
lib.add_book(Book("Dune", "Frank Herbert", "111"))
lib.add_book(Book("1984", "George Orwell", "222"))

lib.checkout("111")
print(lib.list_available())    # ["1984"]
lib.checkout("111")            # raises ValueError — already checked out
lib.return_book("111")
print(lib.list_available())    # ["Dune", "1984"]
```

**Edge cases:** checkout/return an ISBN that doesn't exist.

---

### 4. Employee Payroll

**Requirements**
- `Employee` base class: `name`, `calculate_pay()` — raise `NotImplementedError` in the base
- `HourlyEmployee(Employee)`: `hours_worked`, `hourly_rate` → pay = hours × rate (1.5× rate for hours over 40)
- `SalariedEmployee(Employee)`: `annual_salary` → pay = salary / 12 (monthly)

**Expected behavior**
```python
h = HourlyEmployee("Ada", hours_worked=45, hourly_rate=20)
print(h.calculate_pay())   # 40*20 + 5*30 = 950

s = SalariedEmployee("Grace", annual_salary=120000)
print(s.calculate_pay())   # 10000.0

employees = [h, s]
for e in employees:
    print(e.name, e.calculate_pay())   # polymorphism — same call, different behavior
```

---

## Tier 2 — Intermediate: inheritance, polymorphism, encapsulation

### 5. Shape Hierarchy with Abstract Base Class

**Requirements**
- Use `abc.ABC` and `@abstractmethod` to define `Shape` with `area()` and `perimeter()` — it should be **impossible** to instantiate `Shape` directly.
- Implement `Circle`, `Triangle` (by three sides, use Heron's formula), `Rectangle`.
- Write `total_area(shapes: list) -> float` that sums `.area()` over a mixed list.

**Starter skeleton**
```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self): ...

    @abstractmethod
    def perimeter(self): ...


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    # TODO


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    # TODO: Heron's formula for area
```

**Expected behavior**
```python
Shape()   # TypeError: Can't instantiate abstract class

shapes = [Circle(3), Triangle(3, 4, 5), Rectangle(4, 5)]
print(round(total_area(shapes), 2))   # ~ 68.27
```

**Edge case:** Triangle with sides that don't form a valid triangle — raise `ValueError` in `__init__`.

---

### 6. Vehicle Rental System

**Requirements**
- `Vehicle` base: `make`, `model`, `daily_rate`, `calculate_cost(days)`
- `Car(Vehicle)`, `Motorcycle(Vehicle)`, `Truck(Vehicle)` — `Truck` adds a flat $50/day surcharge; others just use `daily_rate * days`
- `Customer` class: `name`, `rental_history` (list)
- `Rental` class: composes a `Vehicle` + `Customer` + `days`; `total_cost()` delegates to the vehicle

**Expected behavior**
```python
truck = Truck("Ford", "F150", daily_rate=80)
cust = Customer("Raph'el")
rental = Rental(truck, cust, days=3)
print(rental.total_cost())   # 80*3 + 50*3 = 390
```

**This is the key exercise for practicing composition:** `Rental` doesn't inherit from `Vehicle` or `Customer` — it *has* them.

---

### 7. Zoo Simulation

**Requirements**
- `Animal` base: `name`, `make_sound()` (raise `NotImplementedError`)
- `Dog`, `Cat`, `Snake` subclasses each override `make_sound()`
- `Zoo` class: list of animals, `make_all_sounds()` iterates and calls each `make_sound()`

**Expected behavior**
```python
zoo = Zoo([Dog("Rex"), Cat("Milo"), Snake("Kaa")])
zoo.make_all_sounds()
# Rex says Woof!
# Milo says Meow!
# Kaa says Hiss!
```

Simple, but it's the cleanest possible demo of polymorphism — the loop never checks `type()`, it just calls `.make_sound()`.

---

### 8. Temperature Converter with `@property`

**Requirements**
- `Temperature` stores Celsius internally as `_celsius`
- `celsius` is a property (get/set)
- `fahrenheit` is a property: getter converts C→F, **setter** converts the incoming F value back to C and stores it
- Setting either one should update the other consistently

**Starter skeleton**
```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        pass  # TODO: maybe validate value > -273.15

    @property
    def fahrenheit(self):
        pass  # TODO

    @fahrenheit.setter
    def fahrenheit(self, value):
        pass  # TODO: convert F to C, store in self._celsius
```

**Expected behavior**
```python
t = Temperature(25)
print(t.fahrenheit)     # 77.0
t.fahrenheit = 98.6
print(round(t.celsius, 1))   # 37.0
t.celsius = -300         # should raise ValueError (below absolute zero)
```

---

### 9. Inventory Item with Validation

**Requirements**
- `InventoryItem`: `name`, `_price`, `_quantity` — both exposed via properties
- Setters reject negative values (`raise ValueError`)
- `total_value()` = price × quantity
- `restock(amount)` and `sell(amount)` — `sell` raises if amount > current quantity

**Expected behavior**
```python
item = InventoryItem("Widget", price=9.99, quantity=10)
item.sell(3)
print(item.quantity)        # 7
item.price = -5             # raises ValueError
item.sell(100)               # raises ValueError — not enough stock
```

---

## Tier 3 — Intermediate: dunder methods, operator overloading, design patterns

### 10. Vector2D

**Requirements** — implement so instances behave like numbers:
- `__add__`, `__sub__`, `__mul__` (scalar multiply)
- `__eq__`
- `__repr__` → `"Vector2D(3, 4)"`
- `__lt__` (compare by magnitude, i.e. `sqrt(x**2 + y**2)`)
- Bonus: `__abs__` returns magnitude

**Expected behavior**
```python
v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)
print(v1 + v2)          # Vector2D(4, 6)
print(v2 - v1)          # Vector2D(2, 2)
print(v1 * 3)           # Vector2D(3, 6)
print(v1 == Vector2D(1, 2))   # True
print(sorted([v2, v1])) # sorted by magnitude — v1 first
```

---

### 11. Custom Stack with Dunder Methods

**Requirements** — implement `Stack` so it works with native Python syntax:
- `push(item)`, `pop()`, `peek()`
- `__len__` → so `len(stack)` works
- `__contains__` → so `"x" in stack` works
- `__iter__` → so `for item in stack:` works (iterate top to bottom)
- `__repr__`

**Expected behavior**
```python
s = Stack()
s.push(1); s.push(2); s.push(3)
print(len(s))         # 3
print(2 in s)          # True
for x in s:
    print(x)            # 3, 2, 1
print(s.pop())          # 3
```

---

### 12. Restaurant Order System (composition-focused)

**Requirements**
- `MenuItem`: `name`, `price`
- `Order`: composes a list of `MenuItem`s, `add_item()`, `remove_item()`, `subtotal()`
- `Receipt`: takes an `Order`, applies a tax rate, produces a formatted string via `__str__`

**Expected behavior**
```python
order = Order()
order.add_item(MenuItem("Jollof Rice", 8.50))
order.add_item(MenuItem("Suya", 5.00))
receipt = Receipt(order, tax_rate=0.075)
print(receipt)
# Jollof Rice        $8.50
# Suya                $5.00
# Subtotal:          $13.50
# Tax:                $1.01
# Total:              $14.51
```

**Why this one matters:** it's tempting to make `Receipt` inherit from `Order` — resist it. A receipt *has* an order, it isn't a kind of order. Composition over inheritance.

---

### 13. Observer Pattern — Notification System

**Requirements**
- `Subscriber` (interface-ish): `update(message)`
- `EmailSubscriber`, `SMSSubscriber` implement `update()` differently (just print differently)
- `Publisher`: `subscribe(sub)`, `unsubscribe(sub)`, `notify_all(message)` — calls `update()` on every subscriber

**Expected behavior**
```python
pub = Publisher()
pub.subscribe(EmailSubscriber("raphel@example.com"))
pub.subscribe(SMSSubscriber("+234..."))
pub.notify_all("Server is down!")
# [EMAIL to raphel@example.com]: Server is down!
# [SMS to +234...]: Server is down!
```

This is a real design pattern (Observer) — the same shape shows up in GUI event handling, pub/sub systems, and reactive programming.

---

### 14. State Machine — Order Status

**Requirements**
- Each state (`Pending`, `Shipped`, `Delivered`, `Cancelled`) is its own class implementing a common interface (e.g. `next(order)`, `cancel(order)`)
- `Order` holds a reference to its current state object and delegates transitions to it
- Invalid transitions (e.g. `Delivered` → `Shipped`) should raise an error or simply be no-ops — your call, but be consistent

**Expected behavior**
```python
order = Order()
print(order.status)     # "Pending"
order.next()             # Pending -> Shipped
order.next()             # Shipped -> Delivered
print(order.status)      # "Delivered"
order.cancel()            # should fail/no-op — can't cancel a delivered order
```

This one's harder to get "clean" — the point is that `Order` never has a big `if/elif` chain checking its own status. All the transition logic lives inside the state classes.

---

## Suggested order of attack

1. Do 1–4 without looking at the starter skeletons if you can.
2. For 5–9, read the starter code, then implement — these introduce `abc`, `@property`, and composition, which are the concepts most devs get rusty on.
3. For 10–14, don't peek at the expected output until you've got something running — dunder methods and design patterns are best learned by getting the `TypeError`s and fixing them.

If you want, once you've done a few, send me your code for one and I'll review it like a PR — that's usually where the real learning happens.
