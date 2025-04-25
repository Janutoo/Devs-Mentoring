numbers = []
i = 0 
d = 0
while i < 10:
    number = int(input("Podaj liczbę: "))
    numbers.append(number)
    i+=1
while d < 10:
    if numbers[d]%2==0:
            print(numbers[d])
            d+=1
    else:
         d+=1