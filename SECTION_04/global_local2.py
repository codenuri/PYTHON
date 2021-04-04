gx = 1

def outer(ox):
    oy = 3

    def inner():
        global   gx
        nonlocal ox 
        gx = 10
        ox = 10
        oy = 10

    def check():
        print(gx, ox, oy)

    return inner, check

f1, f2 = outer(2)
f1() # inner
f2() # check
