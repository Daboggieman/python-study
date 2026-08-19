# OOP 03: The `self` Parameter

Every method you've written so far starts with a mysterious `self` parameter. This lesson demystifies it completely: `self` is simply **a reference to the specific object the method is being called on**.

---

## 1. `self` Is Just "This Particular Object"

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

rex = Dog("Rex")
fido = Dog("Fido")

rex.bark()    # Rex says Woof!
fido.bark()   # Fido says Woof!
```

Both `rex` and `fido` share the exact same `bark` method (defined once, on the class) — but each call needs to know *which* dog's name to print. That's exactly what `self` provides: when you call `rex.bark()`, Python automatically passes `rex` in as `self`.

---

## 2. What Python Actually Does Behind the Scenes

```python
rex.bark()
# is exactly equivalent to:
Dog.bark(rex)
```

Try it yourself — both lines print the same thing. Calling a method on an object (`rex.bark()`) is just convenient shorthand for calling the class's function and passing the object explicitly as the first argument (`Dog.bark(rex)`).

---

## 3. `self` Is a Naming Convention, Not a Keyword

Nothing in Python *forces* you to call it `self` — it's the first parameter of an instance method, period. But every Python programmer on Earth calls it `self` by convention, and deviating will confuse anyone reading your code (including future you).

```python
class Dog:
    def bark(this):        # works, but PLEASE don't do this
        print(f"{this.name} says Woof!")
```

---

## 4. Using `self` to Read AND Write Attributes

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount    # read self.balance, then write it

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount
```

Every method that needs to look at or change data belonging to *this particular object* does it through `self`.

---

## 5. `self` Also Lets Objects Call Their Own Other Methods

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        self.print_balance()     # calling another method on the same object

    def print_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")
```

---

## 📚 Resources

- **W3Schools:** [Python Classes — The self Parameter](https://www.w3schools.com/python/python_classes.asp)
- **YouTube:** [Corey Schafer — Python OOP Tutorial 1: Classes and Instances](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)
- **YouTube:** [mCoding — What is `self`, really?](https://www.youtube.com/watch?v=mfM-3PQ2mMc)
- **Real Python:** [Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)

---

## 🧠 Try It Yourself

1. Create two `Dog` objects and call `bark()` on each via both `rex.bark()` and `Dog.bark(rex)` syntax — confirm they behave identically.
2. Implement `BankAccount` with `deposit`, `withdraw`, and `print_balance` methods, using `self` to read and write `self.balance` throughout.
3. Deliberately rename `self` to `this` in one class and confirm the code still runs — then rename it back and explain in a comment why the convention matters anyway.
4. Add a method `transfer(self, other_account, amount)` to `BankAccount` that withdraws from `self` and deposits into `other_account` — notice how `self` refers to one object while `other_account` refers to another, in the same method.
