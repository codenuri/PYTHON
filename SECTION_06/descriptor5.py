class LogData:
    def __get__(self, obj, objType=None):
        print('__get__')
        return obj._y

    def __set__(self, obj, value):
        print('__set__')
        obj._y = value

class Sample:
    x = LogData()
    y = LogData()

    def __init__(self):
        self.x = 10  # x 필드 생성
        self.y = 20  # self.y.__set__( self.y, self, 20 )

sam1 = Sample()
sam2 = Sample()

print(sam1.x) # 10
print(sam1.y) # 20




