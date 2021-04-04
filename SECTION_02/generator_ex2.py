# 소수 얻기
import math

def is_prime(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i = i + 2
    return True


def prime_generator():
    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield n

g = prime_generator()

print( next(g) )   # 2
print( next(g) )   # 3
print( next(g) )   # 5
print( next(g) )   # 7
print( next(g) )   # 11