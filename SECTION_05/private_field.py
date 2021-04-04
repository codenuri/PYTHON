
class Point:
    def __init__(self):
        self.x = 1
        self._y = 2
        self.__z = 3

    def print(self):
        print(self.x, self._y, self.__z)

    def __goo(self):
        print('__goo')

p1 = Point()
p1.print()

p1._Point__goo()

print(p1.__dict__ )

print(p1.x)
print(p1._y)
#print(p1.__z)
print(p1._Point__z)


