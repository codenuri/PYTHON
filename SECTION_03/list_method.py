# 1. len, del 
s = [0,1,2,3,4,5,6,7,8,9]

print(len(s))   # 10

del s[0]        # [1, 2, 3, 4, 5, 6, 7, 8, 9]        
del s[1:9:3]    # [1, 3, 4, 6, 7, 9]
print(s)        



# 2. append, insert
s = [1,3,5]
s.append(2)         # [1, 3, 5, 2]
s.append([5,6])     # [1, 3, 5, 2, [5, 6]]
s.insert(1, [7,8])  # [1, [7, 8], 3, 5, 2, [5, 6]]




# 3. remove, pop 
s = [1, 3, 5, 2, 4, 5, 6]

del s[0]    # 0번째 요소(1) 을 제거
s.remove(5) # 첫번째 나오는 5를 제거

print(s)    # [3, 2, 4, 5, 6]

n = s.pop() 
print(n)    # 6
print(s)    # [3, 2, 4, 5]




# 4. extend

s1 = [1,2,3]
s2 = [4,5]
s3 = s1 + s2   # s1 과 s2 자체가 변하지는 않음.
s1.extend(s2)  # s1 += s2 와 동일.

print(s1)  #[ 1,2,3,4,5]




# 5. count, index
s = [ 1, 3, 5, 7, 9, 1, 3, 5, 7, 9]

print( s.count(3) )         # 2 
print( s.index(3) )         # 1
print( s.index(3, 3, 8) )   # 6
#print( s.index(2) )        # ValueError: 2 is not in list



# 6. reverse
s = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

s.reverse() # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# 7. sort method vs sorted 내장함수

#s.sort()    # s 자체가 변경
#print(s)    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

s1 = sorted(s)  # s는 변하지 않고, 정렬된 새로운 list 반환
print(s)    # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(s1)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

