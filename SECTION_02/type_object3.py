import time

n = 0
start = time.time()

print( dir(time) )
#print( dir(int) )
#print( dir(n) )

f = getattr(time, 'time')
f()  # time.time()

print(f())
print(time.time())



