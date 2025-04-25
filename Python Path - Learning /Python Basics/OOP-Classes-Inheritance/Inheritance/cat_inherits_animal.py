# Wprowadzenie do dziedziczenia

#  Metody specjalne __init__, __str__, __add__: https://ufkapano.github.io/algorytmy/lekcja06/metody2.html
# class Zwierze:
#     def __init__(self, gatunek):
#         self.gatuenk = gatunek
    
#     def daj_glos(self):
#         print(f"{self.gatuenk} wydaje dzwiek")

# class Pies(Zwierze):
#     def daj_glos(self):
#         print(f"{self.gatuenk} szczekanie")
        
    
# def main():
#     pies = Pies("Pies")
#     pies.daj_glos()

# if __name__ == "__main__":
#     main()


# class Pojazd:
#     def __init__(self, marka):
#         self.marka = marka
    
#     def ruszaj(self):
#         print(f"Pojazd o marce {self.marka} rusza")

# class Samochod(Pojazd):
#     def ruszaj(self):
#         print(f"Samochód rusza o marce {self.marka}")
        
# def main():
#     samochod = Samochod("toyota")
#     print(samochod.marka)
#     samochod.ruszaj()

# if __name__ == "__main__":
#     main()


# class Wielokat:
#     def __init__(self, boki, sumakatow):
#         self.boki = boki
#         self.sumakatow = sumakatow 
    
#     def obliczObwod(self):
#         return sum(self.boki)
    
#     def wyswietlSumeKatow(self):
#         print(f"Suma katow {self.sumakatow}")

# class Trojakt(Wielokat):
#     def __init__(self, boki):
#         self.boki = boki
#         super().__init__(boki, 180)
    
#     def obliczPoleTrojkata(self):
#         return 0.5 * self.boki[0] * self.boki[1]

# def main():
#     trojkat = Trojakt([3, 4, 5])
#     print(trojkat.obliczObwod())
#     trojkat.wyswietlSumeKatow()
#     print(trojkat.obliczPoleTrojkata())

# if __name__ == "__main__":
#     main()


# class Rodzic:
#     def __init__(self, imie):
#         self.imie = imie 
    
#     def wyswietlImieRodzic(self):
#         return self.imie

# class Dziecko(Rodzic):
#     def __init__(self, imie, wiek):
#         self.imie = imie 
#         self.wiek = wiek 
#         super().__init__("Ania")


# class Rodzic:
#     def __init__(self, imie):
#         self.imieRodzica = imie
    
# class Dziecko(Rodzic):
#     def __init__(self, imie, wiek):
#         self.imie = imie
#         self.wiek = wiek
    


# def main():
#     dziecko = Dziecko("Kamil", 19)
#     print(dziecko.imieRodzica)


# if __name__ == "__main__":
#     main()


# class Zwierze:
#     def __init__(self, imie):
#         self.imie = imie
    
#     def przywitaj_sie(self):
#         print(f"przywitaj sie {self.imie}")

#     def jesc(self):
#         print(f"{self.imie} je")

# class Pies(Zwierze):
    
#     def przywitaj_sie(self):
#         print(f"przywitaj sie {self.imie}")

#     def szczekaj(self):
#         print(f"{self.imie} szczeka")

# class Ptak(Zwierze):
#     def __init__(self, imie, piora):
#         super().__init__(imie)
#         self.piora = piora

#     def latac(self):
#         print(f"{self.imie} latac")

# moj_ptak = Ptak("Babik", "piora")
# print(moj_ptak.imie)

# moj_pies = Pies("Reksio")
# moj_pies.przywitaj_sie()
# moj_pies.jesc()
# moj_pies.szczekaj()


class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie 
        self.nazwisko = nazwisko
        self.pensja = pensja
    
    def przedstaw_sie(self):
        print(f"Mam na imię{self.imie} a nazwisko to {self.nazwisko}")
    
    def wyplac_pensje(self):
        print(f"{self.imie} {self.nazwisko} otrzymał {self.pensja}")

class Manager(Pracownik):
    def __init__(self, imie, nazwisko, pensja, oddzial):
        super().__init__(imie, nazwisko, pensja)
        self.oddzial = oddzial
    
    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Dział {self.oddzial}")
    
    def wyplac_pensje(self):
        super().wyplac_pensje()
        print(f"Dział {self.oddzial}")

class Dyrektor(Manager):
    def __init__(self, imie, nazwisko, pensja, oddzial, autoSluzbowe):
        super().__init__(imie, nazwisko, pensja, oddzial)
        self.autoSluzbowe = autoSluzbowe

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Dział {self.oddzial}")
    
    def wyplac_pensje(self):
        super().wyplac_pensje()
        print(f"Dział {self.oddzial}")

menagert = Manager("Karol", "Chluba", 500, "sprzedaz")

menagert.przedstaw_sie()
menagert.wyplac_pensje()

                   

#Zad. 7
#
# Utworzyć klasy Notatka (Note) i Notatnik (Notebook). 
# Klas notatki przechowuje autora, treść i czas utworzenia 
# (autor i treść są podawane jako argumenty konstruktora, a czas jest pobierany i zapisywany przy tworzeniu obiektu).
# Konstruktor klasy Notatnik nie przyjmuje żadnych argumentów, 
# lecz tworzy pustą listę do której będą dodawane obiekty klasy 
# Notatka. Klasa Notatnika musi posiadać implementacje metod, 
# pozwalających: dodać nową notatkę, dodać istniejącą notatkę, sprawdzić ile jest dodanych notatek, wyświetlić wszystkie dodane notatki. 
# Dodatkowo musi być obsłużona sytuacja kiedy notatnik jest pusty.


import datetime

class Note:
    def __init__(self, imie, tresc):
        self.imie = imie
        self.tresc = tresc
        self.czas_utworzenia = datetime.datetime.now()
    
    def wyswietlenieInformacji(self):
        print(f"{self.imie}, {self.tresc}, {self.czas_utworzenia}")


class Notebook:

    def __init__(self):
        self.lista = []
    
    def dodaj_nowa(self, autor, tresc):
        notatka = Note(autor, tresc)
        self.lista.append(notatka)
        ilosc+=1 

    def dodaj(self):
        pass

    def ile_notatek(self, ilosc):
        
        pass

    def wyswietl_wszystko(self):
        pass
 
        

def main():
    nb = Notebook()
    nb.dodaj_nowa("Bartek", "Dokonczyc instrukcje")
    nb.wyswietl_wszystko()

if __name__ == "__main__":
    main()

# >>> n1 = Note("Andrii", "Sprawdzic instrukcje")





# Przykład:
# >>> nb = Notebook()
# >>> nb.dodaj_nowa("Bartek", "Dokonczyc instrukcje")
# >>> nb.wyswietl_wszystko()
# Masz takie notatki:
# 1. Bartek: "Dokonczyc instrukcje" o godzinie 22:18

# >>> n1 = Note("Andrii", "Sprawdzic instrukcje "

# >>> nb.dodaj(n1)


# >>> nb.wyswietl_wszystko()
# Masz takie notatki:
# 1. Bartek: "Dokonczyc instrukcje" o godzinie 22:18
# 2. Andrii: "Sprawdzic instrukcje" o godzinie 22:20


# Podpowiedź:
# do reprezentacji czasu można użyć modułu
# datetime
# Dokumentacja modułu
# datetime
# https://docs.python.org/3/library/datetime.html

# Przykład:
# >>> import datetime
# >>> t = datetime.datetime.now()
# >>> t
# datetime.datetime(2021, 4, 8, 22, 39, 46, 274407)
# >>> t.hour
# 22
# >>> t.minute
# 27

