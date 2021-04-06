class A:
    def foo(self):
        return None

    def __add__(self, other):
        if not isinstance(other, A):
            return NotImplemented
        print('A __add__')

class B:
    def __radd__(self, other):
        print('B __radd__')

a1 = A()
a1.foo()

a2 = A()
b1 = B()
a1 + a2 # a1.__add__
a1 + b1 # b1.__radd__

