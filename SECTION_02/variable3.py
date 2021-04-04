s1 = 'To Be Or Not To Be'
s2 = s1

s3 = 'To Be Or Not To'
s3 = s3 + ' Be'

print(s1)
print(s2)
print(s3)

print(hex(id(s1)))
print(hex(id(s2)))
print(hex(id(s3)))

# == 와 is 의 차이점
print(s1 == s3) # True
print(s1 is s3) # False



