# Lecture 12b: Standard Library Modules

Python’s standard library gives you powerful tools without installing anything extra. This lesson introduces commonly used modules and when to use them.

---

## 1. `os` and `os.path`
Use `os` for file system tasks and `os.path` for path handling.

```python
import os
print(os.getcwd())
print(os.listdir("."))
print(os.path.join("data", "file.txt"))
```

---

## 2. `sys`
Use `sys` to access command-line arguments and Python runtime information.

```python
import sys
print(sys.argv)
print(sys.version)
```

---

## 3. `math` and `random`
Math provides mathematical functions. Random generates pseudo-random values.

```python
import math
import random
print(math.sqrt(25))
print(random.randint(1, 10))
```

---

## 4. `datetime`
Work with dates and times.

```python
from datetime import datetime
print(datetime.now())
```

---

## 5. `json`
Store and load structured data.

```python
import json
data = {"name": "Jane", "age": 30}
print(json.dumps(data))
```

---

## 6. `csv`
Read and write comma-separated files.

```python
import csv
```

---

## 🧠 Try It Yourself
1. Print the current working directory and list its contents.
2. Use `math` to compute the hypotenuse of a right triangle.
3. Convert a Python dictionary to a JSON string.
