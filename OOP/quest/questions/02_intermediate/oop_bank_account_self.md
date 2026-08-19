# OOP Bank Account Self

Source: oop_bank_account_self

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Define a `BankAccount` class with `__init__(self, owner, balance=0)`, `deposit(self, amount)`, and `withdraw(self, amount)` (withdraw should not go below 0 -- if there are insufficient funds, do not change the balance and instead return the string `"Insufficient funds"`; a successful withdraw or deposit should return the new balance).

Expected function
```python
class BankAccount:
    def __init__(self, owner, balance=0):
        pass

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass
```


Here is a possible program to test your function :
```python
acc = BankAccount("Alice", 100)
print(acc.deposit(50))
print(acc.withdraw(200))
print(acc.withdraw(30))
```

And its output :
```text
150
Insufficient funds
120
```
