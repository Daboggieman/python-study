# Chapter 8: Functions

## Key Concepts

### Defining a Function
A function is a named block of code designed to do one specific job.

```python
def greet_user(username):
    """Display a simple greeting."""  # Docstring
    print(f"Hello, {username.title()}!")

greet_user('jesse')
```

- **Docstring**: The triple-quoted string at the beginning of a function is a docstring. It describes what the function does.
- **Parameters vs Arguments**: `username` in the definition is a **parameter**. `'jesse'` in the call is an **argument**.

### Passing Arguments

#### Positional Arguments
Arguments matched based on the order in which they are written.

```python
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
```

#### Keyword Arguments
Arguments passed as name-value pairs, making order irrelevant.

```python
describe_pet(pet_name='harry', animal_type='hamster')
```

#### Default Values
Parameters can have default values. Defined default parameters must follow parameters without default values.

```python
def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')  # Uses default 'dog'
describe_pet('harry', 'hamster') # Overrides default
```

### Return Values
Functions can return values back to the calling line using the `return` statement.

```python
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)  # 'Jimi Hendrix'
```

- **Returning a Dictionary**:
```python
def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
```

### Passing a List to a Function
When you pass a list to a function, the function gets direct access to the list. Any changes made inside the function modify the original list.

```python
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
```

- **Preventing Modifying a List**: To keep the original list intact, pass a copy of the list using a slice `[:]`.
```python
print_models(unprinted_designs[:], completed_models)
```

### Passing an Arbitrary Number of Arguments
Use `*args` and `**kwargs` to accept an unknown number of positional or keyword arguments.

- **`*args` (Tuple of arguments)**:
```python
def make_pizza(*toppings):
    # toppings is collected as a tuple
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

- **`**kwargs` (Dictionary of arguments)**:
```python
def build_profile(first, last, **user_info):
    # user_info is collected as a dictionary
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
```

### Storing Functions in Modules
You can store functions in a separate file (a **module**) and import them into your main program.

Assuming a module named `pizza.py`:
```python
# Import the entire module
import pizza
pizza.make_pizza(16, 'pepperoni')

# Import specific functions
from pizza import make_pizza
make_pizza(16, 'pepperoni')

# Using alias for function
from pizza import make_pizza as mp
mp(16, 'pepperoni')

# Using alias for module
import pizza as p
p.make_pizza(16, 'pepperoni')

# Import all functions (discouraged due to naming conflicts)
from pizza import *
```

## Common Pitfalls
- **Positional Argument Mix-up**: Writing arguments in the wrong order when calling a function.
- **Modifying Lists Unintentionally**: Passing a list to a function and forgetting that operations like `.pop()` or `.clear()` will affect the caller's list.
- **Shadowing Names**: Using a variable name inside a function that masks a global variable, causing confusion.

## Try It Yourself
1. Write a function called `display_message()` that prints a sentence telling everyone what you are learning about in this chapter. Call the function.
2. Write a function called `make_shirt()` that accepts a size and the text of a message that should be printed on the shirt. Use both positional and keyword arguments to call it.
3. Write a function called `send_messages()` that prints each text message from a list and moves them to a new list. Ensure the original list is preserved.
