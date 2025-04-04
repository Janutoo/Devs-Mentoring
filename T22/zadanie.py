# list_of_systems = []
# while True:
#     entry = input("Podaj nazwe systemu nawigacyjnego:")
#     if entry == "koniec":
#         break    
#     else:
#         list_of_systems.append(entry)
        


# #2
# while True:
#     bilet_price = int(input("podaj wiek tego cwela"))
#     if bilet_price < 3: 
#         print("bilet jest darmowy")
#     elif bilet_price <= 10:
#         print("bilet kosztuje 600zł")
#     else:
#         print("bilet kosztuje 900zł")
#     check = input(("czy chcesz sprawdzac ceny biletu dalej? [tak/nie]"))
#     if check == "nie":
#         break
# #4
# while True:
#     entry = int(input("podaj liczbę "))
#     if entry == 0:
#         print(entry)
#         break
#     _sum += entry

# import random


# n = int(input("Podaj górny przedział "))
# b = int(input("Podaj dolny przedział"))
# losowa_liczba = random.randint(b,n)
# print("Komputer wylosował liczbę ")
# while True:
#     result =(int(input("Podaj liczbe: ")))
#     if n<result <b:
#         print("Zakres 0 do 100")
#         exit()
#     if losowa_liczba<result:
#         print("liczba jest za duza!")
#     elif result == losowa_liczba:
#         print("zgadłeś")
#     elif losowa_liczba>result:
#         print("liczba jest za mala!")
#     break
#6
podstawa = int(input("podaj podstawę"))
wykladnik = int(input("podaj wykladnik"))   
i = 0
result = 1
if wykladnik == 0:
    print("0")
while wykladnik > i:
    result = result * podstawa
    i += 1
print(result)