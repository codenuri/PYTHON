def add1(x, y):
    return x + y

add2 = lambda x, y : x + y

print(type(add1))
print(type(add2))

print(add1)
print(add2)

print(add1(1,2))
print(add2(1,2))

add2.__dict__['x'] = 100
print(add2.x)