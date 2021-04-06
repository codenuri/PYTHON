import ctypes

# dll 파일
#path = './sample.dll'
#mod  = ctypes.windll.LoadLibrary(path)

# so 파일
path = './libsample.so'
mod  = ctypes.cdll.LoadLibrary(path)

print(mod)   # CDLL 타입의 객체

# 1. add 호출
add = mod.add
add.argtypes = (ctypes.c_int, ctypes.c_int)
add.restype = ctypes.c_int

print(add)
print(add(1,2))
