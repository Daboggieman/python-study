# Chapter 4: Working with Lists

## Key Concepts

### Looping Through a List
```python
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone!")  # Outside the loop (not indented)
```
- The `for` loop assigns each item to the loop variable
- **Indentation matters** — indented lines are inside the loop
- The loop variable persists after the loop ends (holds the last value)

### The range() Function
```python
for value in range(5):       # 0, 1, 2, 3, 4
    print(value)

for value in range(1, 6):    # 1, 2, 3, 4, 5
    print(value)

for value in range(2, 11, 2): # 2, 4, 6, 8, 10 (step of 2)
    print(value)

# Convert to list
numbers = list(range(1, 6))   # [1, 2, 3, 4, 5]
```

### Numeric List Functions
```python
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)    # 0
max(digits)    # 9
sum(digits)    # 45
```

### List Comprehensions
A compact way to generate lists:
```python
# Traditional way
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

# List comprehension (same result, one line)
squares = [value ** 2 for value in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# With condition
evens = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

### Slicing Lists
```python
players = ["charles", "martina", "michael", "florence", "eli"]

players[0:3]    # ["charles", "martina", "michael"]
players[1:4]    # ["martina", "michael", "florence"]
players[:4]     # First 4 (start from 0)
players[2:]     # From index 2 to end
players[-3:]    # Last 3
players[::2]    # Every other item

# Looping through a slice
for player in players[:3]:
    print(player.title())
```

### Copying Lists
```python
# Correct: slice copy (independent copy)
my_foods = ["pizza", "falafel", "cake"]
friend_foods = my_foods[:]

# Wrong: assignment (same list, two names!)
friend_foods = my_foods   # Both variables point to SAME list!

# Also correct: list() or .copy()
friend_foods = list(my_foods)
friend_foods = my_foods.copy()
```

### Tuples (Immutable Lists)
```python
dimensions = (200, 50)
print(dimensions[0])     # 200
# dimensions[0] = 250    # TypeError! Tuples can't be modified

# Single-element tuple needs trailing comma
my_tuple = (3,)

# Can reassign the whole variable
dimensions = (400, 100)

# Loop through tuple
for dimension in dimensions:
    print(dimension)
```

## Common Pitfalls
- **Forgetting the colon** at the end of `for` line
- **Incorrect indentation** — Python uses indentation to determine what's inside the loop
- `range(1, 5)` goes up to but **doesn't include** 5
- Copying with `=` creates a **reference**, not a copy — use `[:]` or `.copy()`
- Forgetting the trailing comma in a single-element tuple: `(3)` is just `3`, not a tuple

## Try It Yourself
1. Use a `for` loop to print numbers 1 through 20
2. Create a list of cubes from 1 to 10 using a list comprehension
3. Print the first 3 and last 3 items of a list using slicing
4. Make a copy of a list using `[:]` — modify the copy and confirm the original is unchanged
