imieinazwisko = "Kamil Janusz"

cytat = "Jestem zajebisty "

message = imieinazwisko + "Powiedział kiedyś: " + cytat 


print(message)

age = int(input("Podaj liczbę: "))


if age < 1:
    print("Jest niemowleciem")
elif 1 < age < 3:
    print("Etap wczesnego dzieciństwa")
elif 3 < age < 13:
    print("dziecko")
elif 13 < age < 20:
    print("nastolatek")
elif 20 < age < 65:
    print("dorosły")
else:
    print("senior")