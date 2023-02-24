import time


def timer(func):
    def wrapper(*args, **kwargs):
        time.time()
        result = func(*args, **kwargs)
        time.time()
        return result

    return wrapper
