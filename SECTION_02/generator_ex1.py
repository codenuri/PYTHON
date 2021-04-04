# 짝수를 무한히 반환
def infinite_even():
    num = 0
    while True:
        yield num
        num += 2

g = infinite_even()

print(next(g))
print(next(g))
print(next(g))

