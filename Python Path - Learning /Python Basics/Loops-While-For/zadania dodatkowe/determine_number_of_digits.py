number = int(input("podaj liczbe: "))
text =str(number)
print(len(text))

number2 = 0
while number != 0:
    number = number // 10  
    number2 += 1  
print("Ilość cyfr w podanej liczbie:", number2)