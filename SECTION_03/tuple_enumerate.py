s = ['apple', 'banana']

it = iter(s)

print(next(it))  # apple
print(next(it))  # banana

e = enumerate(s)

print(next(e)) # (0, 'apple')
print(next(e)) # (1, 'banana')


for t in s:
    print(t, end=' ') # apple  banana

print()

for t in enumerate(s):
    print(t, end=' ') # (0, apple)  (1, banana)

print()
for idx, n in enumerate(s):
    print(idx, n) 





    
