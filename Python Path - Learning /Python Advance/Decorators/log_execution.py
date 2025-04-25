# 2. Dekorator dodający logowanie
# Cel: Stworzyć dekorator log_execution, który loguje rozpoczęcie i zakończenie wykonywania funkcji.
# Opis: Dekorator wypisuje komunikaty przed i po wykonaniu dekorowanej funkcji.

def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Początek funkcji:{func.__name__}przyjmuje argumenty {args}, {kwargs}")
        result = func(*args, **kwargs)  
        print(f"Koniec Funkcji:{func.__name__}")
        return result  
    return wrapper
        
@log_execution
def sum_function(a, b):
    return a + b

print(sum_function(4,5))
