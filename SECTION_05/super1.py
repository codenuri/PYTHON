class X:
    def __init__(self):
        print('X __init__')
    
class A(X):
    def __init__(self):
        print('A __init__')
    
class C(A):
    def __init__(self):
        print('C __init__')

c = C()
super(C, c).__init__()
super(A, c).__init__()
