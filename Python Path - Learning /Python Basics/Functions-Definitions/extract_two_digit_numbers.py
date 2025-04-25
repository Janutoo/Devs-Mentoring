def liczby(*args):
    numb = []
    for val in args:
        val2 = len(str(val))
        if val2 == 2:
            numb.append(val)
    return numb

numbers = []
for i in range(10):
    number = int(input("Podaj liczbę: "))
    numbers.append(number)
print(liczby(*numbers))

x = lambda x: len(str(x)) == 2
a = list(filter(x,numbers))
print(a)