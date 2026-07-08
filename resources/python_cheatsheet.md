# 🐍 Python Cheatsheet

A comprehensive quick-reference for Python 3.12+.

---

## Data Types

```python
# Numbers
x = 10          # int
y = 3.14        # float
z = 2 + 3j      # complex

# Strings
s = "hello"
s = 'hello'
s = """multi
line"""

# Boolean
flag = True      # or False

# None
x = None

# Check type
type(x)          # <class 'int'>
isinstance(x, int)  # True
```

## Variables & Assignment

```python
x = 5
x, y = 5, 10           # Multiple assignment
x, y = y, x            # Swap
x += 1                  # Augmented assignment (also -=, *=, /=, //=, %=, **=)

# Constants (convention only — Python has no true constants)
MAX_SIZE = 100
```

## Strings

```python
# Creation
s = "Hello, World!"

# f-strings (formatted strings)
name = "Alice"
greeting = f"Hello, {name}!"
calc = f"2 + 2 = {2 + 2}"

# Common methods
s.upper()           # "HELLO, WORLD!"
s.lower()           # "hello, world!"
s.strip()           # Remove whitespace from both ends
s.lstrip()          # Remove from left
s.rstrip()          # Remove from right
s.split(",")        # ["Hello", " World!"]
s.replace("H", "J") # "Jello, World!"
s.startswith("He")  # True
s.endswith("!")     # True
s.find("World")     # 7 (index, or -1)
s.count("l")        # 3
s.isdigit()         # False
s.isalpha()         # False (has punctuation)
s.join(["a","b"])   # "aHello, World!b" — usually use "".join()
",".join(["a","b"]) # "a,b"

# Slicing
s[0]       # "H"
s[-1]      # "!"
s[0:5]     # "Hello"
s[::2]     # "Hlo ol!"
s[::-1]    # "!dlroW ,olleH" (reverse)
len(s)     # 13
```

## Lists

```python
# Creation
nums = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]
empty = []

# Access
nums[0]     # 1
nums[-1]    # 5
nums[1:3]   # [2, 3]

# Modify
nums.append(6)          # [1, 2, 3, 4, 5, 6]
nums.insert(0, 0)       # [0, 1, 2, 3, 4, 5, 6]
nums.extend([7, 8])     # [0, 1, 2, 3, 4, 5, 6, 7, 8]
nums.remove(0)          # Remove first occurrence of 0
nums.pop()              # Remove and return last item
nums.pop(0)             # Remove and return item at index 0
del nums[0]             # Delete item at index 0

# Search
3 in nums               # True
nums.index(3)           # Index of first 3
nums.count(3)           # How many 3s

# Sort
nums.sort()             # Sort in place (ascending)
nums.sort(reverse=True) # Sort descending
sorted(nums)            # Return new sorted list (original unchanged)
nums.reverse()          # Reverse in place

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# Useful functions
len(nums)
min(nums)
max(nums)
sum(nums)
```

## Tuples

```python
# Immutable sequences
point = (3, 4)
single = (42,)      # Single-element tuple needs trailing comma
x, y = point        # Unpacking

# Named tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)
```

## Dictionaries

```python
# Creation
person = {"name": "Alice", "age": 30}
empty = {}
from_keys = dict.fromkeys(["a", "b"], 0)  # {"a": 0, "b": 0}

# Access
person["name"]              # "Alice" (KeyError if missing)
person.get("name")          # "Alice" (None if missing)
person.get("job", "N/A")    # "N/A" (default if missing)

# Modify
person["job"] = "Developer"  # Add or update
person.update({"age": 31})   # Update multiple
del person["job"]            # Delete key
person.pop("age")            # Remove and return value

# Iteration
person.keys()       # dict_keys(["name", "age"])
person.values()     # dict_values(["Alice", 30])
person.items()      # dict_items([("name", "Alice"), ("age", 30)])

for key, value in person.items():
    print(f"{key}: {value}")

# Comprehension
squares = {x: x**2 for x in range(5)}
```

## Sets

```python
# Creation
s = {1, 2, 3}
empty = set()       # NOT {} — that's an empty dict!

# Operations
s.add(4)
s.remove(4)         # KeyError if missing
s.discard(4)        # No error if missing

# Set operations
a = {1, 2, 3}
b = {2, 3, 4}
a | b       # Union: {1, 2, 3, 4}
a & b       # Intersection: {2, 3}
a - b       # Difference: {1}
a ^ b       # Symmetric difference: {1, 4}
```

## Control Flow

