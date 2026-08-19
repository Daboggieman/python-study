# Exercise 10b: File Access, Reading, and Writing
# Run this script with: python exercises.py

import os

# TODO: Exercise 1
# Create or overwrite a file named sample.txt and write two lines of text.
with open("sample.txt", "w") as file:
    file.write("Line one\n")
    file.write("Line two\n")

# TODO: Exercise 2
# Read sample.txt and print each line without extra blank lines.
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())

# TODO: Exercise 3
# Check if sample.txt exists, then remove it.
print(os.path.exists("sample.txt"))
os.remove("sample.txt")
print(os.path.exists("sample.txt"))
