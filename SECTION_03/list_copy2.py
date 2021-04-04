import copy
s1 = [1, 2, [3,4]]
s2 = s1
s3 = s1.copy()
s4 = copy.deepcopy(s1) # 요소 까지 복사본

print(hex(id(s1))) # 100
print(hex(id(s2))) # 100
print(hex(id(s3))) # 200
print(hex(id(s4))) # 300

# 하지만 요소의 참조 는 동일 합니다.
print(hex(id(s1[2]))) # 1000
print(hex(id(s2[2]))) # 1000
print(hex(id(s3[2]))) # 1000
print(hex(id(s4[2]))) # 2000

s1[2].append(5)   

print(s1[2])    # [3, 4, 5]
print(s2[2])    # [3, 4, 5]
print(s3[2])    # [3, 4, 5]
print(s4[2])    # [3, 4]

print(hex(id(s1[0]))) # 5000
print(hex(id(s4[0]))) # 5000



