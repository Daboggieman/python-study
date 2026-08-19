# OOP Exercise 05: Class Methods and Static Methods
# Run this script with: python exercises.py


class Dog:
    population = 0

    def __init__(self, name, age):
        if not Dog.is_valid_age(age):
            raise ValueError("invalid age")
        self.name = name
        self.age = age
        Dog.population += 1

    # TODO: Exercise 1 - alternative constructor from a birth year
    @classmethod
    def from_birth_year(cls, name, birth_year, current_year=2026):
        pass

    # TODO: Exercise 2
    @classmethod
    def get_population(cls):
        pass

    # TODO: Exercise 3 - static method, no self/cls needed
    @staticmethod
    def is_valid_age(age):
        pass


if __name__ == "__main__":
    rex = Dog.from_birth_year("Rex", 2022)
    fido = Dog("Fido", 1)
    print(rex.age)                    # 4
    print(Dog.get_population())        # 2

    try:
        Dog("Bad", -5)
    except ValueError as e:
        print("Correctly rejected:", e)
