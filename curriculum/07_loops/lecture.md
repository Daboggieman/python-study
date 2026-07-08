# Lecture 07: Loops

Loops allow you to execute a block of code repeatedly. Python supports `for` loops and `while` loops.

---

## 1. For Loops
`for` loops are used to iterate over a sequence (such as a list, tuple, string, or range).

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### The `range()` Function
Use `range()` to generate a sequence of numbers:
```python
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):     # 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (step of 2)
    print(i)
```

---

## 2. While Loops
`while` loops run as long as a specified condition is `True`.

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

---

## 3. Break and Continue
- **`break`**: Exits the loop immediately.
- **`continue`**: Skips the remaining code in the current iteration and jumps to the next iteration.

```python
# Break example
for num in range(10):
    if num == 5:
        break
    print(num)  # Prints 0, 1, 2, 3, 4

# Continue example
for num in range(5):
    if num == 2:
        continue
    print(num)  # Prints 0, 1, 3, 4
```

---

## 4. Loop Else
Python has an optional `else` block for loops. The `else` block runs **only** if the loop completed naturally (without encountering a `break` statement).

```python
for num in range(5):
    print(num)
else:
    print("Loop finished successfully!")
```

---

## 5. Comprehensions
Comprehensions provide a concise way to create lists, dictionaries, or sets from iterable objects.

### List Comprehension
Syntax: `[expression for item in iterable if condition]`

```python
# Create a list of squares of even numbers
squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(squares)  # Output: [0, 4, 16, 36, 64]
```

### Dictionary Comprehension
```python
# Key: number, Value: square of number
squares_dict = {x: x ** 2 for x in range(5)}
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## 🧠 Try It Yourself
1. Write a `while` loop that prompts the user for inputs and prints them, terminating only when the user inputs `"quit"`.
2. Write a list comprehension that extracts all words starting with 'a' from the list `["apple", "banana", "apricot", "cherry"]`.
