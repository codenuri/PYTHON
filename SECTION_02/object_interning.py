n1 = 256
n2 = 256
n3 = 98765678
n4 = 98765678

print(hex(id(n1)))
print(hex(id(n2)))
print(hex(id(n3)))
print(hex(id(n4)))

n1 += 1
n2 += 1
n3 += 1
n4 += 1

print(hex(id(n1)))
print(hex(id(n2)))
print(hex(id(n3)))
print(hex(id(n4)))