# 1. indexing 
s = [1,2,3,[4,5,6]]

print(s[0])     # 1
print(s[-1])    # [4, 5, 6]
print(s[-1][0]) # 4



# 2. slicling
s = [0,1,2,3,4,5,6,7,8,9]

print(s[1:3])   # [1, 2]
print(s[1:9:3]) # [1, 4, 7]

sc = slice(1, 9, 3)
print(s[sc])    # [1, 4, 7]



# 3. unpacking
s = [1,'AB',[7,8]]

a, b, c = s

print(f'{a}, {b}, {c}')     # 1, AB, [7, 8]

#a, b = s        # ValueError: too many values to unpack (expected 2)
#a, b, c, d = s  # ValueError: not enough values to unpack (expected 4, got 3)


# 4. + 와 *
s1 = [1,2,3]
s2 = [4,5,6]

print(s1 + s2)      # [1, 2, 3, 4, 5, 6]
print(3 * s1)       # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(s1 * 3)       # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(s1 + s2 * 3)  # [1, 2, 3, 4, 5, 6, 4, 5, 6, 4, 5, 6]
print((s1 + s2) * 3)  # [1, 2, 3, 4, 5, 6,1, 2, 3, 4, 5, 6,1, 2, 3, 4, 5, 6]
 
s1 += s2            # s1 = s1 + s2
print(s1)           # [1, 2, 3, 4, 5, 6]

print( 3 in s1)     # True

