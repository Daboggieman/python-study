# OOP Exercise 01: Classes and Objects
# Run this script with: python3 exercises.py
#
# Work top to bottom. Each exercise maps to a Part of lecture.md, noted in
# brackets. Once Exercise 1 is done the file runs end to end -- the remaining
# unfinished exercises just print nothing, so run it often to track progress.


# TODO: Exercise 1  [lecture Part 1.2 - 1.3]
# Define an empty Car class. Use `pass` for the body for now.
# Then look at the __main__ block below: it creates two Cars and checks
# that they are separate objects.


# TODO: Exercise 2  [lecture Part 2.1]
# Nothing to write in this section -- the __main__ block attaches
# `make`, `model` and `year` directly to car1 and prints them.
# Read it and make sure you can say what each line does.


# TODO: Exercise 3  [lecture Part 3.1]
# Add a `honk` method to Car that prints exactly: Beep beep!
# Remember the `self` first parameter.


# TODO: Exercise 4  [lecture Part 3.2 - 3.3]
# Add a `describe` method that uses self to print "<year> <make> <model>",
# e.g. "2020 Toyota Corolla".
# The __main__ block calls it BOTH ways -- car1.describe() and
# Car.describe(car1) -- to prove they are the same thing.


# TODO: Exercise 5  [lecture Part 2.4]
# The __main__ block deliberately calls describe() on a car with no
# attributes attached, and catches the error. Run it, read the message,
# then replace this comment with one line explaining what Lesson 02
# (__init__) will do to make this impossible:
#
# YOUR ANSWER:


if __name__ == "__main__":
    # --- Exercise 1: two objects are genuinely separate [Part 1.3] ---
    car1 = Car()
    car2 = Car()
    print("car1 is car2 ->", car1 is car2)      # expect: False
    print("car1 is car1 ->", car1 is car1)      # expect: True

    # --- Exercise 2: attach attributes by hand [Part 2.1] ---
    car1.make = "Toyota"
    car1.model = "Corolla"
    car1.year = 2020
    print(f"{car1.year} {car1.make} {car1.model}")   # expect: 2020 Toyota Corolla

    # --- Exercise 3: a method [Part 3.1] ---
    car1.honk()                                  # expect: Beep beep!

    # --- Exercise 4: self, and the two equivalent call forms [Part 3.3] ---
    car1.describe()                              # expect: 2020 Toyota Corolla
    Car.describe(car1)                           # expect: the exact same line

    # --- Exercise 5: why hand-attaching is fragile [Part 2.4] ---
    car3 = Car()                                 # no attributes attached
    try:
        car3.describe()
    except AttributeError as e:
        print("AttributeError ->", e)            # read this message carefully

    # --- Exercise 6: everything is already an object [Part 5] ---
    print(type(3.14))      # <class 'float'>
    print(type(True))      # <class 'bool'>
    print(type(None))      # <class 'NoneType'>
    print(type(print))     # <class 'builtin_function_or_method'>
    print(type(Car))       # <class 'type'>  -- the class is an object too
