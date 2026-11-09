# error handling is particularly useful in preventing crash of a program when errors are encountered, they provide directions to follow on what to do when an error is encountered, and they also help in debugging the code, by providing information on what went wrong and where it went wrong

# we can ue  try, except, else, finally to handle errors in python, 
# the try block is used to wrap the code that may raise an exception, 
# the except block is used to handle the exception, 
# the else block is used to execute code that should run if no exception was raised, 
# and the finally block is used to execute code that should run regardless of whether an exception was raised or not

import json


try:
    input = int(input("Enter a number: "))
except ValueError:
    print("invalid input. please enter a valid number")

# import pathlib if the json file path is not available in the programs directory
try:
    with open("file_name.json", 'r') as unloaded_file:
        loaded_file = json.load(unloaded_file)

except FileNotFoundError: #raised when the file isnt found
    print("file not found")

except json.JSONDecodeError:
    print("the json file is invalid, perhaps due to syntax errors")

except PermissionError:
    print("u dont have permission to edit/read file")


# for multiple errors being handled by one code line
data = {"a":1, "b":2, "c":3, "d":4, "e":5}
try:
    with open("file_name.json", 'w') as selected_file:
        to_write_to = json.dump(data, selected_file, indent = 4)

except (PermissionError, FileNotFoundError, json.JSONDecodeError, ValueError, ):
    print("error uncovered mid run")

else:
    print("json was written without error")

finally:
    (exit())

# other actions can be taken in the except, else, and finally blocks other than print or exit