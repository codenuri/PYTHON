import mylib3

f = getattr(mylib3, 'add')

f(1,2)

c = getattr(mylib3, 'Car')
print(type(c))
c1 = c()  # Car()

print(dir(mylib3))

for s in dir(mylib3):
    at = getattr(mylib3, s) 
    print(f'{s:>13} : {type(at)}')