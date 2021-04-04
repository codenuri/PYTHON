n1 = 10
n2 = 10

print(hex(id(n1)))
print(hex(id(n2)))

s1 = [10]
s2 = [10]

print(hex(id(s1)))
print(hex(id(s2)))

print(hex(id(s1[0])))
print(hex(id(s2[0])))