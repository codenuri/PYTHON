def square(x):
    return x * x

s1 = [1, 2, 3, 4, 5]

for i in s1:   
    print(i, end=' ')

print()

m = map(square, s1) # 함수, 리스트 보관

for i in m:   
    print(i, end=' ')

print()


s3 = list( map(square, s1))
print(s3)  # [1,4,9,16,25]

print( list( map( lambda x:x*x, s1 )))

print( list( filter( lambda x : x%2== 0, s1 )))

# 지능형 리스트가 더 편리
s4 = [square(x) for x in s1]
print(s4)

