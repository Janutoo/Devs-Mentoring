# lambda argumeny: wyrażenie

number = [4,5]

def is_even(numbers):
    for i in number:
        if i % 2 == 0:
            print(f"liczba {i} jest parzysta")
        else:
            print(f"liczba {i} jest nie parzysta")

print(is_even(number))

is_even = lambda x : x % 2 ==0
print(is_even(4))
print(is_even(5))

constans = lambda : 42
print(constans())

sum_numbers = lambda x, y : x + y
print(sum_numbers(3,5))

# filter(func, interable)

def filter_func(numbers):
    result = []
    for i in numbers:
        if i >= 4:
            result.append(i)
    return result
   

elemetns = [1, 2, 3, 4, 5, 6]
print(filter_func(elemetns))

filtered_result = list(filter(lambda x: x >= 4, elemetns))

print(filtered_result)


# Czy libczy są pierwsze

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# def filter_func(numbers):
#     result = []
#     for i in numbers:
#         if i >= 4:
#             result.append(i)
#     return result

numbers = list(range(1, 20))
prime_numbers = list(filter(is_prime, numbers))
print(prime_numbers)  # [2, 3, 5, 7, 11, 13, 17, 19]

# map(func, iterabl)

def squareds_numbers(numbers):
    result = []
    for i in numbers:
        result.append(i**2)
    return result 
        

numbers = [1, 2, 3, 4]
print(squareds_numbers(numbers))

squardes= list(map(lambda x : x **2, numbers))
print(squardes)

from functools import reduce
# reduce(func, iterable, intilia=opcjonalnie)

def sum_function(numbers):
    result = 0
    for i in numbers:
        result += i
    return result 
        

numbers = [1, 2, 3, 4]
print(sum_function(numbers))

sum_numbers = reduce(lambda x , y : x +y, numbers)
print(sum_numbers)