# OOP Exercise 02: The __init__ Method
# Run this script with: python exercises.py


# TODO: Exercise 1 & 2
# Define a Car class with __init__(self, make, model, year=2024, mileage=0)
class Car:
    pass


# TODO: Exercise 4
# Add a drive(self, miles) method that increases self.mileage


if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Honda", "Civic")             # uses default year
    print(car1.year, car2.year)                # 2020 2024

    car1.drive(50)
    car1.drive(100)
    print(car1.mileage)                          # 150
