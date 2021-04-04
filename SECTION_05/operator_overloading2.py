class A:
    def __add__(self, other):
        if isinstance(other, A):
            print('A __add__')
            return self
        else:
            return NotImplemented
 
class B:
    def __add__(self, other):
        print('B __add__')

    def __radd__(self, other):
        print('B __radd__')

a = A()
b = B()

#a + b   # a.__add__(b)
a + a 

'AA' + b # str.__add__
