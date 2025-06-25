from rectangel import Rectangle
class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square: side={self.width}, area={self.get_area()}, perimeter={self.get_perimeter()}"

    def __repr__(self):
        return f"Square(side={self.width})"

