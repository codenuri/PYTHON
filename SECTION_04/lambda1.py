s1 = [ 'banana', 'kiwi', 'apple']

s2 = sorted(s1)

print( s1 )  # [ 'banana', 'kiwi', 'apple']
print( s2 )  # [ 'apple', 'banana', 'kiwi']

def foo(x):
    return len(x)

print( sorted(s1, key=foo) )   # ['kiwi', 'apple', 'banana']
print( sorted(s1, key=lambda x:len(x) ) )
print( sorted(s1, key=len ) )

# 각 요소의 문자열을 뒤집어서 정렬 기준으로 사용
print( sorted(s1, key=lambda x : x[-1::-1] ) )
