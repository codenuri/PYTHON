import builtins

#print(dir(builtins))

# 문자열로 부터 타입 객체 얻기
i = getattr(builtins, 'int')

n = i(10) # int(10)
print(n) 
