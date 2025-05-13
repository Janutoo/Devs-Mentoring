#**Opis**:
#Utwórz klasę `Book`, która przechowuje tytuł, autora i liczbę stron książki. Klasa `Library` przechowuje listę książek i umożliwia dodawanie nowych książek, wyświetlanie wszystkich książek oraz zliczanie ich liczby. Jeśli w bibliotece nie ma książek, należy wyświetlić odpowiednią informację.
#**Przykład:**
#```python
#>>> b1 = Book("Python 101", "John Doe", 150)
#>>> b2 = Book("Learning Java", "Jane Doe", 200)
#>>> lib = Library()
#>>> lib.dodaj_ksiazke(b1)
#>>> lib.dodaj_ksiazke(b2)
#>>> lib.wyswietl_ksiazki()
#Masz takie książki:
"Python 101" #autorstwa John Doe, 150 stron.
"Learning Java" #autorstwa Jane Doe, 200 stron.
#>>> print(lib.ile_ksiazek())

class Book:
    def __init__(self, tytul, strony, autor):
        self.tytul = tytul
        self.strony = strony 
        self.autor = autor
    def __repr__(self):
        return f"{self.tytul} (strony: {self.strony}, autor: {self.autor})"

class Library:
    def __init__(self):
        self.ksiazki = {}
    def nowa_ksiazka(self, nowa):
        if isinstance(nowa, Book):
            if nowa in self.ksiazki:
                self.ksiazki[nowa] += 1
            else:
                self.ksiazki[nowa] = 1
    def pokaz_ksiazki(self):
        print(self.ksiazki)
        if len(self.ksiazki) == 0:
            print("nie ma ksiazek ez")
        else:
            for key, value in self.ksiazki.items():
                print(str(key) + " ilość: " + str(value))
    def ile_ksiazek(self):
        ile = 0
        for value in self.ksiazki.values():
            ile += value 
        return ile



b1 = Book("niger", 103,"datos")

b2 = Book("dis",123,"smiec")

l1 = Library()

l1.nowa_ksiazka(b1)
l1.nowa_ksiazka(b1)
l1.nowa_ksiazka(b2)
    
l1.pokaz_ksiazki()

l2 = Library()
l2.pokaz_ksiazki()

print(l1.ile_ksiazek())


a = {"a": 20, "b": 40}

for key, value in a.items():
    print(key, value)