# 1. 타입이름(list)을 직접 사용하는 경우
s1 = list()  # []

s2 = list('ABCDEFG') # list( iterable object )
                     # ['A', 'B', 'C', 'D' ] 
s3 = list(range(10)) # [0,1,2,3,4,5,6,7,8,9]   

# generator expression => generator 생성 => iterable
s4 = list((i for i in range(10) if i % 2 == 0)) 
s5 = list( i for i in range(10) if i % 2 == 0 ) # () 가 없어도 가능.

print(s4) # [0,2,4,6,8]

# 2. [] 표기법을 사용하는 경우
s1 = []       # list()
s2 = [1, 2, 3]
s3 = [1, 3.4, 'AAA']
s4 = [1, 2, [3, 4, 5]]  # list 를 포함하는 list


# 3. 지능형 리스트(list comprehension)
s1 = [ i for i in range(10) if i % 2 == 0 ]     
print(s3)  # [0,2,4,6,8]


s1 = 'AB'
s2 = '12'
s3 = [[v1, v2] for v1 in s1 for v2 in s2 ]

print(s3)   # [['A', '1'], ['A', '2'], ['B', '1'], ['B', '2']]

# 개행을 사용하면 가독성이 좋다.
s3 = [[v1, v2] for v1 in s1 
               for v2 in s2 ]



