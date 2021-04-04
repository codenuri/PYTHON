def add(x, y):
    return x + y


# 2개 이상의 값을 리턴하려면
def f1():
    return [1,2,3,4,5]

ret       = f1() # [1,2,3,4,5]
a,b,c,d,e = f1() # 1,2,3,4,5
a,*b,c    = f1() # 1,[2,3,4],5

print(a, b, c)

def f2():
    return 1,2,3,4,5 # (1,2,3,4,5)

ret       = f2() # (1,2,3,4,5)
a,b,c,d,e = f2() # 1,2,3,4,5
a,*b,c    = f2() # 1,[2,3,4],5

print(a, b, c)

import glob
st = glob.glob('C:\\windows\\system32\\*.exe')

print(st)


def f3():
    print('A')

ret = f3()
print(ret) # None
