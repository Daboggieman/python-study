# 22: Exception Handling, Advanced

Lesson 16 covered basic `try`/`except`. This lesson goes deeper: the full `try`/`except`/`else`/`finally` structure, the exception class hierarchy, catching multiple specific exception types, and defining your own custom exceptions.

---

## 1. The Full Structure: `try` / `except` / `else` / `finally`

```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    else:
        print("Division succeeded")   # runs ONLY if no exception was raised
        return result
    finally:
        print("This always runs")       # runs no matter what -- exception or not

print(divide(10, 2))
print(divide(10, 0))
```
```text
Division succeeded
This always runs
5.0
Cannot divide by zero!
This always runs
None
```

- **`else`** runs only when the `try` block completes with no exception — good for code that should only happen "on success."
- **`finally`** always runs, exception or not — the standard place for cleanup (closing files, releasing locks, disconnecting from a database).

---

## 2. Catching Multiple Exception Types

```python
def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        print(f"'{value}' isn't a valid number")
    except TypeError:
        print(f"Can't convert type {type(value)} to int")

safe_convert("abc")     # 'abc' isn't a valid number
safe_convert(None)        # Can't convert type <class 'NoneType'> to int

# Or catch several types in one clause:
def safe_convert_v2(value):
    try:
        return int(value)
    except (ValueError, TypeError) as e:
        print(f"Conversion failed: {e}")
```

**Important: order matters.** Python checks `except` clauses top to bottom and uses the first match — always put more *specific* exception types before more *general* ones.

```python
try:
    risky_operation()
except Exception:          # too broad, placed first -- would swallow EVERYTHING below it!
    print("Something went wrong")
except ValueError:           # this would NEVER be reached if placed after Exception
    print("Bad value")
```

---

## 3. The Exception Hierarchy

Nearly all built-in exceptions inherit from `BaseException`, with `Exception` as the ancestor of almost everything you'll actually want to catch:

```
BaseException
 ├── SystemExit, KeyboardInterrupt   (rarely caught on purpose)
 └── Exception
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── ValueError
      ├── TypeError
      ├── FileNotFoundError (an OSError subclass)
      └── ... many more
```

Catching `Exception` catches almost anything that could reasonably go wrong in normal code; catching bare `except:` (no type at all) also catches `SystemExit`/`KeyboardInterrupt`, which is almost always a mistake — it can make `Ctrl+C` stop working to interrupt a runaway program.

---

## 4. Raising Your Own Exceptions

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError(f"Cannot withdraw {amount}, balance is only {balance}")
    return balance - amount

try:
    withdraw(100, 500)
except ValueError as e:
    print(e)   # Cannot withdraw 500, balance is only 100
```

---

## 5. Custom Exception Classes

For larger programs, defining your own exception types makes error handling much more precise and self-documenting:

```python
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}, balance is only {balance}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(100, 500)
except InsufficientFundsError as e:
    print(f"Error: {e}")
    print(f"Shortfall: {e.amount - e.balance}")
```

Custom exceptions let calling code catch *your* specific error type separately from generic `ValueError`s elsewhere in a large program.

---

## 6. Re-raising and Chaining Exceptions

```python
def process_data(data):
    try:
        return int(data)
    except ValueError as e:
        raise RuntimeError("Failed to process data") from e   # preserves the original cause in the traceback
```

`raise ... from e` keeps a clear "this error was caused by that earlier error" chain, which is invaluable for debugging.

---

## 📚 Resources

- **W3Schools:** [Python Try Except](https://www.w3schools.com/python/python_try_except.asp)
- **Docs:** [Python Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- **YouTube:** [Corey Schafer — Python Exception Handling](https://www.youtube.com/watch?v=NIWwJbo-9_8)
- **Real Python:** [Python Exceptions: An Introduction](https://realpython.com/python-exceptions/)

---

## 🧠 Try It Yourself

1. Write `divide(a, b)` using the full `try`/`except`/`else`/`finally` structure and confirm each block's behavior with both a successful and a failing call.
2. Write a function that catches `ValueError` and `TypeError` separately with different messages, then again using a single tuple-based `except`.
3. Define a custom `InsufficientFundsError` exception carrying `balance` and `amount` attributes, and use it in a `withdraw()` function.
4. Use `raise ... from e` to wrap a `ValueError` in a more general `RuntimeError` while preserving the original exception chain, and print the full traceback to see the chain.
