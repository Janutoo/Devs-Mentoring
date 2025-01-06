# Zadanie 1: Tworzenie sekwencji Fibonacciego za pomocą generatora

def fibonacci_generator():
    a, b = 0, 1
    b = 1
    while True:
        yield a
        a, b = b, a + b

    

fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))


     # 0 1 1 2 3 5 8 13 21 34    


# Procedure Fibonacci: n
# Display 0, 1
# Set a=0,b=1
# Display a,b
# While the number of terms is less than n
         
#          c=a+b
#          Display c
#          Set a=b, b=c
# End procedure

#Zadanie 2: Generowanie nieskończonej sekwencji liczb parzystych
def even_numbers():
    a = 0 
    while True:
        yield a
        a += 2



even_gen = even_numbers()

for _ in range(15):
    print(next(even_gen))
    

#Zadanie 4: Generowanie nieskończonego ciągu znaków
def cyclic_alphabet():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        for letter in alphabet:
            yield letter
            
alphabet_gen = cyclic_alphabet()

# for _ in range(30):
#     print(next(alphabet_gen), end= ' ')

#Zadanie 5: Zliczanie elementów w nieskończonej sekwencji

def counting_generator():
    count = 0
    number = 1
    while True:
        count += 1 
        yield number, count
        number += 1 
        
        
count_gen = counting_generator()
  
for _ in range(5):
    numbers, count = next(count_gen)
    print(f"Liczba: {numbers}, Ilość wygenerowanych: {count}")


'''
Liczba: 1, Ilość wygenerowanych: 1
Liczba: 2, Ilość wygenerowanych: 2
Liczba: 3, Ilość wygenerowanych: 3
Liczba: 4, Ilość wygenerowanych: 4
Liczba: 5, Ilość wygenerowanych: 5
'''

def counting_generator_with_for(data):
    numbers, count = 1, 0
    for value in data:
        count += 1 
        yield numbers, count
        numbers += 1 

numbers = [1, 2, 3, 4 ,5]
counting_gen = counting_generator_with_for(numbers)
for _ in numbers:
    numbers, count = next(counting_gen)
    print(f"Liczba: {numbers}, Ilość wygenerowanych: {count}")
    
# Zadanie 3: Filtruj liczby pierwsze za pomocą generatora
# Napisz generator prime_numbers, który generuje liczby pierwsze. Wypisz pierwsze 10 liczb pierwszych.
# def prime_numbers():
#     pass

# prime_gen = prime_numbers()

# for _ in range(10):
#     print(next(prime_gen))
    
#     ''''
#     2
#     3
#     5
#     7
#     11
#     13
#     17
#     19
#     23
#     29

#     '''


# Zadanie: Generator wzorców liczbowych 
''''
    1, 11, 111, 1111, ...
    lub 2, 22, 222, 2222, ...
'''

def number_patterns(n):
    pattern = ''
    while True:
        pattern += str(n)
        yield int(pattern)
    

gen = number_patterns(5)

for _ in range(5):
    print(next(gen))