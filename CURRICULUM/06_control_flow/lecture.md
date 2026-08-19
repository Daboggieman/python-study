# Lecture 06: Control Flow

Control flow allows your program to make decisions and execute different paths of code based on conditions.

---

## 1. If/Elif/Else Statements
Python uses the keywords `if`, `elif` (short for else-if), and `else` to control decision making:

```python
age = 18

if age >= 21:
    print("You can enter the club and buy drinks.")
elif age >= 18:
    print("You can enter the club but cannot buy drinks.")
else:
    print("You are too young to enter the club.")
```

- In Python, code blocks are defined by **indentation** (typically 4 spaces).
- The colon (`:`) at the end of conditional lines is required.

---

## 2. Logical Operators
You can combine multiple conditions using logical operators:
- **`and`**: True if both conditions are True.
- **`or`**: True if at least one condition is True.
- **`not`**: Reverses the boolean value of a condition.

```python
has_id = True
is_vip = False

if has_id and (age >= 18 or is_vip):
    print("Welcome!")
```

---

## 3. Truthy and Falsy Values
In Python, values can evaluate to `True` or `False` when used in a conditional statement.

### Falsy values:
- `None`
- `False`
- `0` (integer) or `0.0` (float)
- Empty sequences or collections: `""`, `[]`, `()`, `{}`, `set()`

Any other value in Python is considered **Truthy**.

```python
name = input("Enter your name: ")
if name:  # Checks if name is not an empty string
    print(f"Hello, {name}!")
else:
    print("You didn't enter a name.")
```

---

## 4. Ternary Operators
Ternary operators provide a shorthand way to write simple `if-else` statements.

Syntax: `value_if_true if condition else value_if_false`

```python
x = 10
status = "even" if x % 2 == 0 else "odd"
print(status)  # Output: even
```

---

## 5. Match Statements (Python 3.10+)
Similar to switch-case statements in other languages, `match` statements offer structural pattern matching.

```python
command = "start"

match command:
    case "start":
        print("Starting the system...")
    case "stop" | "halt":
        print("Stopping the system...")
    case _:
        print("Unknown command.")  # Default wildcard pattern
```

---

## 🧠 Try It Yourself
1. Write a program that takes a score (0–100) and prints grades: A (>=90), B (>=80), C (>=70), and F (otherwise).
2. Use a ternary operator to assign "allowed" if `age` is >= 18, otherwise "denied".
