# Lecture 05: Dictionaries & Sets

Dictionaries and sets allow you to store collections of data where items are key-value pairs or unique values.

---

## 1. Dictionaries
A **dictionary** is an unordered, mutable collection of **key-value pairs**. It is defined using curly braces `{}`.

```python
alien_0 = {"color": "green", "points": 5}
```

### Accessing Values
You access the value by specifying its key inside square brackets:
```python
print(alien_0["color"])   # Output: green
```

If the key does not exist, Python will raise a `KeyError`. To avoid this, use the `get()` method, which returns `None` or a specified default value if the key is missing:
```python
print(alien_0.get("speed", "slow"))  # Output: slow
```

### Modifying and Adding Key-Value Pairs
```python
# Modifying
alien_0["color"] = "yellow"

# Adding
alien_0["x_position"] = 0
```

### Removing Key-Value Pairs
- **`del`**: Permanently deletes a key-value pair.
- **`pop()`**: Removes the key and returns its value.

```python
del alien_0["points"]
```

---

## 2. Sets
A **set** is an unordered collection of **unique** elements. Sets do not allow duplicates. They are defined using curly braces `{}` or the `set()` constructor.

```python
fruits = {"apple", "banana", "orange", "apple"}
print(fruits)  # Output: {"apple", "banana", "orange"} (duplicates are removed!)
```

### Common Set Operations
- **`add()`**: Adds an item.
- **`remove()`**: Removes an item (raises error if missing).
- **`discard()`**: Removes an item (does not raise error if missing).
- **Set operations**: Union (`|`), Intersection (`&`), Difference (`-`), Symmetric Difference (`^`).

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union: {1, 2, 3, 4, 5}
print(a & b)  # Intersection: {3}
print(a - b)  # Difference: {1, 2}
```

---

## 🧠 Try It Yourself
1. Create a dictionary representing your favorite programming languages. Key should be the person's name, value should be the language. Use `get()` to look up a name that isn't in your dictionary.
2. Given a list containing duplicates, convert it to a set to remove duplicates, and then back to a list.
