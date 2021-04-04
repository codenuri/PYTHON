s = 'print(n)'

# len()
n = len(s) # 8

# eval()
eval(s)    # print(n)

# dir() 
st = dir(s) # [ method  ] 
print(st)
print(s.islower()) # True

# hex(), oct(), bin()
n = 10
print(n, hex(n), oct(n), bin(n))


# open
f = open('built_in_function2.py')
s = f.read()
print(s)

# help()
help(open)