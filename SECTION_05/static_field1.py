class Point:
    cnt = 0   # Point.cnt = 0

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y



p1 = Point(1, 2)
p2 = Point(3, 4)

print(Point.__dict__)
#Point.cnt = 0  # Point.__dict__['cnt'] = 0
#print(Point.__dict__)
