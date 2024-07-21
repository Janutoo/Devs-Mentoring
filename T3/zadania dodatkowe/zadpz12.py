import random 
n = int(input("Podaj ilość rzutów kostką: "))
i=0
number1 = 0
number2 = 0
number3 = 0 
number4 = 0
number5 = 0 
number6 = 0 
while i < n:
    throw=random.randint(1,6)
    if throw == 1:
        number1+=1
    elif throw == 2:
        number2+=1
    elif throw ==3:
        number3+=1
    elif throw ==4:
        number4+=1
    elif throw ==5:
        number5+=1
    elif throw ==6:
        number6+=1
    i+=1
print(f"Liczba 1 wypadała: {number1}")
print(f"Liczba 2 wypadała: {number2}")
print(f"Liczba 3 wypadała: {number3}")
print(f"Liczba 4 wypadała: {number4}")
print(f"Liczba 5 wypadała: {number5}")
print(f"Liczba 6 wypadała: {number6}")

