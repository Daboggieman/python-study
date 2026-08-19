# Chapter 10: Files and Exceptions

## Key Concepts

### Reading from a File
To work with a file, you first need to open it.

```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
```

- **`with` Keyword**: The `with` statement closes the file properly once access is no longer needed. Python closes it automatically, preventing memory leaks or file locks.
- **`open()`**: Returns a file object. If no path is specified, it looks in the directory where the program is running.
- **`read()`**: Reads the entire contents of the file. It adds an extra blank line at the end, which can be removed with `.rstrip()`.

#### Reading Line by Line
```python
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
```

#### Making a List of Lines from a File
```python
with open(filename) as file_object:
    lines = file_object.readlines()  # Returns a list of lines

for line in lines:
    print(line.rstrip())
```

### Writing to a File
To write, you must pass a second argument to `open()`.

- `'w'` **Write mode**: Overwrites the file if it already exists.
- `'r'` **Read mode** (default).
- `'a'` **Append mode**: Appends new data to the end of the file.
- `'r+'` **Read and write mode**.

```python
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
```

- `write()` does not add newlines automatically — you must add `\n` yourself.

### Exceptions
Python uses special objects called **exceptions** to manage errors that arise during program execution. If you write code that handles the exception, the program will continue running. If not, it halts.

Exceptions are handled with a `try-except-else-finally` block:

```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Division successful!")
```

- **`try`**: Code that might fail.
- **`except`**: Code to run if a specific exception occurs.
- **`else`**: Code to run if the `try` block succeeds without raising any exceptions.
- **`finally`**: Code that runs no matter what (useful for cleaning up resources).

#### Handling `FileNotFoundError`
```python
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
```

#### Failing Silently
If you don't want to report an exception to the user, you can use the `pass` statement in the `except` block.

```python
try:
    # some code
except FileNotFoundError:
    pass
```

### Storing Data with `json`
The `json` module allows you to serialize Python objects (lists, dicts) into JSON string files, and deserialize them back.

```python
import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'

# Save data
with open(filename, 'w') as f:
    json.dump(numbers, f)

# Load data
with open(filename, 'r') as f:
    loaded_numbers = json.load(f)
```

## Common Pitfalls
- **Relative Path Errors**: File path issues when running scripts from a different working directory. Use absolute paths or the `pathlib` module.
- **Missing File Modes**: Opening a file in `'w'` mode and accidentally wiping out existing contents. Use `'a'` to append.
- **Broad Exceptions**: Writing `except Exception:` or empty `except:` blocks. This catches *everything*, including syntax errors or system exits, making debugging extremely difficult. Catch specific exceptions.

## Try It Yourself
1. Create a text file, write a script to read it all at once, line by line, and store it in a list to print.
2. Write a program that prompts the user for their name. When they respond, write their name to a file called `guest.txt`.
3. Write a program that asks for two numbers, adds them, and prints the result. Catch `ValueError` exceptions if the user inputs text instead of numbers.
