# 📋 Common Python Mistakes

This document highlights common pitfalls and bugs encountered by beginners and intermediate Python developers, along with how to avoid them.

---

## 1. Mutable Default Arguments
In Python, default arguments are evaluated **once** when the function is defined, not each time the function is called. If you use a mutable object (like a list or dictionary) as a default argument, all calls share the same object!

### ❌ Bad:
```python
def add_item(item, item_list=[]):
    item_list.append(item)
    return item_list

print(add_item("apple"))  # Output: ["apple"]
print(add_item("banana")) # Output: ["apple", "banana"] (unexpected!)
```

###  Good:
Use `None` as the default value and initialize the mutable object inside the function:
```python
def add_item(item, item_list=None):
    if item_list is None:
        item_list = []
    item_list.append(item)
    return item_list

print(add_item("apple"))  # Output: ["apple"]
print(add_item("banana")) # Output: ["banana"]
```

---

## 2. Copying Collections by Reference
Using the assignment operator `=` does not make a copy of a list or dictionary. It only creates another reference pointing to the same object in memory.

### ❌ Bad:
```python
original = [1, 2, 3]
copy = original  # Reference copy
copy.append(4)

print(original)  # Output: [1, 2, 3, 4] (original was modified!)
```

###  Good:
Use slicing, `.copy()`, or the `list()` constructor to create a new shallow copy:
```python
original = [1, 2, 3]

# Slicing
copy1 = original[:]

# .copy() method
copy2 = original.copy()

# constructor
copy3 = list(original)
```

---

## 3. Modifying a Collection While Iterating
Modifying a list or dictionary while looping over it can lead to skipping elements, infinite loops, or runtime errors.

### ❌ Bad:
```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Modifying list during iteration
```

###  Good:
Iterate over a copy of the list, or use list comprehension to create a filtered list:
```python
numbers = [1, 2, 3, 4, 5]

# Using list comprehension
numbers = [num for num in numbers if num % 2 != 0]
```

---

## 4. Broad Exceptions
Catching all exceptions using an empty `except:` block hides syntax errors, keyboard interrupts (Ctrl+C), and other unexpected bugs.

### ❌ Bad:
```python
try:
    x = int(input("Enter number: "))
    result = 10 / x
except:  # Catches EVERYTHING
    print("An error occurred")
```

###  Good:
Catch specific exceptions that you expect and know how to handle:
```python
try:
    x = int(input("Enter number: "))
    result = 10 / x
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## 5. File Leakage
Opening a file without closing it can lead to locked files or file descriptor leaks.

### ❌ Bad:
```python
f = open("data.txt", "r")
content = f.read()
# If an error happens here, f.close() is never called!
f.close()
```

###  Good:
Use a `with` statement (context manager), which automatically closes the file:
```python
with open("data.txt", "r") as f:
    content = f.read()
```
