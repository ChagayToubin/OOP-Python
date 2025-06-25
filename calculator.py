from Square import Square
from rectangel import Rectangle
from Traingle import Traingle
from circle import Circle
from Hexagon import Hexagon

def main():
    shapes = [ Square(5),Rectangle(4, 6),Traingle(4, 3,4,5),Circle(3),Hexagon(2)]


    for S in shapes:
        print(f"{S.__class__.__name__} area: {S.get_area()} primeter:{S.get_perimeter()}")


    s=shapes[4]+shapes[0]

    print(s)

    print(shapes[1]==shapes[2])

    print(shapes[1]-shapes[2])




if __name__ == "__main__":
    main()


