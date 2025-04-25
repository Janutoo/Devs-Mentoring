# Zadanie 1: Suma liczb
# Napisz funkcję sum_all(*args), która przyjmuje dowolną liczbę argumentów i 
# zwraca ich sumę. Jeśli nie zostaną podane żadne argumenty, funkcja powinna zwrócić 0.



# def sum_all(*args):
#     sum= 0
#     for numbers in args:
#         sum += numbers
#     return(sum)
#     # return sum(args) if args else 0

# print(sum_all(1,2,3,4,5))
# print(sum_all())

# Zadanie 2: Powitanie użytkowników
# Napisz funkcję greet_users(*args), która przyjmuje dowolną liczbę imion i drukuje 
# komunikat powitalny dla każdego z nich.


# def greet_users(*args):
#     greetings = list()
#     for name in args:
#         greetings.append(f"Witaj {name}")
#     return greetings

# greetings = greet_users("kamil","bartek","karol")
# for i in greetings:
#     print(i)

# Zadanie 4: Mnożenie liczb
# def multiply_with_factor(factor, *args):
#     if len(args) == 0:
#         return("brak liczb do mnozenia")
    
#     result = list()
#     for number in args:
#         result.append(factor*number)
#     return(result)
        

    



# print(multiply_with_factor(2,1,2,3))  # [2, 4, 6]
# print(multiply_with_factor(0.5, 10, 20))
# print(multiply_with_factor(3)) 



# Zadanie 3: Informacje o osobie

# def print_information_personality(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} = {value}")


# dict_of_information = {name : "karol" ,age : 23, city: "rzeszow"}
# print_information_personality(**dict_of_information, country="Poland")


# Zadanie 5: Tworzenie zamówienia

# def create_order(item, quantity, **detalis):
#     dict = {"item": item,"quantity": quantity}
#     result = dict | detalis
#     return result

# order = create_order("Laptop", 2, color="silver", warranty="2 years")
# # {'item': 'Laptop', 'quantity': 2, 'color': 'silver', 'warranty': '2 years'}
# print(order)


# Zadanie 6: Zliczanie typów danych
# Napisz funkcję count_types(*args, **kwargs), która przyjmuje zarówno argumenty pozycyjne, 
# jak i klucz-wartość, i zwraca słownik z informacjami o liczbie argumentów dla każdego typu danych.

def count_types(*args, **kwargs):
    lista_args_kwargs= []
    list_of_args = list(args)
    list_of_kwargs = list(kwargs.value)

    list_args_kwargs = list_of_args + list_of_kwargs

    dict = {}
    for i in list_args_kwargs:
        dict.update(type(i))
    return(dict)



result = count_types(1, "hello", 3.14, age=25, name="Alice", married=True)
# {'int': 2, 'str': 2, 'float': 1, 'bool': 1}
