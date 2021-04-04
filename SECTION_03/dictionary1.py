# 1. 생성
d1 = dict(name='kim', age = 20, addr = 'seoul')
d2 = {  'name':'kim', 'age':20, 'addr':'seoul'} # d1 과 동일

print(d1)
print(d2)


# 2. 키값 중복
d = { 'name' : 'kim' , 'name' : 'park', 'age' : 20}
print(d)


# 3. [] 를 사용한 요소 접근
print(d['age'])
