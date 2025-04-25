number = int(input("Podaj zakres liczb nieparzystych"))
i = 0 
while i<number:
    if i%2==0:
        i+=1
    else:
        print(i)
        i+=1

