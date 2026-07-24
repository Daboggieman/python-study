# Exception Custom Error

Source: exception_custom_error

Files to submit
- solution.py

Allowed functions
- --allow-builtin

Instructions
Define a custom exception class `InsufficientFundsError(Exception)` that stores `balance` and `amount` attributes and produces the message `f"Cannot withdraw {amount}, balance is only {balance}"`. Write a `withdraw(balance, amount)` function that raises this exception when `amount > balance`, otherwise returns `balance - amount`.

Expected function
```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        pass

def withdraw(balance, amount):
    pass
```


Here is a possible program to test your function :
```python
print(withdraw(100, 30))
try:
    withdraw(100, 500)
except InsufficientFundsError as e:
    print(e)
    print(e.amount - e.balance)
```

And its output :
```text
70
Cannot withdraw 500, balance is only 100
400
```
