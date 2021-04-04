class LogData:
    def __get__(self, obj, objType=None):
        print('__get__')
        return obj._y

    def __set__(self, obj, value):
        print('__set__')
        obj._y = value


class Sample:
    y = LogData()

    def __init__(self):
        self.x = 10


sam1 = Sample()
sam2 = Sample()

sam1.y = 20  # sam1.y.__set__(sam1.y, sam1, 20 )
sam2.y = 30  # sam2.y.__set__(sam2.y, sam2, 30 ) 


print(sam1.x)  # 필드 x를 직접 접근
print(sam1.y)  # __get__ 통해서 sam1._y 
print(sam2.y)





