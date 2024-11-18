class Shape:
    def area(self):  
        return 0

class Square(Shape):
    def __init__(self, length):
        # Przekazujemy długość boku kwadratu
        self.length = length
    
    def area(self):

        return self.length ** 2


shape = Shape()
square = Square(5)

print("Pole Shape:", shape.area())  # Wynik: 0
print("Pole Square:", square.area())  # Wynik: 25