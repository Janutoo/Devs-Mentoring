n = int(input("Podaj zakres: "))
i = 2

while i <= n:
    if i == 2:
        print("Podana liczba jest pierwsza: ", i)
    elif i % 2 == 0:
        print("Podana liczba nie jest pierwsza: ", i)
    else:
        d = 3
        while d * d <= i:
            if i % d == 0:
                print("Podana liczba nie jest pierwsza: ", i)
                break
            d += 2
        else:
            print("Podana liczba jest pierwsza: ", i)
    
    i += 1
    