# Chapter 7: User Input and while Loops

## Key Concepts

### How the `input()` Function Works
The `input()` function pauses your program and waits for the user to enter some text. Once Python receives the input, it stores it in a variable as a **string**.

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

- **Type casting**: Since `input()` always returns a string, you must use `int()` or `float()` to convert the input to a number if you plan to do math with it.

```python
age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("You are eligible to vote!")
```

- **Modulo Operator (`%`)**: Often used to check division properties (e.g., checking if a number is even or odd).

```python
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Introducing `while` Loops
A `for` loop takes a collection of items and executes a block of code once for each item. In contrast, a `while` loop runs as long as a certain condition remains `True`.

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

### Letting the User Choose When to Quit
```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
```

### Using a Flag
For complex programs with many conditions that should end the program, you can define one variable (called a **flag**) that acts as a signal to keep the program running.

```python
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
```

### Using `break` to Exit a Loop
To exit a `while` loop immediately without running the rest of the code in the loop, regardless of the loop condition, use `break`.

```python
while True:
    city = input("Please enter a city you have visited (or 'quit'): ")
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
```

### Using `continue` in a Loop
To skip the rest of the current iteration and return to the beginning of the loop, use `continue`.

```python
# Print only odd numbers
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
```

### Using a `while` Loop with Lists and Dictionaries
Using loops with collections allows you to collect, store, and organize input.

```python
# Moving items from one list to another
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Removing all instances of a specific value from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
    pets.remove('cat')

# Filling a dictionary with user input
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
```

## Common Pitfalls
- **Infinite Loops**: Loops that never terminate because the condition is always True. Always ensure there is a clear path to make the condition False, or call a `break`.
- **TypeError with Inputs**: Forgetting to convert string inputs using `int()` or `float()` when doing numerical operations.

## Try It Yourself
1. Write a program that asks the user what kind of rental car they would like, then print a message about it.
2. Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter toppings, print a message saying you'll add that topping to their pizza.
3. Write a program that asks users about their dream vacation destination. Run a poll and print the results when the poll ends.
