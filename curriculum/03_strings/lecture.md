# Lecture 03: Strings

Strings are collections of characters. They are one of the most commonly used data types in Python.

---

## 1. Creating Strings
In Python, strings can be enclosed in single quotes (`'`) or double quotes (`"`):

```python
simple_string = 'Hello'
another_string = "Python"
```

This flexibility allows you to include quotes inside strings easily:
```python
quote = "He said, 'Python is amazing!'"
contraction = 'It is not a problem.'
```

---

## 2. String Concatenation and Repetition
You can combine strings using the `+` operator, and repeat them using the `*` operator:

```python
# Concatenation
greeting = "Hello" + " " + "World!"  # "Hello World!"

# Repetition
echo = "Hello! " * 3  # "Hello! Hello! Hello! "
```

---

## 3. String Methods
Python provides many built-in methods to perform operations on strings. Note that strings in Python are **immutable** (they cannot be changed in place), so string methods always return a *new* string.

```python
name = "ada lovelace"

# Title Case (capitalizes first letter of each word)
print(name.title())  # Output: Ada Lovelace

# Upper and Lower Case
print(name.upper())  # Output: ADA LOVELACE
print(name.lower())  # Output: ada lovelace
```

### Removing Whitespace
```python
favorite_language = " python "

print(favorite_language.strip())   # Output: "python" (removes from both ends)
print(favorite_language.lstrip())  # Output: "python " (removes from left)
print(favorite_language.rstrip())  # Output: " python" (removes from right)
```

---

## 4. Formatted Strings (f-strings)
F-strings (introduced in Python 3.6) are the cleanest and most readable way to insert variables into strings.

To create an f-string, prefix the string with an `f` and place variables or expressions inside curly braces `{}`:

```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

print(f"Hello, {full_name.title()}!")  # Output: Hello, Ada Lovelace!
```

You can also run code inside the curly braces:
```python
print(f"2 + 2 = {2 + 2}")  # Output: 2 + 2 = 4
```

---

## 5. String Slicing and Indexing
You can access individual characters in a string using square brackets `[]` and indices (starting at 0).

```python
s = "Python"

print(s[0])   # Output: P (first character)
print(s[-1])  # Output: n (last character)
```

You can extract a substring using **slicing** with the syntax `[start:stop:step]`:
```python
print(s[0:3])  # Output: Pyt (indices 0, 1, 2. Stop index 3 is not included)
print(s[2:])   # Output: thon (from index 2 to the end)
print(s[::-1]) # Output: nohtyP (reverses the string!)
```

---

## 🧠 Try It Yourself
1. Store a person's name in a variable, and include some whitespace characters at the beginning and end of their name (e.g., using `\t` and `\n`).
2. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions: `lstrip()`, `rstrip()`, and `strip()`.
