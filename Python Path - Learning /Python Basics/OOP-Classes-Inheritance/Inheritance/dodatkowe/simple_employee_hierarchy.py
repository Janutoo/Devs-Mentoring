# Zadanie 7: Klasy Device i Computer
# Opis:
# Stwórz klasę Device z metodą power_on() wypisującą “Uruchamianie urządzenia”.
#  Utwórz podklasę Computer, która dodaje metodę boot_up() wypisującą “Komputer się uruchamia”.
#  Wywołaj obie metody dla obiektu klasy Computer.
# Przykład:
# >>> device = Device()
# >>> computer = Computer()
# >>> computer.power_on()
# Uruchamianie urządzenia
# >>> computer.boot_up()
# Komputer się uruchamia


class Device:
    def power_on(self):
        print("Uruchamianie urządzenia")

class Computer(Device):
    def boot_up(self):
        print("Komputer uruchamia")