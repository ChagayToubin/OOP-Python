# rect.py
from Shape import Shape

class Rectangle(Shape):
    def __init__(self, width, high):
        self.width = width
        self.high = high

    def get_area(self):
        return self.width * self.high

