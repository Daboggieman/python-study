# Chapter 3: Introducing Lists

## Key Concepts

### What Is a List?
A list is an **ordered, mutable collection** of items. Lists can hold any data type and mix types.

```python
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)    # ['trek', 'cannondale', 'redline', 'specialized']
```

### Accessing Elements
```python
bicycles[0]      # "trek" (first element — zero-indexed!)
bicycles[-1]     # "specialized" (last element)
bicycles[1]      # "cannondale"
```

### Modifying Lists

```python
# Change an element
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles[0] = "ducati"   # ["ducati", "yamaha", "suzuki"]

# Add elements
motorcycles.append("harley")          # Add to end
motorcycles.insert(0, "bmw")          # Insert at position

# Remove elements
del motorcycles[0]                     # Delete by index
popped = motorcycles.pop()             # Remove & return last
popped = motorcycles.pop(0)            # Remove & return at index
motorcycles.remove("yamaha")           # Remove by value (first match)
```

### Organizing Lists
```python
cars = ["bmw", "audi", "toyota", "subaru"]

# Permanent sort
cars.sort()                    # Alphabetical (in place)
cars.sort(reverse=True)        # Reverse alphabetical

# Temporary sort
sorted_cars = sorted(cars)     # Returns new list, original unchanged

# Reverse order
cars.reverse()                 # Reverses in place

# Length
len(cars)                      # 4
```

### Avoiding Index Errors
```python
motorcycles = ["honda", "yamaha"]
# motorcycles[5]   # IndexError!
# motorcycles[-3]  # IndexError! (only 2 items)
```
- Use `len()` to check before accessing
- An empty list `[]` has no valid index

## Common Pitfalls
- **Off-by-one errors**: Lists are zero-indexed — the first item is `[0]`, not `[1]`
- `remove()` only removes the **first** occurrence
- `sort()` modifies the list in place and returns `None` — don't do `cars = cars.sort()`
- Accessing an index beyond the list length raises `IndexError`

## Try It Yourself
1. Create a list of 5 friends' names and print each using their index
2. Add a name, remove a name, and replace a name
3. Sort the list alphabetically, then reverse it
4. Try to access an index that doesn't exist — read the error message
