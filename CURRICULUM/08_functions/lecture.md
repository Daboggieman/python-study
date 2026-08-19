# Lecture 08: Functions

Functions are named blocks of code designed to perform a specific task. They help make your code reusable, organized, and modular.

---

## 1. Defining a Function
Use the `def` keyword followed by the function name and parentheses:

```python
def greet():
    """Display a simple greeting."""  # Docstring
    print("Hello, World!")

greet()  # Call the function
```

- **Docstring**: The triple-quoted string is a documentation string. It describes what the function does and is accessed via `help(greet)` or `greet.__doc__`.

---

## 2. Arguments and Parameters
- **Parameters**: Variables listed in the function definition (e.g., `name` below).
- **Arguments**: Values passed to the function when calling it (e.g., `"Alice"` below).

```python
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")
```

---

## 3. Positional vs Keyword Arguments
You can pass arguments by position or by explicit name.

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# Positional (order matters)
describe_pet("dog", "Rex")

# Keyword (order does not matter)
describe_pet(pet_name="Rex", animal_type="dog")
```

---

## 4. Default Values
Parameters can have default values. Parameters with default values must come *after* parameters without defaults.

```python
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("Rex")  # Uses default "dog"
describe_pet("Whiskers", "cat")  # Overrides default
```

---

## 5. Return Values
Functions can send data back to the caller using the `return` statement. If no `return` is executed, the function returns `None`.

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8
```

---

## 6. Arbitrary Arguments (`*args` and `**kwargs`)
Sometimes you don't know how many arguments will be passed to a function.

- **`*args`**: Collects extra positional arguments into a **tuple**.
- **`**kwargs`**: Collects extra keyword arguments into a **dictionary**.

```python
# Arbitrary positional arguments
def make_pizza(*toppings):
    print(toppings)  # e.g., ('mushrooms', 'peppers')

make_pizza("mushrooms", "peppers")

# Arbitrary keyword arguments
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

profile = build_profile("Albert", "Einstein", location="Princeton", field="Physics")
print(profile)
```

---

## 7. Variable Scope
- **Local scope**: Variables defined inside a function can only be accessed inside that function.
- **Global scope**: Variables defined outside functions can be accessed anywhere.

```python
x = 10  # Global variable

def my_func():
    y = 5  # Local variable
    print(x)  # Accessible
    print(y)  # Accessible

my_func()
# print(y)  # NameError: name 'y' is not defined
```

---

## 8. Lambda Functions
Lambdas are small, anonymous functions defined with the `lambda` keyword. They are limited to a single expression.

Syntax: `lambda arguments: expression`

```python
square = lambda num: num ** 2
print(square(5))  # 25
```

---

## 🧠 Try It Yourself
1. Write a function called `city_country()` that takes the name of a city and its country. The function should return a string formatted like `"Santiago, Chile"`.
2. Write a function that accepts a list of numbers and returns a new list containing only the even numbers from the original list.
