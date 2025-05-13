import timeit
import threading
import multiprocessing

def measure_threading():
    threads = [threading.Thread(target=bubble_sort, args=(array,)) for array in sample_arrays]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def multithreading_sort(arr):
    threads = []
    for array in arr:
        thread = threading.Thread(target= bubble_sort, args=(array,))
        threads.append(thread)
        thread.start()
    for thead in threads:
        thead.join()

sample_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 3, 8, 6, 2, 7, 4, 1],
        [29, 10, 14, 37, 14],
        [10, 30, 20, 40, 50],
        [3, 5, 1, 8, 7, 2, 6],
        [9, 7, 5, 3, 1],
        [100, 200, 50, 150],
        [15, 10, 5],
        [99, 44, 77, 33, 11],
        [2, 1, 3]
    ]

print("Unsorted sample arrays")
for array in sample_arrays:
    print(array)

multithreading_sort(sample_arrays)

print("Sorted sample arrays")
for array in sample_arrays:
    print(array)



multiprocessing_time = timeit.timeit(lambda: multithreading_sort(sample_arrays), number=1)
print(f"Czas wykonania z threading: {multiprocessing_time:.6f} sekund")

threading_time = timeit.timeit(lambda: measure_threading(), number=1)
print(f"Czas wykonania z measure_threading: {threading_time:.6f} sekund")





# https://docs.python.org/3/library/multiprocessing.html
# int a = 5 
# int *ptr = &a 

# smart pointer[64, 34, 25, 12, 22, 11, 90],