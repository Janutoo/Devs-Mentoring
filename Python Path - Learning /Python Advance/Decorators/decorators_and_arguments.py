# 1. Dekorator liczący czas wykonania funkcji
# Cel: Stworzyć dekorator measure_time, który zmierzy czas wykonania funkcji i wypisze go na ekran.
# Opis: Dekorator powinien korzystać z modułu time do zmierzenia czasu przed i po wykonaniu funkcji,
#  a następnie obliczyć różnicę.

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs)  
        end_time = time.time() 
        execution_time = end_time - start_time  
        print(f"Funkcja '{func.__name__}' wykonała się w {execution_time:.6f} sekund.")
        return result 
    return wrapper

@measure_time
def sample_function(n):
    total = 0
    for i in range(n):
        total += i
    return total


result = sample_function(1000000)


def example(**kwargs):
    print(kwargs)

example(name="example", age=30)
# def example(*args):
#     print(args)

example(1,2,3)