def iloczyn(*args):
    iloczyn = 1 
    for val in args:
        iloczyn *=val
    return iloczyn
number= int(input("Podaj liczby: "))
numbers = []
while number:
    numbers.append(number)
    number = int(input("Podaj liczby: "))
print(iloczyn(*numbers))