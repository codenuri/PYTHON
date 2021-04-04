def foo():
    print('foo 1')
    yield 10
    print('foo 2')
    yield 20
    print('foo 3')
    yield 30

g = foo()
print(type(g))  # <class 'generator'>

print( next(g) )
print( next(g) )
print( next(g) )
print( next(g, -1) )
