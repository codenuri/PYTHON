def foo():
    print('foo')

f = foo             # 1. 함수를 변수에 대입합니다.
print( f == foo )   # 2. 동일 비교의 대상


def f1(f):
    f()

f1(foo)         # 2. 함수를 인자로 전달합니다.

def f2():
    return foo  # 3. 함수를 반환 합니다.

f2()()





