# Exercise 10: Files & Exceptions
# Run this script with: python exercises.py

# TODO: Exercise 1
# Create a text file named 'learning.txt' inside this directory with three lines:
# "I am learning Python."
# "I am learning file handling."
# "I am learning exception handling."
# Then write code below that reads this file and prints the content all at once.


# TODO: Exercise 2
# Write code that appends a fourth line: "I am learning to write code." to 'learning.txt'.
# Then read the file line by line, printing each line stripped of extra whitespace.


# TODO: Exercise 3
# Write a try-except block that attempts to open a non-existent file named 'missing.txt'.
# Handle the FileNotFoundError by printing "The file could not be found." instead of crashing.


# TODO: Exercise 4
# Given the dictionary 'config' below, write it to a file named 'config.json' in JSON format.
# Then load it back and print the loaded dictionary.
import json
config = {"theme": "dark", "volume": 80, "debug_mode": True}

