# 🐍 Piscine Cheatsheet

A quick-reference guide for solving the Piscine Quests. For a comprehensive cheatsheet, see [python_cheatsheet.md](file:///c:/Users/user/python-study/resources/python_cheatsheet.md).

---

## 1. Input and Output
```python
# Print to console
print("Hello", "World", sep="-")  # Hello-World
print("No newline", end="")

# Read user input
user_input = input("Enter prompt: ")
```

## 2. Basic Conversions
```python
int("123")      # 123
float("3.14")   # 3.14
str(42)         # "42"
list("abc")     # ['a', 'b', 'c']
ord('a')        # 97 (character to ASCII code)
chr(97)         # 'a' (ASCII code to character)
```

## 3. String Manipulation
```python
s = "Hello World"
s[0]          # 'H'
s[-1]         # 'd' (last character)
s[0:5]        # "Hello" (slice)
s[::-1]       # "dlroW olleH" (reverse string)

s.lower()     # "hello world"
s.upper()     # "HELLO WORLD"
s.strip()     # Remove padding whitespace
s.split(" ")  # ['Hello', 'World']
"-".join(['a', 'b'])  # "a-b"
```

## 4. Collections
```python
# Lists
lst = [1, 2, 3]
lst.append(4)      # [1, 2, 3, 4]
lst.pop()          # returns 4, lst becomes [1, 2, 3]
lst.insert(0, 99)  # [99, 1, 2, 3]

# Dictionaries
d = {"name": "Alice", "age": 20}
d["gpa"] = 3.9     # Add key-value
d.get("salary", 0) # Get with default (avoids KeyError)

# Sets (Unique items)
s = {1, 2, 2, 3}   # {1, 2, 3}
s.add(4)
```

## 5. Loops and Ranges
```python
# Loop with index
for idx, val in enumerate(["a", "b"]):
    print(idx, val)

# Loop multiple lists at once
for name, score in zip(["Alice", "Bob"], [95, 88]):
    print(name, score)

# Range patterns
range(5)       # 0, 1, 2, 3, 4
range(1, 6)    # 1, 2, 3, 4, 5
range(5, 0, -1)# 5, 4, 3, 2, 1
```

## 6. Logic and Conditions
```python
# Ternary Operator
result = "even" if x % 2 == 0 else "odd"

# Checking existence
if "apple" in fruits:
    print("Found")
```
