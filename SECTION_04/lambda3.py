x = 10

f1 = lambda y : x + y        # 실행시 x 평가
f2 = lambda y, x = x : x + y # 이순간 x 평가

x = 20

print(f1(1))    # 21
print(f2(1))    # 11


f3 = lambda x, y : x if x > y else y

print(f3(10, 5))
print(f3(6, 8))

f4 = lambda x, y : x if x > y else y if y > 0 else 0