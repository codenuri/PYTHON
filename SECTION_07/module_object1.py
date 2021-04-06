import mylib3
import sys

print(hex(id(mylib3)))
print(type(mylib3))

print(sys.getsizeof(mylib3))


print(mylib3.__doc__)
print(mylib3.__class__)
print(mylib3.__name__)
print(mylib3.__file__)
