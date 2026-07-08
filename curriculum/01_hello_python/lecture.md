# Lecture 01: Hello, Python!

Welcome to your first Python lesson! Python is a high-level, interpreted programming language known for its simplicity and readability. It is used in web development, data science, automation, AI, and more.

---

## 1. Writing Your First Python Program
Every programmer starts with a "Hello, World!" program. In Python, this is incredibly simple compared to languages like Java, C++, or Go.

Create a file named `hello.py` and write the following line:

```python
print("Hello, World!")
```

To run it, open your terminal and type:
```bash
python hello.py
```

### Explanation:
- `print()` is a **built-in function** in Python that outputs text to the screen.
- `"Hello, World!"` is a **string** (text data). In Python, strings must be surrounded by either double quotes (`"`) or single quotes (`'`).

---

## 2. Python Comments
Comments are notes in your code written for humans. Python completely ignores them when running the program.

Use the hash symbol (`#`) to start a comment:

```python
# This is a comment. Python will ignore this.
print("Hello, Python!")  # This comment is inline
```

For multi-line comments, you can repeat the `#` symbol or use a multi-line string (docstring) that isn't assigned to any variable:

```python
"""
This is a multi-line comment.
It uses triple double-quotes.
"""
```

---

## 3. The Python REPL (Interactive Shell)
You don't always need to write files to run Python. You can use the **REPL** (Read-Eval-Print Loop).
Open your terminal and type `python` (or `python3` on Mac/Linux) and press Enter. You should see a prompt like:

```python
>>> 
```

Now you can run Python code line by line:
```python
>>> 3 + 5
8
>>> print("Interactive mode!")
Interactive mode!
>>> exit()
```

---

## 4. Basic Arithmetic
Python can act as a simple calculator. Try these in the REPL:

| Operation | Operator | Example | Result |
|-----------|----------|---------|--------|
| Addition | `+` | `5 + 3` | `8` |
| Subtraction | `-` | `10 - 4` | `6` |
| Multiplication| `*` | `4 * 3` | `12` |
| Division | `/` | `7 / 2` | `3.5` (returns a float) |
| Exponentiation| `**` | `2 ** 3` | `8` (2 cubed) |

---

## 🧠 Try It Yourself
1. Open the interactive Python shell (REPL) and calculate `12345 * 67890`.
2. Write a Python script that prints three lines of text: your name, your favorite programming language, and your goal for this study path.
