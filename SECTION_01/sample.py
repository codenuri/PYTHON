import functools

# 주석입니다.
'''
여러줄 주석입니다.
'''

# 변수
n1 = 10
n2 = 0x10
s1 = 'Hello' # 문자열은 ' ' 로 해도 되고
s2 = "Hello" #          " " 를 사용해도 된다.
s2 = 3.4    # 하나의 변수에 다양한 타입의 
            # 객체를 담을수 있다

# 시퀀스 
st = [1,2,3,4]  # list
tp = (1,2,3,4)  # tuple
se = {1,2,3}    # set
dic = { 'mon':'월요일', 'tue':'화요일', 'wed':'수요일'} 
            # dictionary

print(st[0], tp[1], dic['mon']) # 1, 2, '월요일'


# 제어문
if n1 % 2 == 0:
    print('even')
   

# 반복문 
for i in range(10):
    print(i)

cnt = 0
while True:
    print('hi')
    cnt = cnt + 1
    if cnt == 3:
        break


# 함수 
def add(x, y):
    return x + y
    

# 클래스 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1,2)   # 객체를 생성하는 모양 

# 예외 처리
try:
    add(1,2)
except ValueError as e:
    print('Error')

# generator, coroutine
def nextOdd():
    n = 1
    while True:
        yield n
        n = n + 1
        
# 비동기
import asyncio

async def foo():
    print('foo 중단... 5초간 대기')
    await asyncio.sleep(5)
    print('foo 재개')
    


