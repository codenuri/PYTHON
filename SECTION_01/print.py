# print 함수
print('AAA')            # 출력 후 개행
print('BBB', end='\t')  #
print('CCC', end='')    # 출력 후 개행 안함.
print()     # 개행


# 변수값 출력 방법
# 1. 변수 값만 출력
n1, n2, n3 = 10, 20, 30  # 여러개의 변수를 한줄로 만드는 표기
print(n1)
print(n1, n2, n3)           # 10 20 30 
print(n1, n2, n3, sep=', ') # 10, 20, 30


# 2. % 사용
print('n1 = %d' % n1 )
print('n1 = %d, n2 = %d' % (n1, n2) )


# 3. format 사용
print('n1 = {0},  n2 = {1}'.format( n1, n2 ))            # 문자열.format()
print('n1 = {v1}, n2 = {v2}'.format( v1 = n1, v2 = n2 ))


# 4. f-string 사용 - 강좌에서 사용하는 방법
print(f'n1 = {n1}, n2 = {n2}')
print(f'{n1 = }, {n2 = }') # debugging support for f-string. python 3.8 부터 지원
      # n1 = n1
