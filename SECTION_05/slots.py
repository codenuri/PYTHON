class Point1:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
p1 = Point1(1, 2)
p1.z = 100
print(dir(p1))

class Point2:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
p2 = Point2(1, 2)
#p2.z = 100
print(dir(p2))

