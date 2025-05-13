# lista = ["gruszka", "truskawka", "banan"]
# wprowadz = input("Wprowadz nazwe owoca")

# if wprowadz in lista:
#     print("jest w liscie")
# else:
#     print("nie ma na lisie ")

# listaLiczb = [3,3,1]

# if listaLiczb[0] == listaLiczb[1] or listaLiczb[1] == listaLiczb[2] or listaLiczb[0] == listaLiczb[2]:
#     print("dwie sa takie same ")
# else:
#     print("nie sa takei same")
# numbers = []
# i = 0
# while i < 3:
#     number = int(input("podaj liczbe: "))
#     numbers.append(number)
#     i +=1

# if numbers[0] < numbers[1] and numbers[1] < numbers[2]:
#     print("liczby sa rosnąco")
# else:
#     print("liczby nie są rosnoąco ")

# a = float(input("Podaj długość pierwszego boku: "))
# b = float(input("Podaj długość drugiego boku: "))
# c = float(input("Podaj długość trzeciego boku: "))

# if a + b > c and a + c > b and b + c > a:
#     print("mozna zbudowac ")
# else:
#     print("nie mozna")

day = int(input("Wprowadz dzień od 1 do 31: "))
if day  < 1 or day > 31:
    print("Wprowadzono zły dzień ")
    exit()
month = int(input("Wprowadz miesiac od 1 do 12: "))
if month < 1 or month > 12:
    print("Wprowadzono zły miesiąc")
    exit()
year = int(input("Wprowadz rok od 1900 do 2050: "))
if year < 1900 or year > 2050:
    print("Wprowadzono zły rok")
    exit()


print(f"Rok{day}.{month}.{year}r.")
