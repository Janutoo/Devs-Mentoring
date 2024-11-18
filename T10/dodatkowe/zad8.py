# Opis:
# Stwórz klasę bazową Animal z atrybutem species (gatunek) i metodą sound() zwracającą “Brak dźwięku”.
#  Utwórz podklasę Cat, która nadpisuje metodę sound() tak, aby zwracała “Meow”.
# Przykład:
# >>> animal = Animal()
# >>> cat = Cat()
# >>> print(animal.sound())
# Brak dźwięku
# >>> print(cat.sound())
# Meow

   
class Animal:
    def __init__(self, species):
        self.species = species

    def sound(self):
        return "Brak dźwięku"

class Cat(Animal):
    def sound(self):
        return "Meow"