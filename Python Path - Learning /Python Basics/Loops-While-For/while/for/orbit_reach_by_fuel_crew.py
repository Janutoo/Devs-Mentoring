high = 0
members = 0
fuel = 0 
distance = 0
try:   
    while True:
        fuel = (int(input("Podaj ilość paliwa: ")))
        if fuel>=5000 and fuel<=30000:
            break 
        else:
            print("podaj poprawną wartość 5000-30000")  
    while True:
        members = (int(input("Podaj ilość Członków: ")))
        if members >0 and members <= 7:
            break
        else:
            print("Podaj poprawną wartość od 1-7 ")
    for i in range (0,fuel,100):
        fuel= fuel-(300+100*members)
        print("Przebydto: ",i)
        distance = i
        print(fuel)
        if fuel==0:
            break
    if distance>2000:
        print("Statek dotarł na orbite ")
    else:
        print("Statek kosmiczny nie dotarł na orbite")
except ValueError:
    print("Podaj poprawną wartość ")
