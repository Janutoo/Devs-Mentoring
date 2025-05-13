def star_decorator(func):
    def wrapper(*args, **kwargs):
        print("*" * 30)  
        result = func(*args, **kwargs)  
        print("*" * 30) 
        return result  
    return wrapper


@star_decorator
def display_text(text):
    print(text)


display_text("Hello, world!")