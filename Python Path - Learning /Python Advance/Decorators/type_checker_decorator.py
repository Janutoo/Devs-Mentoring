
def check_type(expected_type):
    def decorator(func):
        def wrapper(arg):
            if not isinstance(arg, expected_type):
                raise TypeError(f"{expected_type} we got {arg}")
            return func(arg)
        return wrapper
    return decorator            


@check_type(int)
def print_square(num):
    print(num ** 2)


print_square(4)
print_square("4")