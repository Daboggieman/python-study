class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        # self._area = area[]   #there is no need ffor this since the class already has a function that calculates area, just return the area from that value and save to output.json

        if self.height <= 0:
            raise ValueError("A dimension of the Rectangle cannot be ZERO(0) or have a negative value (-x)") 
        if self.width <= 0:
            raise ValueError("A dimension of the Rectangle cannot be ZERO(0) or have a negative value (-x)") 
        if self.height == self.width:
            # return self.side = self.width
            raise ValueError("values given are dimensions for a square, NOT a rectangle")

    def area(self):
        return (self.height) * (self.width)

    def perimeter(self):
        return 2 * ((self.height) + (self.width))

    def describe(self):
        return f'"Rectangle {self.width}x{self.height}"'

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * 2

    def perimeter(self):
        return 2 * (self.side + self.side)


def add_to_json(filepath, record):
    pass # addd the json append function when needed


r = Rectangle(4, 5)
print(r.area(), r.perimeter(), r.describe())

s = Square(4)

print(s.area(), s.perimeter())
print(isinstance(s, Rectangle))
