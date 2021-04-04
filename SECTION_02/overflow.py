import sys 

n1 = 10
n2 = 10000000000    # 0 10개
n3 = 100000000000000000000      # 0 20개
n4 = n3 * n3

print(n3)
print(n4)

print(sys.getsizeof(n1)) # 28
print(sys.getsizeof(n2)) # 32
print(sys.getsizeof(n3)) # 36
print(sys.getsizeof(n4)) # 44