# Lecture 10: Files & Exceptions

Learning to work with files and handle exceptions allows your programs to persist data and run robustly without crashing when errors occur.

---

## 1. Reading from a File
To read a file in Python, use the `open()` function. Combining it with the `with` keyword ensures the file is automatically and properly closed after the code block runs.

```python
# Reading the entire file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
```

- **File Modes**: `'r'` (read, default), `'w'` (write/overwrite), `'a'` (append), `'r+'` (read & write).

### Reading Line by Line:
```python
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes extra newlines
```

---

## 2. Writing to a File
When writing to a file, ensure you select `'w'` (overwrite) or `'a'` (append) mode.

```python
with open("output.txt", "w") as file:
    file.write("Hello, writing to a file!\n")
    file.write("Python makes file handling easy.\n")
```

---

## 3. JSON Files
Python's `json` module allows you to save and load Python structures (like lists and dictionaries) directly to files.

```python
import json

data = {"name": "Alice", "age": 25, "active": True}

# Save to JSON file
with open("user.json", "w") as file:
    json.dump(data, file, indent=4)

# Read from JSON file
with open("user.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)
```

---

## 4. Exceptions and Error Handling
Exceptions are errors detected during execution. Use a `try-except` block to catch and handle exceptions to prevent the program from crashing.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
```

### Try-Except-Else-Finally:
- **`else`**: Runs only if the `try` block succeeds without exceptions.
- **`finally`**: Runs no matter what (even if an exception occurs).

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result is {result}")
finally:
    print("Execution of try-except block finished.")
```

---

## 🧠 Try It Yourself
1. Write a program that prompts the user for their name, and appends the name to a `guests.txt` file.
2. Write a function that takes two numbers, divides them, and catches any `ZeroDivisionError` or `ValueError`, returning `None` instead of crashing.
