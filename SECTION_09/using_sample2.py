import ctypes

path = './libsample.so'
mod  = ctypes.cdll.LoadLibrary(path)

# 1. void sub(double, double, double*)
sub = mod.sub
sub.argtypes = (ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double))
sub.restype = None

outparam = ctypes.c_double()   # c 언어와 호환되는 double 객체

ret = sub(3.2, 2.2, outparam)  

print(outparam.value)   # 1.0





# 2. int sum(int* arr, int sz)
sum = mod.sum
sum.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)
sum.restype = ctypes.c_int

# python list => C 배열로 변경
s = [1,2,3,4,5,6,7,8,9,10] 

arr = (ctypes.c_int * len(s))(*s)

print( sum(arr, len(s)) ) 






# 3. int getarea(Rect* r)
class Rect(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('w', ctypes.c_int),
                ('h', ctypes.c_int)]

getarea = mod.getarea
getarea.argtypes = (ctypes.POINTER(Rect),)  # 구조체 포인터,  튜플로 사용
getarea.restype = ctypes.c_int

r = Rect(0, 0, 5, 10)

print( getarea(r) ) # 50



