import random
import time
points_user = 0
points_computer = 0
print("Wygrasz gdy uzyskasz 3 pkt\n Przegrasz gdy komputer uzyska 3 pkt")


while True:
    wybor = (input("o - orzeł \n r - reszka\n Wybierz:"))
    wybor_komputera = random.randint(0,1)
    if wybor not in["o","r"]:
        continue
    if wybor_komputera == 0:
        wybor_komputera = 'o'
    else:
        wybor_komputera ='r'
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Wybór komputera",wybor_komputera)
    if wybor == wybor_komputera:
        points_user+=1
        if points_user == 3:
            print("Wygrałeś posiadasz 3 punktów")
            exit()
       
        print(("Wygrałeś posiadasz {} punktów").format(points_user))
    else:
        points_computer+=1
        if  points_computer == 3:
            print("Przegrałeś komputer zdobył 3 punkty")
            exit()
        print(("Przegrałeś  komputer posiada {} punktów").format(points_computer))
        