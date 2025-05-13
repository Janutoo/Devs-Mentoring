def fibonacci():
    a, b = 1, 2  
    while True:
        yield a  
        a, b = b, a + b  

gen = fibonacci()

print(next(gen))  
print(next(gen))  
print(next(gen))  
print(next(gen))  
print(next(gen))  
print(next(gen))  