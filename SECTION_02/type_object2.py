n1 = 10

print(n1)   # 10
print(int)  # <class 'int'>

def foo(x):
    return float

ret = foo(int)

DWORD = type(n1)
print( DWORD is int) # True
print( type(n1) )    # <class 'int'>

n = 10
print( type(n) is int )     # True
print( type(n) is object )  # False

print( isinstance(n, int) ) # True
print( isinstance(n, object) ) # True


