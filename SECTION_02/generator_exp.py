# generator
def foo():
    for i in range(0, 100, 5):
        yield i

g1 = foo()

g2 = ( i for i in range(0, 100, 5) )

print( type(g2)) # class 'generator' 

print(next(g2)) # 0
print(next(g2)) # 5
print(next(g2)) # 10

g3 = ( i +j for i in range(10) 
            for j in range(11,20) )

print(next(g3)) # 0 + 11
print(next(g3)) # 0 + 12
print(next(g3)) # 0 + 13
