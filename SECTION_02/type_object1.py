n1 = 10
n2 = 20

print(hex(id(n1)))
print(hex(id(int))) # 타입 객체의 주소

DWORD = int 
n1 = int

n3 = DWORD(10) # int(10)
n4 = n1(10)    # int(10)

int = n2
#n5 = int(10) # error. int 는 타입 아님
print(int)   # 20



