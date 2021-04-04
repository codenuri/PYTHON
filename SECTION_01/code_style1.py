# 1. ; 은 붙여도 되고 안붙여도 됩니다.
print('A')
print('B');
print('B'); print('C')


# 2. 하나의 문장을 여러줄로 표기
n = 1 +     # error
    2       

# \ 를 사용하면 여러줄 표기 가능
n = 1 + \   
    2 


# 3. [], (), {} 안에서는 여러줄 표기 가능
print(
    'A')


# 조건식에는 ()가 있어도 되고 없어도 가능
# {} 대신 한 칸 이상의 들여 쓰기 사용
n = 10
if n % 2 == 0:
    print('even number')
    print('even number')
else:
    print('odd number')


