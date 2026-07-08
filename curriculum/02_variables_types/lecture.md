# Lecture 02: Variables & Types

In programming, we need a way to store data so we can use it later. In Python, we do this using **variables**.

---

## 1. Creating Variables
To create a variable, you assign a value to a name using the `=` operator.

```python
x = 5
message = "Hello, Python!"
```

- In Python, you do **not** need to declare a variable's type before using it. Python automatically figures out the type of the value. This is called **dynamic typing**.
- A variable is a **label** pointing to a value in memory, not a container holding it.

---

## 2. Naming Rules
Variables must follow these naming rules:
- Names can contain letters, numbers, and underscores (`_`).
- Names cannot start with a number.
- Spaces are not allowed (use underscores instead).
- Avoid using Python keywords (like `print`, `if`, `for`, `class`, etc.).
- Python is case-sensitive (`age`, `Age`, and `AGE` are three different variables).

### Best Practices:
- Use **snake_case** for multi-word variable names (e.g., `student_name`, `user_age`, `total_price`).
- Choose descriptive names (use `score` instead of `s`).

---

## 3. Basic Data Types
Python has several built-in basic data types.

### Integers (`int`)
Whole numbers without a fractional part.
```python
age = 21
count = -5
```
*Note*: You can use underscores in large numbers to make them easier to read: `one_million = 1_000_000` (Python ignores the underscores).

### Floating-Point Numbers (`float`)
Numbers with a decimal point.
```python
price = 19.99
pi = 3.14159
```

### Booleans (`bool`)
Represent logical values: either `True` or `False`.
```python
is_active = True
has_passed = False
```

### NoneType (`None`)
A special type that represents the absence of a value.
```python
result = None
```

---

## 4. Checking Types with `type()`
You can find out the data type of any value or variable using the built-in `type()` function:

```python
x = 10
print(type(x))  # Output: <class 'int'>

y = 3.14
print(type(y))  # Output: <class 'float'>
```

---

## 5. Type Conversion (Casting)
You can convert a value from one type to another using built-in functions:

```python
# Convert float to int (truncates the decimal part)
print(int(3.9))  # Output: 3

# Convert int to float
print(float(5))  # Output: 5.0

# Convert number to string
print(str(100))  # Output: "100"

# Convert string to integer
print(int("25"))  # Output: 25
```

---

## 🧠 Try It Yourself
1. Store your age in a variable called `my_age`.
2. Convert `my_age` to a float and print it.
3. What happens if you try to convert the string `"apple"` to an integer? Try it in the REPL and note the error.
