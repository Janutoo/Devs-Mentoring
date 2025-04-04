# Stwórz klasę abstrakcyjną Shape z metodą abstrakcyjną area(). Zaimplementuj klasy potomne:
# •	Circle – pole powierzchni koła.
# •	Square – pole powierzchni kwadratu.
# •	Triangle – pole powierzchni trójkąta.
# Wykorzystaj polimorfizm, tworząc listę różnych kształtów i obliczając ich łączne pole powierzchni.
import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Circle(5),
    Square(4),
    Triangle(3, 6),
    Circle(2),
    Square(7)
]


total_area = sum(shape.area() for shape in shapes)
print(total_area)