number = (int(input("Podaj liczbe: ")))

if number > 0:
    print(("Liczba {} jest dodatnia").format(number))
elif number == 0:
    print(("Liczba przyjmuje wartość {}").format(number))
else:
    print(("Liczba {} jest ujemna").format(number))