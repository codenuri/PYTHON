class LogData:
    def __get__(self, obj, objType=None):
        print('__get__')
        return 20

    def __set__(self, obj, value):
        print('__set__')


class Sample:
    x = 10
    y = LogData()

sam = Sample()


print(Sample.__dict__)
print(sam.__dict__)   # {}

n1 = sam.x      # read

print(sam.__dict__)   # {}

sam.x = 20     # writer

print(sam.__dict__)   # { 'x' : 20 }
print(sam.x)          # 20


sam.y = 100     # 객체의 __dict__ 에 y를 추가하지 않고
                # sam.y.__set__ 호출
print(sam.__dict__) # { 'x' : 20 }
n = sam.y       # sam.y.__get__ 호출





