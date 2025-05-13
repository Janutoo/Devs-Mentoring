number = int(input("Podaj liczbę: "))
suma = 0
i = 1
while i < number:
    if number % i == 0:
       suma += i
    i+=1
if suma == number:
    print("Podana liczba jest doskonała.")
else:
        print("Podana liczba nie jest doskonała.")