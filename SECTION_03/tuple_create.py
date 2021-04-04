# 1. 타입 이름(tuple) 사용
t1 = tuple()           # ()
t2 = tuple('ABCD')     # ('A', 'B', 'C', 'D')
t3 = tuple(range(5))   # (0, 1, 2, 3, 4)
t4 = tuple([1,2,3,4])  # (1, 2, 3, 4)



# 2. ()로 생성
t1 = ()     # ()
t2 = (1)    # <class 'int'>
t3 = (1,)   # <class 'tuple'>



# 3. () 가 없어도 된다.
t1 = (1, 2, 3)  
t2 = 1, 2, 3    # t1 과 동일 합니다.
t3 = 1,         # tuple 입니다.
t4 = 1          # int 입니다.
t5 = 1, 2



# 4. generator expression
s1 = [i for i in range(10) if i % 2 == 0]    # 지능형 리스트
t1 = (i for i in range(10) if i % 2 == 0)    # 주의 t1은 튜플이 아닙니다.

print(type(s1)) # <class 'list'>
print(type(t1)) # <class 'generator'>

# generator expression 을 사용하려면 
# tuple 타입 이름을 사용해야 합니다.
t1 = tuple((i for i in range(10) if i % 2 == 0))
t2 = tuple( i for i in range(10) if i % 2 == 0 )  # t2와 동일

print(t2)   # (0, 2, 4, 6, 8)
print(t3)   # (0, 2, 4, 6, 8)

s1 = [1, 2]
s2 = [3, 4]

t4 = tuple([i, j] for i in s1
                  for j in s2 )

print(t4)   # ([1, 3], [1, 4], [2, 3], [2, 4])