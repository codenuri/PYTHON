class LogData:  
    def __set_name__(self, cls, name):
        print('__set_name__')
        self.name = '_' + name  # x.name = '_x'
                                # y.name = '_y'
    def __get__(self, obj, objType=None):
        print('__get__')
        #return obj._y 
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        print('__set__')
        #obj._y = value
        setattr(obj, self.name, value )

class Sample:
    x = LogData()   # x.__set_name__(x, Sample, 'x')
    y = LogData()   # y.__set_name__(y, Sample, 'y')
#    z = LogData()   # z.__set_name__(z, Sample, 'z')

    def __init__(self):
        self.x = 10 # self.x.__set__( self.x, self, 20 )  
        self.y = 20 # self.y.__set__( self.y, self, 20 ) 

sam = Sample()
print( sam.x)  # 10
print( sam.y)  # 10

