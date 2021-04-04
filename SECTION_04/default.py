def f1(a, b = 0, c = None):
    print(a, b, c)

f1(1, 2, 3)  # 1, 2, 3
f1(1, 2)     # 1, 2, None
f1(1)        # 1, 0, None

#def f2(a, b = 0, c):
#    print(a, b)

#f2(1, 2)

def f3(a, b = 0, *,  c):
    print(a, b)

f3(1, c = 2)