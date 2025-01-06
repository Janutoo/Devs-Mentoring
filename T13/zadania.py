double = lambda x: x * 2
print(double(4))  

add = lambda x, y: x + y
print(add(3, 7))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))
print(squares)  


numbers = [5, 2, 9, 1, 5, 6]

sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)

