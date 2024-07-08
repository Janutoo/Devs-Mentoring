try:
    number = int(input("Podaj liczbę 1-7: "))
    if number == 1:
        print("Poniedziałek")
    elif number == 2:
        print("Wtorek")
    elif number == 3:
        print("Środa")
    elif number == 4:
        print("Czwartek")
    elif number == 5:
        print("Piątek")
    elif number == 6:
        print("Sobota")
    elif number == 7:
        print("Niedziela")
    else:
        print("nie ma takiego dnia")    
except ValueError:
    print("nie ma takiego dnia")