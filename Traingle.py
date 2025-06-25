from rectangel import Rectangle

class Traingle(Rectangle):
    def __init__(self ,base,high,side2,side3):
        self.base=base
        self.high=high
        self.side2=side2
        self.side3=side3
        super().__init__(base,high)
    def get_area(self):
        return 0.5*(super().get_area())

    def get_perimeter(self):
        return  self.side2+self.side3+self.base

    def __str__(self):
        return f"Traingle: base={self.base}, height={self.high}, sides=({self.base},{self.side2},{self.side3}), area={self.get_area()}, perimeter={self.get_perimeter()}"

    def __repr__(self):
        return f"Traingle(base={self.base}, high={self.high}, side2={self.side2}, side3={self.side3})"
c=Traingle(5,7,7,7)
# print(c.get_perimeter())