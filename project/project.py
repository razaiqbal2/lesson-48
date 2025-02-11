import math


class Polygon:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method.")


class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height


class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

def main():
    triangle = Triangle(5, 10)
    rectangle = Rectangle(4, 6)
    circle = Circle(7)
    square = Square(4)
    
    print(f"Area of the triangle: {triangle.area()} square units")
    print(f"Area of the rectangle: {rectangle.area()} square units")
    print(f"Area of the circle: {circle.area()} square units")
    print(f"Area of the square: {square.area()} square units")

if __name__ == "__main__":
    main()
