# 17: The `match` Statement (Structural Pattern Matching)

Python 3.10 introduced `match`/`case` — Python's version of what other languages call a "switch statement," but considerably more powerful because it can match on *structure* (the shape of data), not just a single value.

---

## 1. The Basics: Matching a Value

```python
def describe_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:                  # `_` is the wildcard -- matches anything else
            return "Unknown status"

print(describe_status(404))   # Not Found
print(describe_status(999))   # Unknown status
```

This alone replaces long `if/elif/elif/.../else` chains that just compare one variable to several fixed values.

---

## 2. Matching Multiple Values in One Case

```python
def describe_status(code):
    match code:
        case 200 | 201 | 204:       # `|` means "or" inside a pattern
            return "Success"
        case 400 | 401 | 403 | 404:
            return "Client Error"
        case _:
            return "Other"
```

---

## 3. Matching Structure (This Is the Real Power)

`match` can destructure lists, tuples, and dictionaries directly in the pattern:

```python
def handle_command(command):
    match command:
        case ["go", direction]:
            return f"Moving {direction}"
        case ["pick", "up", item]:
            return f"Picking up {item}"
        case ["go", *rest]:                    # `*rest` captures remaining items
            return f"Go with extra args: {rest}"
        case []:
            return "Empty command"
        case _:
            return "Unknown command"

print(handle_command(["go", "north"]))        # Moving north
print(handle_command(["pick", "up", "key"]))   # Picking up key
```

---

## 4. Matching Dictionaries and Classes

```python
def handle_event(event):
    match event:
        case {"type": "click", "x": x, "y": y}:
            return f"Clicked at ({x}, {y})"
        case {"type": "key", "key": key}:
            return f"Key pressed: {key}"
        case _:
            return "Unknown event"

print(handle_event({"type": "click", "x": 10, "y": 20}))  # Clicked at (10, 20)
```

Note: `{"type": "click", "x": x, "y": y}` doesn't require the dict to have *only* these keys — extra keys are ignored. This is intentional (partial matching).

You can also match against class instances by their attributes:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def describe_point(p):
    match p:
        case Point(x=0, y=0):
            return "Origin"
        case Point(x=0, y=y):
            return f"On the Y-axis at {y}"
        case Point(x=x, y=0):
            return f"On the X-axis at {x}"
        case Point():
            return "Somewhere else"

print(describe_point(Point(0, 0)))   # Origin
print(describe_point(Point(0, 5)))    # On the Y-axis at 5
```

---

## 5. Guards: Adding Conditions to a Case

```python
def classify(n):
    match n:
        case x if x < 0:
            return "negative"
        case 0:
            return "zero"
        case x if x % 2 == 0:
            return "positive even"
        case _:
            return "positive odd"
```

The `if` after a pattern is a **guard** — the case only matches if both the pattern AND the guard condition are true.

---

## 6. `match` vs `if/elif` — When to Reach for Each

- Use `match` when you're comparing **one thing** against several possible **shapes or values** — command parsers, simple state machines, handling different response formats.
- Use `if/elif` when your conditions involve **multiple unrelated variables** or complex boolean logic that doesn't reduce to "what shape/value is this one thing."

---

## 📚 Resources

- **W3Schools:** [Python Match Statement](https://www.w3schools.com/python/python_match.asp)
- **Docs:** [PEP 636 — Structural Pattern Matching Tutorial](https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching)
- **YouTube:** [mCoding — Python 3.10's new Structural Pattern Matching](https://www.youtube.com/watch?v=scIRvS4RXCw)
- **YouTube:** [Tech With Tim — Python Match Statement](https://www.youtube.com/watch?v=T1nfB0KyqEk)

---

## 🧠 Try It Yourself

1. Write a `describe_status(code)` function using `match` for at least 5 HTTP status codes plus a wildcard case.
2. Write a simple text-adventure command handler using list-pattern matching for commands like `["go", direction]`, `["take", item]`, and `["look"]`.
3. Write `classify(n)` using guards to sort a number into "negative", "zero", "positive even", "positive odd".
4. Define a small `Point` class and write `describe_point` using class-pattern matching as shown above.
