import random
import time

n = int(input("Podaj górny przedział "))
b = int(input("Podaj dolny przedział"))
points = 100
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
losowa_liczba = random.randint(b,n)
print("Komputer wylosował liczbę ")
result = 0
while True:
    pytanie1 =(int(input("Podaj liczbe: ")))
    result= pytanie1+result
    print(result)
    if n<result <b:
        print("Zakres 0 do 100")
        exit()
    if losowa_liczba<result:
        print("liczba jest za duza!")
        points-=1
    elif result == losowa_liczba:
        print("zgadłeś")
        print(f"Zdobyłeś:{points} pkt")
    elif losowa_liczba>result:
        print("liczba jest za mala!")
        points-=1