def f1(a, b, c):
    print(a, b, c)

s = [1,2,3]
t = (1,2,3)
d = {'a':1, 'b':2, 'c':3 }

f1(1, 2, 3) # ok
#f1(s)       # error.
f1(*s)      # ok. f1(1, 2, 3)
f1(*t)      # ok. f1(1, 2, 3)
f1(*d)      # ok. f1('a', 'b', 'c')
f1(**d)     # ok. f1( a = 1, b = 2, c = 3)