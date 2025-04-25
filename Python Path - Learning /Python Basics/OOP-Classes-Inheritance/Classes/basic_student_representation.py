# Zad. 1
# Stwórz klasę reprezentującą studenta. 
# Cechy studenta określaj z poziomu konstruktora. D
# odaj do klasy metodę wyświetlającą informacje o danym obiekcie.


class Student:
    def __init__(self, imie, nazwisko, numer_indeksu, kierunek):
        # Cechy studenta
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.kierunek = kierunek

    def wyswietl_informacje(self):
        # Wyświetlanie informacji o studencie
        print(f"Student: {self.imie} {self.nazwisko}")
        print(f"Numer indeksu: {self.numer_indeksu}")
        print(f"Kierunek: {self.kierunek}")


student1 = Student("Jan", "Kowalski", "123456", "Informatyka")
student1.wyswietl_informacje()

# Zad. 2
# Stwórz klasę reprezentującą pojazd. 
# Dodaj do niej pola określające maksymalną prędkość obiektu oraz
#  jego przebieg. Dodaj do klasy metodę, która zwiększać będzie wartość 
# pola przebiegu o przesłaną wartość typu float.

class Pojazd:
    def __init__(self, przebieg, maxSpeed):
        self.maxSpeed = maxSpeed
        self.przebieg = przebieg
    
    def zwiekszPrzebieg(self, dystans):
        if dystans > 0:
            self.przebieg += dystans
        else:
            print("Dystans musi byc wiekszy niz zero")

    def wyswietlInformacjeOPojezdzie(self):
        print(f"Przebieg: {self.przebieg}")
        print(f"Maksymalna predkość: {self.maxSpeed}")
        
pojazd01 = Pojazd(200000,230)
pojazd01.wyswietlInformacjeOPojezdzie()

pojazd01.zwiekszPrzebieg(200)
pojazd01.wyswietlInformacjeOPojezdzie()



# Zad. 4
# Stwórz Pythonową klasę BankAccount, która reprezentować będzie konto bankowe zawierające takie informacje jak: numer_konta, nazwa właściciela konta, stan konta. 
# Stwórz konstruktor odpowiednio uzupełniający pola.
# Napisz metodę deposit(), która przyjmować będzie kwotę, jaką chcesz wpłacić na konto. Dodaj założenie, że za każde wpłacone 100 zł, pobierana będzie prowizja równa 2 zł.
# Stwórz metodę withdraw(), która przyjmować będzie jako parametr kwotę, którą chcesz wypłacić z konta. Program ma wyświetlać odpowiedni komunikat, gdy niemożliwe jest wypłacanie wskazanej ilości pieniędzy (przykładowo z powodu braku wystarczającej ilości środków na koncie).
# Napisz metodę change_ownership(), która przyjmować będzie imię nowego właściciela konta i będzie aplikowała tę zmianę w obiekcie klasy.
# Stwórz metodę display(), która będzie wyświetlać wszystkie informacje o koncie.

class BankAccount:
    def __init__(self, numer_konta, nazwa_wlasciciela, stan_konta):
        self.numer_konta = numer_konta
        self.nazwa_wlascicela = nazwa_wlasciciela
        self.stan_konta = stan_konta

    def deposit(self, wprowadzona_kwota):
        prowizja = (wprowadzona_kwota // 100) * 2
        self.stan_konta += wprowadzona_kwota
        print(f"Wpłacona kwota: {wprowadzona_kwota}")
        print(f"Prowizja: {prowizja} z {wprowadzona_kwota}")
        
    def withdraw(self, wprowadzona_kwota): 
        if self.stan_konta >= wprowadzona_kwota:
            self.stan_konta -= wprowadzona_kwota
            print(f"Wypłacono: {wprowadzona_kwota}")
        else:
            print("Jesteś spłukany")
    
    def change_ownership(self, imie):
        temp = self.nazwa_wlascicela
        self.nazwa_wlascicela = imie
        print(f"Włascicielem konta {temp} został zmienionu na nowego {self.nazwa_wlascicela}")

    def display(self):
        print(f"numer konta: {self.numer_konta}")
        print(f"Imię własciciela: {self.nazwa_wlascicela}")
        print(f"Stan konta wynosi: {self.stan_konta}")

konto1 = BankAccount(123124, "kamil", 1000)

konto1.display()


#Wplata na konto 500 zl
konto1.deposit(500)
# wyswielt informacje
konto1.display()


#wyplata 300 zl
konto1.withdraw(300)
#Wyswielt
konto1.display()


#wyplata 1500 zl
konto1.withdraw(1500)



#zmiana uzytkownika
konto1.change_ownership("karol")

#wysiwelt
konto1.display()