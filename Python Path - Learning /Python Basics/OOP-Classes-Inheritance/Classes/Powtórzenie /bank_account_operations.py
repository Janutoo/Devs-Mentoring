# Zadanie 3 – Hermetyzacja
# Zaimplementuj klasę BankAccount, która będzie chronić dane klienta:
# •	Prywatne pola: saldo oraz numer konta.
# •	Publiczne metody: wpłata, wypłata (sprawdzająca saldo), odczyt salda.
# •	Sprawdź poprawność działania i ochronę pól przed dostępem z zewnątrz.



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