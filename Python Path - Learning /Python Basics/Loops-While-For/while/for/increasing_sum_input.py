suma = 0
suma2 = 0
while True:
    number = int(input("Wpisz liczbę : "))
    suma += number
    if suma <= suma2:
        break
    suma2 = suma
print("Końcowa suma :", suma)