class Base:
    def __init__(self):
        print('Base __init__')

class A(Base):
    def __init__(self):
        print('A __init__')
        super().__init__() # super(self.__class__, self)
    
class B(Base):
    def __init__(self):
        print('B __init__')
        super().__init__()

class C(A, B):
    def __init__(self):
        print('C __init__')
        super().__init__() # super(self.__class__, self)

c = C()
