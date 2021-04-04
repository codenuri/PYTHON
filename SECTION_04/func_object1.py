import sys

def add(x, y):
    return x + y

print(hex(id(add)))
print(sys.getrefcount(add))
print(sys.getsizeof(add))

f = add
f(1,2)  # add(1,2)

add = 10
print(add)



