class Base:
    def __init__(self):
        print('Base __init__')

class A(Base):
    def __init__(self):
        print('A __init__')
        Base.__init__(self)
    
class B(Base):
    def __init__(self):
        print('B __init__')
        Base.__init__(self)

class C(A, B):
    def __init__(self):
        print('C __init__')
        A.__init__(self)
        B.__init__(self)

c = C()
