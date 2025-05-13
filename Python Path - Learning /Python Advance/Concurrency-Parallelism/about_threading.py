# Proces: Oddzielny program działający na procesorze.
# Wątek: Lżejszy od procesu, dzielący pamięć z innymi wątkami tego samego procesu.

# import threading

# Struktura wątku w Pythonie:
# 1 Funkcja docelowa(target)
# 2 Argumety (args)
# 3 Metody wątku 
# * start()
# * join()
# * is_alive()

# def print_hello():
#     print("Hello")

# thread = threading.Thread(target=print_hello)

# thread.start()

# thread.join()

# import time

# def task(name):
#     print(f"{name} is starting")
#     time.sleep(2)
#     print(f"{name} is finished")
    
# thread1 = threading.Thread(target=task, args=("Thread1",))
# thread2 = threading.Thread(target=task, args=("Thread2",))

# thread1.start()
# thread2.start()


# thread1.join()
# thread2.join()

# print("All threas are finished!")

# Zadanie 1: Symulacja współbieżności i równoległości
# Stwórz dwa wątki w Pythonie, gdzie jeden wypisuje liczby, a drugi litery.
# Użyj import time, time.sleep(2)

#GIL Global Interpreter Lock

import threading

from multiprocessing import Process
import timeit


def measure_threading():
    threads = [threading.Thread(target=task) for _ in range(2)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

def task():
    result = 0
    for i in range(1000000):
        result += i ** 2

def measure_multiprocessing():
    processes = [Process(target=task) for _ in range(2)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()


if __name__ == "__main__":
    threading_time = timeit.timeit(measure_threading, number=1)
    print(f"Czas wykonania z threading: {threading_time:.6f} sekund")
    multiprocessing_time = timeit.timeit(measure_multiprocessing, number=1)
    print(f"Czas wykonania z multiprocessing: {multiprocessing_time:.6f} sekund")



# Zadanie 4: Dwa wątki obliczające różne potęgi
# Stwórz dwa wątki: jeden oblicza kwadraty liczb, a drugi sześciany.


# import threading

# def calculate_square(numbers):
#     for number in numbers:
#         print(f"Kwadrat liczby {number} to {number**2}")

# def calculate_cube(numbers):
#     for number in numbers:
#         print(f"Sześcian liczby {number} to {number**3}")

# numbers = [1, 2, 3, 4, 5]

# thread1 = threading.Thread(target=calculate_square, args=(numbers,))
# thread2 = threading.Thread(target=calculate_cube, args=(numbers,))
# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# DeadLock
# import threading

# lock = threading.Lock()

# def task():
#     lock.acquire()
#     lock.acquire()
#     lock.release()

# threaad = threading.Thread(target=task)
# threaad.start()
# threaad.join()

#Data race

# import threading

# counter = 0  

# def increment():
#     global counter
#     for _ in range(100000):
#         counter += 1  


# thread1 = threading.Thread(target=increment)
# thread2 = threading.Thread(target=increment)


# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# print(f"Wynik końcowy: {counter}")

# Race condition

# import threading

# balance = 100  # Wspolny 

# def withdraw(amount):
#     global balance
#     if balance >= amount:
#         print(f"Wypłata {amount}")
#         balance -= amount
#     else:
#         print("Za mało środków")


# thread1 = threading.Thread(target=withdraw, args=(80,))
# thread2 = threading.Thread(target=withdraw, args=(50,))


# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# print(f"Pozostałe środki: {balance}")
