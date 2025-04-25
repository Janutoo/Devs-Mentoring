n = int(input("Podaj Liczbe: "))

c =1
while c <= n:
    suma =0 
    i = 0
    a = len(str(c))
    while i < a:
        suma = suma + int(str(c)[i])**a 
        i+=1
    if suma == c:
        print(c)
    c+=1    

