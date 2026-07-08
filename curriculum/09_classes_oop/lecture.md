# Lecture 09: Classes & OOP

Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around data, or objects, rather than functions and logic. An object can be defined as a data field that has unique attributes and behavior.

---

## 1. What is a Class?
A **class** is a blueprint or template for creating objects. An **object** is an instance of a class.

```python
class Dog:
    """A simple class representing a dog."""
    
    def __init__(self, name, breed):
        """Constructor: Initializes name and breed attributes."""
        self.name = name
        self.breed = breed
        
    def bark(self):
        """A simple method."""
        return f"{self.name} says Woof!"
```

- **`__init__`**: The special constructor method called automatically when creating a new instance.
- **`self`**: A reference to the current instance of the class. It is used to access class attributes and methods.
- **Attributes**: Variables bound to a class or instance (e.g., `self.name`).
- **Methods**: Functions defined inside a class.

### Creating an Instance:
```python
my_dog = Dog("Rex", "German Shepherd")
print(my_dog.name)  # Access attribute: Rex
print(my_dog.bark())  # Call method: Rex says Woof!
```

---

## 2. Modifying Attribute Values
You can modify instance attributes directly, or write helper methods to update them:

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.odometer = 0  # Default value
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You cannot roll back an odometer!")
```

---

## 3. Inheritance
Inheritance allows a new class (child class) to inherit attributes and methods from an existing class (parent class). Use the `super()` function to call the parent constructor.

```python
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, battery_size=75):
        """Initialize attributes of the parent class."""
        super().__init__(make, model)
        self.battery_size = battery_size
        
    def charge(self):
        return "Charging the battery..."
```

---

## 4. Overriding Methods
A child class can redefine a method from the parent class to customize its behavior.

```python
class ElectricCar(Car):
    # ...
    def update_odometer(self, mileage):
        # Custom logic or override behavior entirely
        print("Updating electric odometer...")
        super().update_odometer(mileage)
```

---

## 🧠 Try It Yourself
1. Create a class called `Restaurant` with two attributes: `restaurant_name` and `cuisine_type`. Add a method `describe_restaurant()` that prints these two pieces of information, and a method `open_restaurant()` that prints a message indicating the restaurant is open. Create an instance and test them.
2. Create an `IceCreamStand` class that inherits from `Restaurant`. Add an attribute called `flavors` that stores a list of ice cream flavors. Write a method that displays these flavors.
