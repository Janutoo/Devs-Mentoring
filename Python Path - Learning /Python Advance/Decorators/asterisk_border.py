
def star_decorator(func):
    def wrapper(*args, **kwargs):
        print(10 * '*')
        func(*args, **kwargs)
        print(10 * "*")
    return wrapper

class StartDecorator:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwds):
        print(10 * "*")
        self.func()
        print(10 * "*")

        

@star_decorator
def display_messgae():
    print("Hello World!")

@StartDecorator
def display_messgae02():
    print("Hello World!")

display_messgae()
display_messgae02()
