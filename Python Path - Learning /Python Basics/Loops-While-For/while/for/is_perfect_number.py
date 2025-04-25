number = int(input("Podaj liczbę: "))
suma = 0
for i in range(1, number):
    if number % i == 0:
        suma += i
if suma == number:
    print("Podana liczba jest doskonała.")
else:
        print("Podana liczba nie jest doskonała.")