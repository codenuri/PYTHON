import sys 

n1 = 10
n2 = n1

print( n1 is n2)  # True
print( sys.getrefcount(n2))

n1 = n1 + 1 

print( n1 is n2)  # False
print( sys.getrefcount(n2))

