# Exercise 04: Lists & Tuples
# Run this script with: python exercises.py

# TODO: Exercise 1
# Create a list called 'colors' containing: "red", "green", "blue".
# Add "yellow" to the end of the list.
# Insert "orange" at index 1.
# Print the final list.
colors = ["red", "green","blue"]
colors.append("yellow")
colors.insert(1, "orange")
print(colors)


# TODO: Exercise 2
# Given the list 'numbers' below, sort it permanently in descending order and print it.
numbers = [42, 7, 19, 99, 1]
numbers.sort()
numbers.reverse()
print(numbers)

# TODO: Exercise 3
# Create a tuple named 'point' representing 3D coordinates: x=10, y=20, z=30.
# Unpack the tuple into three variables: px, py, pz.
# Print px, py, and pz.

point = ("x=10", "y=20", "z=30")
x, y, z = point

print(x)
print(y)
print(z)

# color_grade
navy_blue = (5, 0, 128)

red, green, blue = navy_blue

print(f"the RGB color palette value of NAVY-BLUE is \n > red = {red}\n > green ={green} \n > blue = {blue}")

# TODO: Exercise 4
# Demonstrate the difference between sort() and sorted() on the list below.
# Print the temporarily sorted version, print the original list to show it hasn't changed,
# then run sort() and print the list to show the permanent change.
grades = [88, 72, 95, 60]

