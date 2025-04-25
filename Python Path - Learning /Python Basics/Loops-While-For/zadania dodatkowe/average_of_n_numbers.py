numberOfNumbers = int(input("Podaj ilość liczb: "))
_sum = 0 
i = 0 
while i < numberOfNumbers:
    number =int(input("Podaj liczbę: "))
    _sum = _sum + number
    i+=1 
result = _sum/numberOfNumbers
print(result)
