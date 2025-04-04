# data = [10, 0, "text"]
# for item in data:
#     print(100 / item)


    
# ZeroDivisionError: division by zero

# ZeroDivisionError	Występuje, gdy próbujesz dzielić przez zero.
    
    
# Typowe wyjątki w Pythonie
# Wyjątek	Opis
# ValueError	Niewłaściwa wartość dla operacji.
# IndexError	Indeks poza zakresem sekwencji (np. listy).
# KeyError	Nieznaleziony klucz w słowniku.
# IOError	Problem z operacją wejścia/wyjścia (np. plik niedostępny).
# NameError 




# TypeError	Operacja wykonywana na niezgodnych typach.



# print (0 * x)

# x = int("text")
# numbers = [1, 2, 3, 4, 5]
# try:
#     print(numbers[10])  # Próba dostępu do indeksu poza zakresem
# except IndexError as e :
#     print(f"Bład:{e}" )
    


# Opis: Napisz program, który prosi użytkownika o podanie dwóch liczb i wykonuje dzielenie. Obsłuż błędy:

# Dzielenie przez zero.
# Nieprawidłowy format danych wejściowych.


# try: 
#     numbers = int(input("wprowadz liczbe:"))
#     numbers2 = int(input("liczba dzielona:"))
#     result = numbers/numbers2
# except ZeroDivisionError as e:
#     print(f"Błąd:{e}")
# except ValueError as e: 
#     print (f" Błąd :{e}")
# else:
    
#     print(f"Wynik:{result}")
# finally:
#     print("Zakończono obliczenia")
    
# else i finally

# try:
#     file = open("example.txt", "w")
#     file.write("Dane testowe")
    
# except IOError:
#     print("Bład przy zapisaniu do pliku")
# else:
#     print("Zapisano pomyślnie teskt w pliku")
# finally:
#     file.close()
#     print("Plik zamknniety")

class TooSmallError(Exception):
    def __init__ (self,value):
        self.value = value
    def __str__(self):
        return f"Libcza {self.value}, jest za mała"
    
def validate_postive(number):
    if number <= 0:
        raise TooSmallError("Invalid postive")

data = [1, 2, 0]
for item in data:
    validate_postive(item)
    
    
