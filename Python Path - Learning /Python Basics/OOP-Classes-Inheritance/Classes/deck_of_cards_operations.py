import random

class Card:
    def __init__(self, wartość, figura):
        self.wartość = wartość
        self.figura = figura

    def __repr__(self):
        return f"{self.wartość} of {self.figura}"

class Deck:
    def __init__(self):
        figury = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        wartości = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.karty = [Card(wartość, figura) for figura in figury for wartość in wartości]
    
    def shuffle(self):
        random.shuffle(self.karty)
    
    def deal(self):
        if self.karty:
            return self.karty.pop()
        else:
            raise IndexError("Brak kart w talii")

# Przykład użycia
talia = Deck()
print(f'Talia przed tasowaniem: {talia.karty[:5]}')  
talia.shuffle()
print(f'Talia po tasowaniu: {talia.karty[:5]}')  

karta = talia.deal()
print(f'Rozdana karta: {karta}') 
print(f'Talia po rozdaniu: {talia.karty[:5]}')  