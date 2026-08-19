# Chapter 5: if Statements

## Key Concepts

### Conditional Tests
A conditional test is an expression that evaluates to `True` or `False`. Python uses boolean values (`True`, `False`) to decide whether the code in an `if` statement should be executed.

```python
car = 'subaru'
print(car == 'subaru')  # True (equality operator)
print(car == 'audi')    # False
print(car != 'audi')    # True (inequality operator)
```

- **Case sensitivity**: `'Audi' == 'audi'` is `False`. You can use `.lower()` to do case-insensitive comparisons: `car.lower() == 'audi'`.

### Comparison Operators
- `==` Equality
- `!=` Inequality
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

### Checking Multiple Conditions
- **`and`**: True only if *both* conditions are True.
- **`or`**: True if *at least one* condition is True.

```python
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)  # False
print(age_0 >= 21 or age_1 >= 21)   # True
```

### Checking Whether a Value Is in a List
- **`in`**: Check if a value exists in a collection.
- **`not in`**: Check if a value does *not* exist in a collection.

```python
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)  # True
print('pepperoni' not in requested_toppings)  # True
```

### The `if-elif-else` Chain
Python executes only one block in an `if-elif-else` chain. It runs the first test that passes and skips the rest.

```python
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")
```

- The `elif` blocks can be repeated as many times as needed.
- The `else` block is optional. You can end with an `elif` block instead to ensure only explicit conditions match.

### Testing Multiple Conditions Individually
Sometimes you want to check all conditions. In this case, use multiple simple `if` statements instead of `if-elif-else`.

```python
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
```

### Using `if` Statements with Lists
- Check if a list is empty: `if list_name:` evaluates to `True` if it has elements, and `False` if it is empty.

```python
requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}.")
else:
    print("Are you sure you want a plain pizza?")
```

## Common Pitfalls
- **Confusing `=` with `==`**: `=` is for assignment, `==` is for comparison.
- **Indentation errors**: The block of code inside the `if` statement must be indented.
- **Logical flaws in chain order**: Place more specific conditions before general ones in `if-elif-else` chains.

## Try It Yourself
1. Create a conditional test for string equality, inequality, numbers, and multiple conditions using `and`/`or`.
2. Write an `if-elif-else` chain that determines a person's stage of life based on their age variable.
3. Make a list of usernames, including 'admin'. Loop through the list and print greetings. If the username is 'admin', print a special greeting. If the list is empty, print a message asking for users.
