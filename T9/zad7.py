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
        print("Dodano nową notatkę")
        

    def dodaj(self, note):
        for n in self.lista:
            if n.imie == note.imie and n.tresc == note.tresc:
                self.lista.append(Note)


    def ile_notatek(self):
        return len(self.lista)


    def wyswietl_wszystko(self):
        if not self.lista:
            print("Notatnik jest pusty")
        else:
            for i in (self.lista):
                print(f"Notatka {self.lista}")
 
        

def main():
    nb = Notebook()
    nb.dodaj_nowa("Bartek", "Dokonczyc instrukcje")
    nb.wyswietl_wszystko()

if __name__ == "__main__":
    main()
