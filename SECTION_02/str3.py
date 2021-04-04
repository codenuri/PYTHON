# 1. 모든 멤버 함수 조사
print( dir(str) )


# 2. upper, lower
s = 'ABcd'
s1 = s.upper()  # 'ABCD'
s2 = s.lower()  # 'abcd'

print(s)    # 'ABcd'  s는 변화 없음
print(s1)   # 'abcd' 
print(s2)   # 'ABCD'  




# 3. count, find, index
s = 'hello'

print(s.count('l')) #  2 회
print(s.find('l'))  #  2 번째 위치
print(s.index('l')) #  2

print(s.find('a'))  # -1
#print(s.index('a')) # ValueError



# 4. strip, lstrip, rstrip
s = ' hello '
print( '|' + s          + '|')  # | hello |
print( '|' + s.strip()  + '|')  # |hello|
print( '|' + s.lstrip() + '|')  # |hello |
print( '|' + s.rstrip() + '|')  # | hello|


# 5. replace
s1 = 'python is simple'
s2 = s1.replace('simple', 'complicated')
print(s1)   # python is simple
print(s2)   # python is complicated


# 6. join
s1 = 'ABCDEFG'
s2 = '/'.join(s1)
print(s2)       # A/B/C/D/E/F/G


# 7. split
s = 'To be or not to be, that is the question'
st = s.split()
print(st)   # ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']


# 8. 
s = 'hello'
#print( s.len() ) # AttributeError: 'str' object has no attribute 'len'
print( len(s) )  # ok