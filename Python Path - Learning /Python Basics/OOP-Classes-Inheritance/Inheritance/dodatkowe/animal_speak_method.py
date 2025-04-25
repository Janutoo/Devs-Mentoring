# Zadanie 1: Klasy Animal i Dog
# Opis:
# Utwórz klasę Animal, która ma metodę speak() zwracającą tekst “Nieznany dźwięk”. 
# Następnie utwórz klasę Dog, która dziedziczy po Animal i nadpisuje metodę speak() tak, aby zwracała tekst “Woof!”. 
# Klasa Dog powinna także mieć dodatkowy atrybut breed (rasa psa).
# Przykład:
# >>> animal = Animal()
# >>> dog = Dog("Labrador")
# >>> print(animal.speak())
# Nieznany dźwięk
# >>> print(dog.speak())
# Woof!
# >>> print(dog.breed)
# Labrador


class Animal:
    def speak(self):
        return "Nieznany dźwięk"

class Dog(Animal):
    def __init__(self, breed):
        self.breed = breed

    def speak(self):
        return "Woof!"