class Point:
    cnt = 0   
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        Point.cnt += 1

p1 = Point(1, 2)
p2 = Point(3, 4)

# 1. 클래스 이름으로 접근
Point.cnt = 100

# 2. 객체이름으로 접근
print(p1.cnt)   # 100

p1.cnt = 200
print(Point.cnt) # 100
print(p1.cnt)    # 200
print(p2.cnt)    # 100