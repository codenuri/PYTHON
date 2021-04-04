s = 'ABCD'
n = 10
f = 3.4

it1 = iter(s)  # ok
#it2 = iter(n)  # error. 
#it3 = iter(f)  # error

#--------------------
r = range(1,10) # 1 ~ 9
it = iter(r)
#it2 = iter(it)
#print(hex(id(it)))
#print(hex(id(it2)))

print(type(r))
print(type(it))

print(next(it)) # 1 
print(next(it)) # 2
print(next(it))
print(next(it))

