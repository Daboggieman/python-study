# OOP Exercise 01: Classes and Objects
# Run this script with: python exercises.py


# TODO: Exercise 1
# Define an empty Car class.
class Car:
    pass


# TODO: Exercise 2
# Add a `honk` method that prints "Beep beep!"


if __name__ == "__main__":
    car1 = Car()
    car2 = Car()
    print(car1 is car2)   # False

    car1.make = "Toyota"
    car1.model = "Corolla"
    car1.year = 2020
    print(f"{car1.year} {car1.make} {car1.model}")

    car1.honk()   # Beep beep!

    print(type(3.14))   # <class 'float'>
    print(type(True))    # <class 'bool'>
    print(type(None))    # <class 'NoneType'>
