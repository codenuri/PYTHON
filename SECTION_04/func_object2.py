def foo(a = 10, b = 20, *, c = 30, d = 40):
    '''
        foo 함수에 대한 설명 
    '''    
    print('foo')


print(foo.__doc__)

print(foo.__name__)         # 함수이름
print(foo.__qualname__)     # 클래스이름.함수이름
print(foo.__defaults__)
print(foo.__kwdefaults__)
