def f1(*args):
    print(args)

f1(1,2,3)       # f1( (1,2,3) )
#f1(1,2,3, a = 10) # error


def f2(**kwargs):
    print(kwargs)

f2(a = 10, b = 20) 
f2(1, a = 10, b = 20) # error

