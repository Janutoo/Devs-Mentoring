print("Napisz funkcję generatora, która generować będzie kilka dowolnych wartości. Pobierz te wartości przy użyciu globalnej metody next() oraz metody generatora __next__(). Rzuć wyjątkiem wewnątrz generatora (po jego kilkukrotnym wywołaniu) i zbadaj stack trace.")

def generate():
    for i in range(10):
        yield i

gen = generate()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

