from rectangel import Rectangle
import math

class Hexagon(Rectangle):
    def __init__(self,side):
        self.side=side
        super().__init__(side,side)
    def get_area(self):
        return  (3*(math.sqrt(3))/2)* super().get_area()
    def get_perimeter(self):
        return  self.side*6

