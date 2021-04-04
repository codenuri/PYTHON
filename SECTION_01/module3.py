import time

start = time.time()
t = sum( range(1,1000000) )
print(t)
end = time.time()

print(f'time : {end-start}')


start = time.time()
t = 0
for i in range(1,1000000):
    t = t + i
print(t)
end = time.time()

print(f'time : {end-start}')
