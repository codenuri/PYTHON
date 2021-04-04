import time

def foo(a, b, c):
    print(a, b, c)
    time.sleep(2)

def goo():
    print('goo')
    time.sleep(3)

def chronometry(f, *args, **kwargs ):
    start = time.time()
    f(*args, **kwargs)         
    end   = time.time()
    print(f'elapsed : {end-start}')

#chronometry(goo)
chronometry(foo, 1, 2, 3)
chronometry(foo, 1, 2, c = 3)
