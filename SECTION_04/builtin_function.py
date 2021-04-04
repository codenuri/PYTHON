import sys

def add(x, y):
    return x + y

print(add.__dict__)
#print(print.__dict__)

print(add)
print(print)

print(sys.getsizeof(add))
print(sys.getsizeof(print))

print(dir(add))
print(dir(print))

