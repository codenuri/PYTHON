# 연산자 정리
n = 10
n = n + 1
n += 1
#++n     # 버그, ++ 연산자는 없다.

# walrus operator - python 3.8
def foo():
    return 10

#if (ret = foo()) == 10:
if (ret := foo()) == 10:
    print('10')

# &&, ||, ! 대신 and, or, not
#b = True && False
#b = True || False
#b = !True
b = True and False
b = True or False
b = not True

# in 연산자
s = 'ABCDE'
b = 'AB' in s
print(b)
