# Zadanie 5: Klasy Appliance i WashingMachine
# Opis:
# Napisz klasę Appliance, która będzie miała metodę turn_on() wypisującą “Uruchomiono urządzenie”. 
# Utwórz podklasę WashingMachine i nadpisz metodę turn_on(), aby wypisywała “Uruchomiono pralkę”.
# Przykład:
# >>> appliance = Appliance()
# >>> washing_machine = WashingMachine()
# >>> appliance.turn_on()
# Uruchomiono urządzenie
# >>> washing_machine.turn_on()
# Uruchomiono pralkę

class Appliance:
    def turn_on(self):
        print("Uruchomiono urządzenie")

class WashingMachine(Appliance):
    def turn_on(self):
        print("Uruchomiono pralkę")