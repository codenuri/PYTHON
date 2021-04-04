import sys
import ctypes

class Int(ctypes.Structure):
    _fields_ = [ ('ob_refcnt', ctypes.c_long),
                 ('ob_type',   ctypes.c_void_p),
                 ('ob_size',   ctypes.c_ulong),
                 ('ob_digit',  ctypes.c_long)]

#n1 = 10
n1 = 100000000000000000000

p1 = Int.from_address(id(n1))
print(sys.getrefcount(n1))
print(p1.ob_refcnt)
print(p1.ob_size)

