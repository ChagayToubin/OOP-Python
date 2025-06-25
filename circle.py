from rectangel import Rectangle
from math import pi


class Circle(Rectangle):
    def __init__(self,redios):
        self.redios=redios

        super().__init__(redios,pi)
    def get_area(self):
        return (self.redios^2)*pi
    def get_perimeter(self):
        return super().get_area()*2