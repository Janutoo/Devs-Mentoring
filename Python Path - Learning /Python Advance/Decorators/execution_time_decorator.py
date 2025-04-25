import time 

def timethis(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(round(end_time-start_time, 2))
        return result
    return wrapper



@timethis
def timer(x, y):
    time.sleep(2)
    print(x**20 + y **20)


timer(5, 6)