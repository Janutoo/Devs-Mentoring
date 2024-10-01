### Zadanie 2: Klasy `Student` i `School`
#**Opis**:
#Stwórz klasę `Student`, która przechowuje imię, nazwisko i listę ocen ucznia.
#  Klasa `School` przechowuje listę uczniów i pozwala dodawać nowych uczniów,
#  dodawać oceny do ucznia, wyświetlać wszystkich uczniów i obliczać średnią ocen dla każdego ucznia.
#  Jeśli szkoła nie ma żadnych uczniów, wyświetl odpowiednią informację.
#**Przykład:**
'''python
>>> s1 = Student("Anna", "Kowalska")
>>> s1.dodaj_ocene(5)
>>> s1.dodaj_ocene(4)
>>> s2 = Student("Jan", "Nowak")
>>> s2.dodaj_ocene(3)
>>> s2.dodaj_ocene(5)
>>> school = School()
>>> school.dodaj_ucznia(s1)
>>> school.dodaj_ucznia(s2)
>>> school.wyswietl_uczniow()
Uczniowie:
Anna Kowalska: oceny [5, 4], średnia 4.5
Jan Nowak: oceny [3, 5], średnia 4.0
'''
def srednia(zbior_liczb):
    return sum(zbior_liczb)/len(zbior_liczb)
        
class Student:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = []
    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)
    def __repr__(self):
        return f"{self.imie} {self.nazwisko}, Oceny: {self.oceny}, SREDNIA: {srednia(self.oceny)}"
    
class School:
    def __init__(self):
        self.lista_uczniow = []

    def dodaj_ucznia(self, uczen):
        if uczen in self.lista_uczniow:
            print("ten uczen jest juz w liscie")
        else:
            self.lista_uczniow.append(uczen)
    def wyswietl_uczniow(self):
        for x in self.lista_uczniow:
            print(x)

s1 = Student("Anna", "Kowalska")
s1.dodaj_ocene(5)
s1.dodaj_ocene(4)
s2 = Student("Jan", "Nowak")
s2.dodaj_ocene(3)
s2.dodaj_ocene(5)
school = School()
school.dodaj_ucznia(s1)
school.dodaj_ucznia(s2)
school.wyswietl_uczniow()