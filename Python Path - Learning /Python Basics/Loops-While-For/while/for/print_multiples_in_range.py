try:
    number = int(input("Podaj liczbę: "))
    n = int(input("Podaj początek przedziału: "))
    m = int(input("Podaj koniec przedziału: "))
    if n < m:
        print("Liczby podzielne przez {} w przedziale od {} do {}:".format(number,n,m))
    for i in range(n, m + 1):
        if i % number == 0:
            print(i)
    else:
        print("Początek musi być wiekszy od końca")
except ValueError:
    print("Wartość nie jest liczbą całkowitą ")