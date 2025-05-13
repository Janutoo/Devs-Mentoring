a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))
c = float(input("Podaj długość trzeciego boku: "))

sides = sorted([a, b, c])

if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("Podane długości tworzą trójkąt prostokątny.")
else:
    print("Podane długości nie tworzą trójkąta prostokątnego.")
    