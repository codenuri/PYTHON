
def foo():
    global y
    global z
    x = 20   # 지역변수 x 생성   
    y = 20  
    z = 20   # 전역변수 z 생성    
    print(x)
    print(y)

x = 0
y = 0

print(x)    
print(y)    
#print(z) #error   
foo()

print(x)    
print(y)    
print(z) # ok
