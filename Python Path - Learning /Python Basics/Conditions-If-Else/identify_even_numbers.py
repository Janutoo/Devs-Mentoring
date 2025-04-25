number1 = (int(input("Podaj pierwszą liczbę: ")))
number2 = (int(input("Podaj drugą liczbę: ")))

if number1 %2==0 and number2 %2==0:
    print("liczby są parzyste")
elif number1 %2==0 or number2 %2==0:
    print("Jedna liczba jest parzysta")
else:
    print("Żadna liczba nie jest parzysta")


    
