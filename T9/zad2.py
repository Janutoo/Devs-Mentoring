# Zad. 2
# Stwórz klasę reprezentującą pojazd. 
# Dodaj do niej pola określające maksymalną prędkość obiektu oraz
#  jego przebieg. Dodaj do klasy metodę, która zwiększać będzie wartość 
# pola przebiegu o przesłaną wartość typu float.

class Pojazd:
    def __init__(self, przebieg, maxSpeed):
        self.maxSpeed = maxSpeed
        self.przebieg = przebieg
    
    def zwiekszPrzebieg(self, dystans):
        if dystans > 0:
            self.przebieg += dystans
        else:
            print("Dystans musi byc wiekszy niz zero")

    def wyswietlInformacjeOPojezdzie(self):
        print(f"Przebieg: {self.przebieg}")
        print(f"Maksymalna predkość: {self.maxSpeed}")