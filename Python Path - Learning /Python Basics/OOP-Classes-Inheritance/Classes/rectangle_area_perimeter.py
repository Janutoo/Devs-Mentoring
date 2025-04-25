class Prostokąt:
    def __init__(self, szerokość, długość):
        self.szerokość = szerokość
        self.długość = długość

    def pole(self):
        return self.szerokość * self.długość

    def obwód(self):
        return 2 * (self.szerokość + self.długość)

# Przykład użycia
prostokąt = Prostokąt(5, 10)
print(f'Pole prostokąta: {prostokąt.pole()}')  
print(f'Obwód prostokąta: {prostokąt.obwód()}')  
