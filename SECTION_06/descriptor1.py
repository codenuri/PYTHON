class LogData:
    def __get__(self, obj, objType=None):
        print('__get__')
        return 20

class Sample:
    x = 10
    y = LogData()

n1 = Sample.x
n2 = Sample.y  # Sample.y.__get__( ... )

print(type(n1))  # int
print(type(n2))  # int   

Sample.y = 3.4

n3 = Sample.y
print(type(n3)) # float




