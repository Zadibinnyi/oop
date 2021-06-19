import time


def decorator(func):
    def wrapper(arg):
        start = time.time()
        b = func(arg)
        stop = time.time()
        result = stop - start
        print (f'Elapsed time: {result}')
        return b
    return wrapper


@decorator
def fib (n: int) -> int:
    a = 0
    b = 1

    if n == 1:
        return a 
    elif n == 2:
        return b

    for _ in range(3, n+1):
        a, b = b, a + b 

    return b

print(fib(500000))
    