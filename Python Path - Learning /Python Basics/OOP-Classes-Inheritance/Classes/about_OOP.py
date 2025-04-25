# # Programowanie proceduralne:
# # W programowaniu proceduralnym piszemy instrukcje krok po kroku, na przykład:
# def powitaj_proceduralnie(imie):
#     print(f"Cześć, {imie}!")

# def main():
#     powitaj_proceduralnie("Jan")

# if __name__ == "__main__":
#     main()


# class Osoba:
#     def __init__(self, imie_, wiek_, kolorOczu_):
#         self.imie = imie_
#         self.wiek = wiek_
#         self.kolorOczu = kolorOczu_
    
#     def powitaj(self):
#         print(f" Mam {self.kolorOczu}")
#         print(f"Cześć, {self.imie}!")

# def main():
#     # Teraz tworzymy obiekt na podstawie klasy:
#     osoba1 = Osoba("Jan")
#     osoba1.powitaj()

# if __name__ == "__main__":
#     main()

# class Czlowiek:
#     def __init__(self,imie_,nazwisko_,wiek_,pesel_):
#         self.imie=imie_
#         self.nazwisko=nazwisko_
#         self.wiek=wiek_
#         self.pesel=pesel_
    
#     def przywitanie(self):
#         print(f"Cześć mam na imię",self.imie)


# def main():
#     osoba01 = Czlowiek("kamil","janusz",18,2321413241)
#     osoba02 = Czlowiek("karol", "chluba", 26, 12355)
    
#     osoba01.przywitanie()
#     osoba02.przywitanie()   

# if __name__ == "__main__":
#     main()


class Samochod:
    def __init__(self,marka_,model_,rok_,kraj_):
        self.mark=marka_
        self._model=model_
        self.rok=rok_
        self.__kraj=kraj_

    def getKraj(self):
        return self.__kraj

    def setKraj(self, kraj):
        self.__kraj = kraj

def main():
    auto = Samochod("Audi","a4",2016,"Niemcy")
    auto01 = auto

    import copy
    auto01  = copy.auto()
    auto02 = copy.deepcopy(auto)
    auto01.setKraj("Włochy")


    print(auto.getKraj())


    
if __name__ == "__main__":
    main()
