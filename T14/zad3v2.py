def fibonacci():
    a, b = 1, 2  
    while True:
        yield a  
        a, b = b, a + b  
