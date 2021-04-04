class Base:

    def foo(self):
        print('Base foo')

    def goo(self):
        print('Base goo')        


class Derived(Base):

    def goo(self):
        print('Derived goo')

        Base.goo(self)
        super().goo()

d = Derived()
d.foo()
d.goo()
