class Rectangle:
    def __init__(self, width, lenght):
        self.lenght = height
        self.width = width
        self._area = area[]

        if self.lenght <= 0:
            raise ValueError("A dimension of the Rectangle cannot be ZERO(0) or have a negative value (-x)") 
        if self.width <= 0:
            raise ValueError("A dimension of the Rectangle cannot be ZERO(0) or have a negative value (-x)") 
        if self.lenght == self.width:
            raise ValueError("values given are dimensions for a square, NOT a rectangle")

    def area(self):
        return (self.lenght) * (self.width)

    def perimeter(self):
        return 2 * ((self.lenght) * (self.width))

