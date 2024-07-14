from functools import wraps

def timer(func):
    from time import time
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time()
        res = func(*args, **kwargs)
        t2 = time()
        delta_t = (t2 - t1)
        print(f"{func.__name__} finished execution in {str(delta_t) + 's' if delta_t >= 1 else str(delta_t * 1000) + 'ms'}")
        return res
    return wrapper

@timer
def print_name(name):
    for i in range(9000000):
        pass

print_name("scieph3r")
