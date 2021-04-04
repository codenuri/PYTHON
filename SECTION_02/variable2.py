import sys

n = 10
f = 3.4

print(n)
print(hex(id(n)))   # 객체의 주소 출력

print( sys.getrefcount(n) ) # 객체의 참조계수 출력

print( sys.getsizeof(n) )   # 객체의 메모리 크기 28
print( sys.getsizeof(f) )   # 24

print( type(n) )
print( isinstance(n, int))  # True
print( isinstance(f, int))  # False
print( type(n) is int )