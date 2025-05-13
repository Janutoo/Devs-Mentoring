# Stabdardiwa składbua kusty składanej

'''

[wyrażenie for elemet in kolekcja]

Z warunkiem

[wyrażenie for element in kolekcja if warunek]

'''
# Kwadrat liczby naturalnych

squares = []
for i in range(10):
    i = i ** 2 
    squares.append(i)
print(squares)

squares2 = [i**2 for i in range(10)]
print(squares2)

# Pobieranie liczb parzystych

even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# Płaskie listy z macierzy dwuwymniarowej

matrx = [[1,2], [3,4]]
flat_list = [num for row in matrx for num in row]
print(flat_list)


sentence = "Python to fajny jezyk!"
upper_sentence = ''.join([char.upper() for char in sentence])
print(upper_sentence)
print(sentence)

print(upper_sentence)


# Podnoszenie liczb do kwadratu ale tylko parzystych
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares_numbers = [i**2 for i in numbers if i % 2 == 0]



'''
def generate():
    for i in range(10):
        yield i

gen = generate()

print(next(generate))

'''

# def simple_generator():
#     print("Start")
#     yield 1
#     print("Resumed")
#     yield 2
#     print("End)")
#     yield 3

# gen = simple_generator()

# print(next(gen))
# print(next(gen))
# print(next(gen))

# Nieskończony ciąg liczb

# def infinity_numbers(): 
#     num = 0
#     while True:
#         value = yield num
#         if value is not None:
#             num += value
#         num += 1

# func = infinity_numbers()
# print(next(func))
# print(next(func))
# print(func.send(10))
# print(next(func))
# print(next(func))
# print(next(func))
# print(next(func))
# print(next(func))
# func.close()
# print(next(func))

# def accumulator():
#     total = 0
#     while True:
#         value = yield total
#         if value is not None:
#                 total += value

# gen = accumulator()
# print(next(gen))
# print(gen.send(10))
# print(gen.send(15))


def controlle_gen():
    try:
        while True:
            yield "Running"
    except ValueError:
        yield "Error"
        return

gen = controlle_gen()
print(next(gen))
print(next(gen))
print(gen.throw(ValueError))