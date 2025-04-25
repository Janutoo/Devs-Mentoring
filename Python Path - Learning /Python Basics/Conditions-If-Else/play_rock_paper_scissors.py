

print("Wybierz: kamień, papier, nożyce ")
user1 =(input("Wybór gracza 1: "))
user2 =(input("Wybór gracza 2: "))

if user1 and user2 in ["kamień","papier","nożyce"]:
    if (user1 == 'kamień' and user2 == 'nożyce') or \
        (user1 == 'papier' and user2 == 'kamień') or \
        (user1 == 'nożyce' and user2 == 'papier'):
        print("Wygrywa Gracz 1!")
    elif user1 == user2:
        print("remis")
    else:
        print ("Wygrywa Gracz 2!")
else:
    print("Błędne Dane !")
    