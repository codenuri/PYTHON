def foo():
    print('foo')

print(foo.__dict__)

foo.__dict__['x'] = 10

print(foo.__dict__)

foo.y = 20  # foo.__dict__['y'] = 20

print(foo.__dict__)

def goo():
    print('goo')

foo.goo = goo
foo.goo()
