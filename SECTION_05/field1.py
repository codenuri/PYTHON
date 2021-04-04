class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
        print('Point ctor')

p1 = Point()
p2 = Point()
p3 = Point()

p1.__dict__['x'] = 0
p1.y = 0

print( p1.__dict__)
print( p2.__dict__)

print(p1.x) # 0
#print(p2.x) # Error