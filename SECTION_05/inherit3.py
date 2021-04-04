class A:
    def foo(self):
        print('A foo')

class B:
    def foo(self):
        print('B foo')

class C(A, B):
    pass 

c = C()
c.foo()
print(C.mro())

super(C, c).foo()  # A.foo(c)
super(A, c).foo()  # B.foo(c)

    