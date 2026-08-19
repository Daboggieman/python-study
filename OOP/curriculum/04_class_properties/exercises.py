# OOP Exercise 04: Class Properties (Attributes)
# Run this script with: python exercises.py


class Dog:
    species = "Canis familiaris"   # class attribute
    population = 0                    # class attribute used as a counter

    def __init__(self, name):
        self.name = name              # instance attribute
        # TODO: Exercise 2 - increment Dog.population here


class Circle:
    def __init__(self, radius):
        self._radius = radius

    # TODO: Exercise 3 - radius property (getter)
    @property
    def radius(self):
        pass

    # TODO: Exercise 3 - radius property (setter, must reject negative values)
    @radius.setter
    def radius(self, value):
        pass

    # TODO: Exercise 3 - read-only area property
    @property
    def area(self):
        pass


if __name__ == "__main__":
    rex = Dog("Rex")
    fido = Dog("Fido")
    print(Dog.population)   # 2

    c = Circle(5)
    print(c.radius, round(c.area, 2))   # 5 78.54
    c.radius = 10
    print(c.radius, round(c.area, 2))   # 10 314.16
    try:
        c.radius = -3
    except ValueError as e:
        print("Correctly rejected:", e)
