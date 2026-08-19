# Chapter 2: Variables and Simple Data Types

## Key Concepts

### Variables
```python
message = "Hello, Python!"
print(message)
```
- Variable names can contain letters, numbers, and underscores
- Cannot start with a number
- Use **snake_case** by convention: `my_variable`, `student_name`
- Variables are **labels** that point to values — not boxes that contain them
- No need to declare types — Python figures it out (**dynamic typing**)

### Strings
```python
name = "ada lovelace"

# Methods (don't modify original — return new string)
name.title()    # "Ada Lovelace"
name.upper()    # "ADA LOVELACE"
name.lower()    # "ada lovelace"
name.strip()    # Remove whitespace from ends

# f-strings (Python 3.6+)
first = "ada"
last = "lovelace"
full = f"{first} {last}"       # "ada lovelace"
print(f"Hello, {full.title()}!")  # "Hello, Ada Lovelace!"

# Escape characters
tab = "Hello\tWorld"     # Tab
newline = "Hello\nWorld" # New line
```

### Numbers
```python
# Integers
x = 10
big = 1_000_000   # Underscores for readability (= 1000000)

# Floats
y = 3.14
z = 0.1 + 0.1     # 0.2 (mostly — beware floating-point quirks)
w = 0.1 + 0.2     # 0.30000000000000004 (not exactly 0.3!)

# Operations
2 + 3    # 5  (addition)
3 - 1    # 2  (subtraction)
2 * 3    # 6  (multiplication)
3 / 2    # 1.5 (division — always returns float)
3 // 2   # 1  (floor division — integer result)
3 % 2    # 1  (modulo — remainder)
2 ** 3   # 8  (exponentiation)

# Mixing ints and floats → always produces float
4 + 2.0  # 6.0
```

### Constants
```python
# Python has no true constants — use ALL_CAPS as convention
MAX_CONNECTIONS = 100
PI = 3.14159
```

### Multiple Assignment
```python
x, y, z = 1, 2, 3
```

### Type Conversion
```python
age = "30"
age_num = int(age)      # String → int
height = float("5.9")   # String → float
score = str(100)        # Int → string
```

## Common Pitfalls
- **NameError**: Using a variable before assigning it, or misspelling the name
- **TypeError**: Trying to concatenate a string and number without str()
- Floating-point arithmetic: `0.1 + 0.2 != 0.3` — use `round()` or `decimal` module for precision
- Forgetting `f` prefix on f-strings: `"{name}"` literally prints `{name}`

## Try It Yourself
1. Store your name in a variable and print a greeting using an f-string
2. Experiment with all arithmetic operators
3. Try `type()` on different values: `type(42)`, `type(3.14)`, `type("hello")`, `type(True)`
4. Deliberately cause a NameError and a TypeError — understand the error messages
