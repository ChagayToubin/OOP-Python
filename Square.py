from rectangel import Rectangle
class Square(Rectangle):
    def __init__(self,side):
        self.side=side
        super().__init__(side, side)


