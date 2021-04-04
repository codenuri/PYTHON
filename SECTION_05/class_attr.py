import sys

class Point:
    def __init__(self):
        print('Point ctor')

p1 = Point()
p2 = Point()


print(sys.getsizeof(Point))
print(sys.getsizeof(p1))
print(sys.getsizeof(p2))

ct = p1.__class__

p3 = ct()  # p3 = Point()