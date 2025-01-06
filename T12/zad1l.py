def log_arguments(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Positional arguments: {args}")
        print(f"Keyword arguments: {kwargs}")
        result = func(*args, **kwargs)  
        return result

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


@log_arguments
def add(a, b):
    return a + b

@log_arguments
def greet(name, age=None):
    print(f"Hello, {name}! Age: {age}")


print(add(3, 7))
greet("Alice", age=25)