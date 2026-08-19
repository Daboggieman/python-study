# Chapter 9: Classes

## Key Concepts

### Creating and Using a Class
Object-oriented programming (OOP) is one of the most effective approaches to writing software. In OOP, you write **classes** that represent real-world things or situations, and create **objects** (instances) based on these classes.

```python
class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
```

- **`__init__()` Method**: A special method Python runs automatically whenever we create a new instance based on the class. The double underscores indicate it is a special/dunder method.
- **`self` Parameter**: Required in method definitions and must come first. It represents the specific instance being created/called, giving the object access to the attributes and methods in the class.
- **Attributes**: Variables prefixed with `self` (e.g., `self.name`, `self.age`) are attributes.

### Creating an Instance of a Class
```python
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
```

### Working with Classes and Instances

#### Setting a Default Value for an Attribute
Attributes can be defined with default values in `__init__()`. You don't have to pass an argument for them.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Default value
```

#### Modifying Attribute Values
1. **Directly**: `my_car.odometer_reading = 23`
2. **Through a Method**:
```python
def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
        self.odometer_reading = mileage
    else:
        print("You can't roll back an odometer!")
```
3. **Incrementing through a method**:
```python
def increment_odometer(self, miles):
    self.odometer_reading += miles
```

### Inheritance
If the class you're writing is a specialized version of another class, you can use **inheritance**. The original class is the **parent class** (or superclass), and the new class is the **child class** (or subclass).

```python
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 40  # Child-specific attribute
```

- **`super()` Function**: A helper function that calls parent methods, letting you initialize parent attributes inside a child class.
- **Overriding Parent Methods**: To override, define a method in the child class with the exact same name as the method in the parent class.

### Instances as Attributes (Composition)
You can break a large class into smaller classes and use instances of those classes as attributes in the larger class.

```python
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  # Instance as attribute
```

### Importing Classes
Just like functions, you can store your classes in modules and import them:

```python
from car import Car
from car import Car, ElectricCar
import car
from car import *  # Discouraged
```

## Common Pitfalls
- **Forgetting `self`**: Forgetting `self` as the first argument in class methods or when referencing attributes (`name` instead of `self.name`).
- **Mutable Class Attributes**: Defining list or dict class attributes outside `__init__()`. They will be shared across *all* instances of the class! Always initialize mutable attributes inside `__init__()`.
- **Naming Conflicts**: Importing multiple modules that contain classes with duplicate names.

## Try It Yourself
1. Make a class called `Restaurant` with `restaurant_name` and `cuisine_type`. Create an instance, print the attributes, and call the methods.
2. Make a class called `User` with user attributes, `describe_user()`, and `greet_user()`.
3. Create an `Admin` class that inherits from `User`. Add a list of privileges as an attribute and a method to print them.
