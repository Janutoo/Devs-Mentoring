# Utwórz klasę Shape z metodą area() zwracającą 0. 
# Następnie utwórz klasę Circle, która dziedziczy po klasie Shape i dodaj atrybut radius (promień). 
# Nadpisz metodę area() tak, aby obliczała pole koła.
# Przykład:
# >>> shape = Shape()
# >>> circle = Circle(5)
# >>> print(shape.area())
# 0
# >>> print(circle.area())
# 78.5  # Przyjmując pi ~ 3.14

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

