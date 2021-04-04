# pass
def foo():  # void foo() {}
    pass 

class Car:
    pass

# else 가 반복문(for, while)에도 놓일수 있다.
cnt = 10
while cnt < 10:
    print('AAA')
else:
    print('cnt >= 10')

# 한줄에 2개의 변수를 만들수 있다.
n1, n2 = 10, 20
n1, n2 = n2, n1 
print(n1, n2) # 20, 10


