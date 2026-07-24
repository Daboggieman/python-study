# OOP Exercise 06: Polymorphism
# Run this script with: python exercises.py


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement speak()")

    def describe(self):
        return f"I am {self.name}"


# TODO: Exercise 1 - Dog overrides speak()
class Dog(Animal):
    def speak(self):
        pass


# TODO: Exercise 1 - Cat overrides speak()
class Cat(Animal):
    def speak(self):
        pass


# TODO: Exercise 2 - Bird overrides speak() too
class Bird(Animal):
    def speak(self):
        pass


# TODO: Exercise 3 - Robot has NO shared parent with Animal, but has its own speak()
class Robot:
    def speak(self):
        pass


# TODO: Exercise 4 - Dog extends Animal's describe() using super()
class DescriptiveDog(Animal):
    def describe(self):
        pass


if __name__ == "__main__":
    animals = [Dog("Rex"), Cat("Whiskers"), Bird("Tweety")]
    for animal in animals:
        print(animal.speak())

    everything = [Dog("Fido"), Robot()]
    for thing in everything:
        print(thing.speak())    # works via duck typing, no shared parent needed

    print(DescriptiveDog("Rex").describe())   # I am Rex, a good dog
