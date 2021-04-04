s = [1, 2, [3,4] ] # list
t = (1, 2, [3,4] ) # tuple

# 1. tuple 항목을 추가/삭제 할수 없습니다.
s.append(3)  # ok 
#t.append(3)  # error 

del s[0]    # ok  
#del t[0]    # error  

# 2. tuple 에 각 요소(참조)에 새로운 객체를 할당할수 없다.
s[2] = 10   # ok 
#t[2] = 10   # error 

# 4. tuple 은 imutable 하지만 
# 요소 자체가 immutable 한 것은 아니다.
t[2].append(5)

print(t)    # (1, 2, [3, 4, 5] )


