# 1. [] 연산
t1 = ( 1, 2, 'ABC', [3,4], 5, 6, 7 )

print(t1[0])        # 1
print(t1[1:5:2])    # (2, [3, 4])
#t1[0] = 20      # error


# 2. +, *
t2 = ('A', 'B')

print(t2 + t2)  # ('A', 'B', 'A', 'B')
print(t2 * 3 )  # ('A', 'B', 'A', 'B', 'A', 'B')



# 3. len, count, index
print(len(t2))         # 2
print(t2.count('A') )  # 1
print(t2.index('A') )  # 0


# 4. unpacking
t = (1, 2, [3,4])

a, b, c = t

print(f'{a}, {b}, {c}') # 1, 2, [3, 4]


# 5. list 보다 메소드가 적다
print(dir(t))


