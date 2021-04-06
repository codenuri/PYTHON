import builtins 

builtins.print('hello')
__builtins__.print('hello')

#for s in dir(__builtins__):
#    at = getattr(__builtins__, s) 
#    print(f'{s:>25} : {type(at)}')

import sys

#print(sys.modules)
m = sys.modules[__name__]

print(m)

