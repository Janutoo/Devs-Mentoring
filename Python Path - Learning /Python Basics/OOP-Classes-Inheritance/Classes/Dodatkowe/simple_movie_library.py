'''## Zadanie 4: Klasy `Movie` i `MovieCollection`
**Opis**:
Stwórz klasę `Movie`, która przechowuje tytuł, reżysera i rok produkcji filmu. Klasa `MovieCollection` przechowuje listę filmów
i umożliwia dodawanie nowych filmów, wyświetlanie wszystkich filmów, wyszukiwanie filmów po tytule oraz usuwanie filmów z kolekcji.
**Przykład:**
```python
>>> m1 = Movie("Inception", "Christopher Nolan", 2010)
>>> m2 = Movie("The Matrix", "The Wachowskis", 1999)
>>> collection = MovieCollection()
>>> collection.dodaj_film(m1)
>>> collection.dodaj_film(m2)
>>> collection.wyswietl_filmy()
Filmy w kolekcji:
"Inception" - Reżyser: Christopher Nolan, Rok: 2010
"The Matrix" - Reżyser: The Wachowskis, Rok: 1999
>>> collection.szukaj_filmu("Inception")
Znaleziono film: "Inception" - Reżyser: Christopher Nolan, Rok: 2010
>>> collection.usun_film("The Matrix")
>>> collection.wyswietl_filmy()
Filmy w kolekcji:
"Inception" - Reżyser: Christopher Nolan, Rok: 2010
```'''
class Movie:
    def __init__(self, tytul, rezyser, rok_produkcji):
        self.tytul = tytul 
        self.rezyser = rezyser
        self.rok_produkcji = rok_produkcji
    def __repr__(self):
        return f"{self.tytul} - Rezyser: {self.rezyser}, Rok: {self.rok_produkcji}"

class MovieCollection:
    def __init__(self):
         self.listafilmow = []
    def dodaj_film(self, film):
        self.listafilmow.append(film)
    def usun_film(self,szukaj):
        for i in self.listafilmow:
            if i.tytul == szukaj:
                self.listafilmow.remove(i)
    def wyswietl_filmy(self):
        for i in self.listafilmow:
            print(i)
    def szukaj_filmu(self, szukaj):
        for i in self.listafilmow:
            if i.tytul == szukaj:
                print(i)


m1 = Movie("Inception", "Christopher Nolan", 2010)
m2 = Movie("The Matrix", "The Wachowskis", 1999)
collection = MovieCollection()
collection.dodaj_film(m1)
collection.dodaj_film(m2)
collection.wyswietl_filmy()
collection.szukaj_filmu("Inception")
collection.usun_film("The Matrix")
collection.wyswietl_filmy()

