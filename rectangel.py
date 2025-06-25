# rect.py
from Shape import Shape

class Rectangle(Shape):
    def __init__(self, width, high):
        self.width = width
        self.high = high

    def get_area(self):
        return self.width * self.high

    def get_perimeter(self):
        return (self.width + self.high) * 2

    def __str__(self):
        return f"Rectangle: width={self.width}, height={self.high}, area={self.get_area()}, perimeter={self.get_perimeter()}"

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.high})"

    def __add__(self, other):
        return self.get_area()+other.get_area()
    def __eq__(self, other):
        return other.get_area==self.get_area()
    def __sub__(self, other):
        return self.get_area()-other.get_area()
