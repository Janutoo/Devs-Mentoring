# Zadanie 2: Klasy Vehicle i Car
# Opis:
# Stwórz klasę Vehicle z atrybutem speed (szybkość).
# Następnie utwórz klasę Car, która dziedziczy po klasie Vehicle i dodaj do niej atrybut brand (marka samochodu).
# Dodaj metodę w klasie Car, która wyświetli markę i prędkość samochodu.
# Przykład:
# >>> v = Vehicle(60)
# >>> car = Car(120, "Toyota")
# >>> print(car.brand)
# Toyota
# >>> print(car.speed)
# 120 km/h


class Vehicle:
    def __init__(self, speed):
        self.speed = speed

class Car(Vehicle):
    def __init__(self, speed, marka):
        super().__init__(speed)
        self.marka = marka

    