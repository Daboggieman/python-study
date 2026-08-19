# Lecture 16: Modules, Imports, and Error Handling

Python becomes much more powerful when you reuse code from modules and handle problems gracefully.

---

## 1. Importing Modules
A module is a file containing Python code.

```python
import math

print(math.sqrt(16))
```

You can also import specific functions:

```python
from math import pi

print(pi)
```

---

## 2. Useful Standard Library Modules

```python
import random
import statistics

print(random.randint(1, 10))
print(statistics.mean([1, 2, 3, 4]))
```

---

## 3. Handling Errors with `try` and `except`

```python
try:
    number = int("abc")
except ValueError:
    print("That was not a valid integer.")
```

This lets your program recover from mistakes instead of crashing.

---

## 4. Debugging Basics
A few useful debugging habits:
- Read the error message carefully.
- Print values before and after key steps.
- Check whether input was converted correctly.
- Test small pieces of code separately.

---

## 🧠 Try It Yourself
1. Import `math` and calculate the square root of 81.
2. Write a `try/except` block that handles invalid input.
3. Use `print()` to debug a small calculation.
