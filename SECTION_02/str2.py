# 1. 문자열 생성
s1 = str('hello')
s2 = str()
s3 = 'hello'


# 2. + 와 * 연산
s1 = 'Python'
s2 = s1 + s1
s3 = s1 * 4

print(s2)       # PythonPython
print(s3)       # PythonPythonPythonPython

print('=' * 20) # ====================



# 3. [] 연산자
s = 'hello'
print( s[1] )   # e
#s[1] = 'x'      # TypeError: 'str' object does not support item assignment
                # immutable type

# 4. in 연산자
s = 'hello'
print('llo' in s) # True
print(len(s))   # 5



