
def outer(x):
    y = 0
    print(hex(id(x)), hex(id(y)) )    

    def inner():
        nonlocal x, y
        x = 10
    
    return inner

f = outer(10)  # f = inner
print(f.__closure__)