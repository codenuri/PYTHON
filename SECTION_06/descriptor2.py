class LogData:
    def __get__(self, obj, objType=None):
        print('__get__')
        return 20


class Sample:
    x = 10
#    y = LogData()

    def __init__(self):
        self.y = LogData()


sam = Sample()

#n1 = Sample.y  # 클래스 이름으로 접근
n2 = sam.y     # 객체 이름으로 접근

print(type(n2)) # LogData

