class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x = {self.x}, y = {self.y}'    

    def __repr__(self):
        return f'Point({self.x}, {self.y})'    
        
p1 = Point(1,2)

print( p1 )  # p1 => "문자열"
print(str(p1))
print(repr(p1))

p2 = eval(repr(p1)) # eval('Point(1,2)')
print(p2)
