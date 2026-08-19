# Lecture 12: Standard Library

Python's standard library is extensive and offers a wide range of modules that provide solutions to many common programming tasks. It is referred to as "batteries included".

---

## 1. What is the Standard Library?
A collection of pre-written modules that are distributed with Python. You do not need to install them using `pip`. Simply use the `import` statement.

---

## 2. Commonly Used Modules

### `math`
Provides mathematical functions:
```python
import math

print(math.sqrt(16))  # 4.0 (square root)
print(math.pow(2, 3)) # 8.0 (exponentiation)
print(math.pi)        # 3.141592653589793
```

### `random`
Provides functions for generating random numbers and selecting random elements:
```python
import random

print(random.randint(1, 10))    # Random integer between 1 and 10 (inclusive)
print(random.random())           # Random float between 0.0 and 1.0
print(random.choice(['a', 'b'])) # Random item from list
```

### `datetime`
Provides classes for manipulating dates and times:
```python
import datetime

now = datetime.datetime.now()
print(now)              # Current date and time
print(now.year)         # Current year
today = datetime.date.today()
print(today)            # YYYY-MM-DD
```

### `os` and `sys`
Provide operating system and system-specific configurations:
```python
import os
import sys

print(os.getcwd())       # Get current working directory
print(sys.argv)          # Command line arguments passed to the script
print(sys.version)       # Python version information
```

### `collections`
Provides specialized container datatypes:
```python
from collections import Counter

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counts = Counter(words)
print(counts)  # Counter({'apple': 3, 'banana': 2, 'orange': 1})
```

---

## 🧠 Try It Yourself
1. Use the `random` module to simulate a rolling die: generate random numbers from 1 to 6.
2. Use the `datetime` module to calculate the number of days between today and your next birthday.
