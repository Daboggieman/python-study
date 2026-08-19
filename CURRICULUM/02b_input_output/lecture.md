# Lecture 02b: Input, Output, and Formatting

Getting input from users and presenting output clearly are core beginner skills in Python.

---

## 1. Printing Information
The `print()` function displays text or values to the screen.

```python
print("Hello")
print(42)
```

You can print multiple values at once:

```python
print("Name:", "Ada")
```

### `sep` and `end`
```python
print("Python", "is", "fun", sep="-", end="!\n")
```

---

## 2. Getting User Input
Use `input()` to ask the user for information.

```python
name = input("What is your name? ")
print("Hello, " + name)
```

Important: `input()` always returns a string.

```python
age = input("Enter your age: ")
print(type(age))
```

---

## 3. Converting Input
If you want numbers, convert the input string.

```python
age = int(input("Enter your age: "))
print(age + 1)
```

Common conversions:
- `int()`
- `float()`
- `str()`
- `bool()`

---

## 4. String Formatting
Python offers several ways to format output.

### Concatenation
```python
name = "Ada"
print("Hello, " + name)
```

### f-strings
```python
name = "Ada"
print(f"Hello, {name}")
```

### `.format()`
```python
print("Hello, {}".format(name))
```

---

## 🧠 Try It Yourself
1. Ask the user for their name and print a greeting.
2. Ask for a number, convert it to an integer, and print the next number.
3. Use an f-string to print a short message with two values.
