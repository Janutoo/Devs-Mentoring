
a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj drugą liczbe: "))
while b!=0:
        a,b = b,a % b
print(a)    
