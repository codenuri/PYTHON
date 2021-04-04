class Test:

    def foo(self):
        print('Test foo')
        ct = self.__class__

    @staticmethod
    def goo():
        print('Test goo')

    @classmethod
    def hoo(cls):
        print('Test hoo')

t = Test()

t.foo()
t.goo()   # Test.goo()
t.hoo()   # Test.hoo(t.__class__)

Test.foo(t)
Test.goo()
Test.hoo() # Test.hoo(Test)




