import sys

n1 = 100
n2 = n1

print(sys.getrefcount(n1))

del n2

print(sys.getrefcount(n1))

print(n2)
