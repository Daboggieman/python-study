# Exercise 12b: Standard Library Modules
# Run this script with: python exercises.py

import os
import math
import json
from datetime import datetime

# TODO: Exercise 1
# Print the current working directory and the list of files in it.
print("CWD:", os.getcwd())
print("Files:", os.listdir("."))

# TODO: Exercise 2
# Calculate the length of the hypotenuse for sides 3 and 4.
print(math.hypot(3, 4))

# TODO: Exercise 3
# Convert a dictionary into a JSON string and print it.
person = {"name": "Sam", "age": 28}
print(json.dumps(person))

# TODO: Exercise 4
# Print the current date and time.
print(datetime.now())
