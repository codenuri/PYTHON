def f(a,b,c,d,e):
    print(a,b,c,d,e)

f(1, 2, 3, 4, 5)
f(a = 1, b = 2, c = 3, d = 4, e = 5)

f(1, 2, c = 3, d = 4, e = 5)
f(1, 2, d = 4, c = 3, e = 5)

#f(1, 2, c = 4, d = 3, 5) # error

def f2(a, /, b, *, c):
    print(a,b,c)

#f2(1, 2, 3)   # error c= 3 밖에 안됨.
#f2(a = 1, b = 2, c = 3)  # error. a=1 이 안됨
f2(1, 2, c = 3)         # ok
f2(1, b = 2, c = 3)     # ok
#f2(1, b = 2, 3)         # error

print('AAA', end='')