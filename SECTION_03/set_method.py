s1 = {1,2,3}

print(len(s1))

# 1. 요소 추가. add, update
s1.add(4)               # { 1, 2, 3, 4 }
s1.update({3,4,5,6})    # { 1, 2, 3, 4, 5, 6}

print(s1)   # { 1, 2, 3, 4, 5, 6}



# 2. 요소 제거
s1.remove(5)
print(s1)   # { 1, 2, 3, 4, 6}

# 3. 집합 연산
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8,9}

# 교집합
print(s1.intersection(s2))  # {4, 5}
print(s1 & s2)              # {4, 5}

# 합집합
print(s1.union(s2))         # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1 | s2)              # {1, 2, 3, 4, 5, 6, 7, 8, 9}

#  차집합
print(s1.difference(s2))    # {1, 2, 3}
print(s1 - s2)              # {1, 2, 3}