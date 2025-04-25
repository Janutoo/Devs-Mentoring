number = int(input("Podaj zakres liczb parzystych "))
i = 0
result = 0 
while i<=number:
    if i%2==0:
        result = result +i
        i+=1
        print(result)
    else:
        
        i+=1
print("suma liczb parzystych",result)
