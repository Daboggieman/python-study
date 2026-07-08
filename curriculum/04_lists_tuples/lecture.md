# Lecture 04: Lists & Tuples

In Python, lists and tuples are used to store multiple items in a single variable.

---

## 1. Lists
A **list** is an ordered, mutable (changeable) collection of items. Lists are defined using square brackets `[]`.

```python
motorcycles = ["honda", "yamaha", "suzuki"]
```

### Accessing Elements
Lists are zero-indexed:
```python
print(motorcycles[0])   # Output: honda
print(motorcycles[-1])  # Output: suzuki (last element)
```

### Modifying Elements
```python
motorcycles[0] = "ducati"
print(motorcycles)  # Output: ["ducati", "yamaha", "suzuki"]
```

### Adding Elements
- **`append()`**: Adds an item to the end of the list.
- **`insert()`**: Adds an item at a specific index.

```python
motorcycles.append("honda")        # Adds to the end
motorcycles.insert(1, "harley")   # Inserts at index 1
```

### Removing Elements
- **`del`**: Deletes an item at a specific index (permanent).
- **`pop()`**: Removes and returns the last item (or index specified).
- **`remove()`**: Removes the first occurrence of a value.

```python
del motorcycles[0]       # Deletes the first element
popped_bike = motorcycles.pop()  # Removes and returns last element
motorcycles.remove("yamaha")     # Removes by value
```

---

## 2. Organizing Lists
- **`sort()`**: Sorts the list permanently in alphabetical/numerical order.
- **`sorted()`**: Returns a sorted copy of the list, leaving the original list unchanged.
- **`reverse()`**: Reverses the order of the list permanently.
- **`len()`**: Returns the length (number of items) in the list.

```python
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()          # Permanent sort
print(sorted(cars))  # Temporary sort
cars.reverse()       # Permanent reverse
print(len(cars))     # 4
```

---

## 3. Tuples
A **tuple** is an ordered, **immutable** (unchangeable) collection of items. Tuples are defined using parentheses `()`.

```python
dimensions = (200, 50)
print(dimensions[0])  # 200

# dimensions[0] = 250  # TypeError! You cannot modify elements in a tuple
```

- If you need to define a tuple with only one element, you *must* include a trailing comma: `single_tuple = (3,)`.

---

## 4. Packing and Unpacking
You can pack values into a tuple or list, and unpack them into individual variables.

```python
# Packing
coordinates = (10, 20)

# Unpacking
x, y = coordinates
print(x)  # 10
print(y)  # 20
```

---

## 🧠 Try It Yourself
1. Create a list of 5 movies. Add one movie to the end, insert one in the middle, and pop the last one. Print the list length.
2. Create a tuple containing three items of food. Try to change one of the foods and look at the error.
