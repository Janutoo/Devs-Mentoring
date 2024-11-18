# #nazwa 
# def greet_decorator(func):
#     # core, opakowanie
#     def wrapper():
#         print("Witaj")
#         func()
#     return wrapper

# @greet_decorator
# def greet():
#     print("Milo Cie widziec!")

# greet()
# from functools import wraps

# def decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"poczatek funkcji {args}, {kwargs}")
#         func(*args, **kwargs)
#         print("koniec funkcji")
#     return wrapper

# @decorator
# def say_hello(name):
#     """Wyświetla powitanie."""
#     print(f"Cześć {name}!")

# say_hello('Kamil')

# print(say_hello.__doc__)

# )

# @staticmethod
# @classmethod

# class Worker:
#     def __init__(self, name, start_year):
#         self.name = name
#         self.start_year = start_year

#     @classmethod
#     def from_years_worked(cls, name, years):
#         start_year = cls.calculate_start_year(years)
#         return cls(name,start_year)
    
#     @staticmethod
#     def calculate_start_year(years):
#         current_year = 2024
#         return current_year - years

#     def print_name(self):
#         print(self.name)

# worker = Worker.from_years_worked("Kami", 5)
# worker_start_year = Worker.calculate_start_year(5)
# print(worker_start_year)
# print(worker.name, worker.start_year)

#(0°C × 9/5) + 32 = 32 

class TemperatureConverter:
    def __init__(self, celsius, fahrenheit):
        self.celsius = celsius
        self.fahrenheit = fahrenheit

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celsius = cls.fahrenheit_to_celsius(fahrenheit)
        return cls(celsius, fahrenheit)
    
    @classmethod
    def from_celsius(cls, celsius):
        fahrenheit = cls.celsius_to_fahrenheit(celsius)
        return cls(celsius, fahrenheit)
    
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
    
        return (fahrenheit-32) * 5/9 


#przyklad uzycia

temp_c = TemperatureConverter.from_celsius(20)
temp_f = TemperatureConverter.fahrenheit_to_celsius(32)
print(temp_c.fahrenheit, temp_c.celsius)
print(temp_f.celsius)
# print(TemperatureConverter.celsius_to_fahrenheit(0))
# print(TemperatureConverter.fahrenheit_to_celsius(32))


#car = Car("Toyota", 2020, 200)

#car.prinnt_ifno()
#car.calcutlete_max_speed(200)