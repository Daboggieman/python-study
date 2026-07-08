# Chapter 1: Getting Started

## Key Concepts

### What is Python?
- Python is a **high-level, interpreted** programming language created by Guido van Rossum (first released 1991)
- Known for its **readability** and **simplicity** — designed to be easy to learn
- Used everywhere: web development, data science, AI/ML, automation, scripting, game development
- Python uses **indentation** (whitespace) to define code blocks — no curly braces like C/Java

### Installing Python
- Download from https://python.org
- On Windows: **check "Add Python to PATH"** during installation
- Verify: `python --version` or `python3 --version` in terminal

### Running Python Code

**Interactive mode (REPL):**
```python
>>> print("Hello!")
Hello!
>>> 2 + 3
5
```

**Script mode:**
```bash
python hello.py
```

### Your First Program
```python
# hello.py
print("Hello, World!")
```

- `print()` is a **built-in function** that outputs text to the terminal
- Strings can use `"double"` or `'single'` quotes
- Lines starting with `#` are **comments** — ignored by Python

### The Python Philosophy
Run `import this` in the REPL to see "The Zen of Python":
- Beautiful is better than ugly
- Simple is better than complex
- Readability counts

## Common Pitfalls
- Forgetting to add Python to PATH on Windows
- Mixing `python` and `python3` commands (system-dependent)
- Indentation errors — Python requires consistent indentation

## Try It Yourself
1. Install Python and verify it works in your terminal
2. Open the REPL and try basic math: `2 + 2`, `10 / 3`, `2 ** 8`
3. Create a `hello.py` file and run it
4. Add a comment to your file and run it again — notice comments are ignored
