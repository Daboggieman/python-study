# Chapter 6: Dictionaries

## Key Concepts

### What Is a Dictionary?
A dictionary in Python is an unordered, mutable collection of **key-value pairs**. Each key is connected to a value, and you can use a key to access the value associated with it. Keys must be unique and immutable (strings, numbers, tuples).

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])   # 'green'
print(alien_0['points'])  # 5
```

### Working with Dictionaries
```python
# Adding new key-value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25

# Starting with an empty dictionary
alien_1 = {}
alien_1['color'] = 'blue'

# Modifying values
alien_0['color'] = 'yellow'

# Removing key-value pairs (permanent)
del alien_0['points']
```

### Using `get()` to Access Values
If you try to access a key that doesn't exist, Python raises a `KeyError`. To avoid this, use `get()`, which returns a default value if the key does not exist.

```python
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])  # KeyError!
points_value = alien_0.get('points', 'No point value assigned.')
print(points_value)  # 'No point value assigned.'
```

### Looping Through a Dictionary
You can loop through all key-value pairs, keys, or values.

```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# Loop through all key-value pairs
for key, value in user_0.items():
    print(f"Key: {key}, Value: {value}")

# Loop through all keys (default behavior)
for name in user_0.keys():  # or just: for name in user_0:
    print(name)

# Loop through keys in sorted order
for name in sorted(user_0.keys()):
    print(name)

# Loop through all values
for val in user_0.values():
    print(val)

# Loop through unique values using set()
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
for lang in set(favorite_languages.values()):
    print(lang.title())  # Python, C, Ruby
```

### Nesting
You can store dictionaries inside lists, lists inside dictionaries, or dictionaries inside dictionaries.

```python
# A list of dictionaries
aliens = [
    {'color': 'green', 'points': 5},
    {'color': 'yellow', 'points': 10},
    {'color': 'red', 'points': 15},
]

# A list inside a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# A dictionary inside a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
```

## Common Pitfalls
- **KeyError**: Accessing a key that doesn't exist. Use `get()` or check `if key in dict:`.
- **Modifying while looping**: Modifying a dictionary directly inside a loop over its keys can raise a `RuntimeError`. Loop over `list(dict.keys())` instead if modification is needed.

## Try It Yourself
1. Create a dictionary representing a person with first name, last name, age, and city. Print each piece of information.
2. Use a dictionary to store people's favorite numbers. Loop through and print each person's name and favorite number.
3. Make three dictionaries representing different pets. Store all three in a list called `pets`. Loop through your list and print everything you know about each pet.
