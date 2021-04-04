s = 'ABCDE'

print(s[0])  # A
print(s[4])  # E

print(s[-1]) # E
print(s[-0]) # s[0] 동일, A
print(s[-5]) # A

s = 'ABCDE'
n = s[0]    # ok
s[0] = 'X'  # error. immutable!
