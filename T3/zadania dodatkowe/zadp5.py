number = input("Podaj Liczbe: ")
i = 0
suma = 0
a = len(number)
while i < a:
    suma = suma + int(number[i])
    i+=1
print(suma)