```python
# if / elif / else
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")

# Ternary
result = "even" if x % 2 == 0 else "odd"

# Match (Python 3.10+)
match command:
    case "quit":
        exit()
    case "hello":
        print("Hi!")
    case _:
        print("Unknown command")
```

## Loops

```python
# for loop
for item in [1, 2, 3]:
    print(item)

for i in range(5):         # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):  # 2, 4, 6, 8
    print(i)

for i, val in enumerate(["a", "b", "c"]):
    print(i, val)           # 0 a, 1 b, 2 c

# while loop
while condition:
    do_something()

# break / continue
for i in range(10):
    if i == 5:
        break       # Exit loop entirely
    if i % 2 == 0:
        continue    # Skip to next iteration
    print(i)
```

## Functions

```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# Default arguments
def greet(name="World"):
    return f"Hello, {name}!"

# *args and **kwargs
def func(*args, **kwargs):
    print(args)     # Tuple of positional args
    print(kwargs)   # Dict of keyword args

# Lambda
square = lambda x: x ** 2

# Type hints (optional but recommended)
def add(a: int, b: int) -> int:
    return a + b
```

## Classes

```python
class Dog:
    # Class variable
    species = "Canis lupus"

    def __init__(self, name: str, age: int):
        self.name = name        # Instance variable
        self.age = age

    def bark(self) -> str:
        return f"{self.name} says Woof!"

    def __str__(self) -> str:
        return f"Dog({self.name}, {self.age})"

    def __repr__(self) -> str:
        return f"Dog(name='{self.name}', age={self.age})"

# Inheritance
class Puppy(Dog):
    def __init__(self, name: str):
        super().__init__(name, age=0)

    def bark(self) -> str:
        return f"{self.name} says Yip!"

# Usage
dog = Dog("Rex", 5)
print(dog.bark())
```

## File I/O

```python
# Reading
with open("file.txt", "r") as f:
    content = f.read()          # Entire file as string
    # or
    lines = f.readlines()       # List of lines
    # or
    for line in f:              # Line by line (memory efficient)
        print(line.strip())

# Writing
with open("file.txt", "w") as f:   # Overwrites
    f.write("Hello\n")

with open("file.txt", "a") as f:   # Appends
    f.write("World\n")

# JSON
import json
with open("data.json", "r") as f:
    data = json.load(f)

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Pathlib (modern approach)
from pathlib import Path
p = Path("folder") / "file.txt"
content = p.read_text()
p.write_text("Hello")
p.exists()
p.is_file()
p.is_dir()
```

## Error Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError):
    print("Type or value error")
except Exception as e:
    print(f"Unexpected: {e}")
else:
    print("No errors!")       # Runs if no exception
finally:
    print("Always runs")      # Cleanup code

# Raising exceptions
raise ValueError("Invalid input")

# Custom exceptions
class MyError(Exception):
    pass
```

## Common Built-in Functions

```python
# Math
abs(-5)          # 5
round(3.7)       # 4
round(3.14159, 2) # 3.14
pow(2, 3)        # 8
divmod(17, 5)    # (3, 2) — quotient, remainder

# Type conversion
int("42")        # 42
float("3.14")    # 3.14
str(42)          # "42"
bool(0)          # False
list("abc")      # ["a", "b", "c"]
tuple([1,2,3])   # (1, 2, 3)
set([1,1,2])     # {1, 2}

# Iteration helpers
range(5)                    # 0, 1, 2, 3, 4
enumerate(["a","b"])        # (0,"a"), (1,"b")
zip([1,2], ["a","b"])       # (1,"a"), (2,"b")
map(str, [1,2,3])           # "1", "2", "3"
filter(lambda x: x>0, [-1,0,1,2])  # 1, 2
sorted([3,1,2])             # [1, 2, 3]
reversed([1,2,3])           # 3, 2, 1
any([False, True])          # True
all([True, True])           # True
```

## Decorators

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
```

## Useful Standard Library Modules

```python
import os               # OS interface
import sys              # System-specific params
import math             # Math functions
import random           # Random numbers
import datetime         # Date and time
import json             # JSON encoding/decoding
import csv              # CSV file reading/writing
import re               # Regular expressions
import pathlib          # Object-oriented filesystem paths
import collections      # Specialized containers
import itertools        # Iterator building blocks
import functools        # Higher-order functions
import argparse         # CLI argument parsing
import unittest         # Testing framework
import logging          # Logging facility
import typing           # Type hints
```

## Virtual Environments

```bash
# Create
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (macOS/Linux)
source .venv/bin/activate

# Install packages
pip install requests

# Save dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Deactivate
deactivate
```
