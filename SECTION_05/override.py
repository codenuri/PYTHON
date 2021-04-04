class Base:
    def f1(self):   print('Base f1')
    def _f2(self):  print('Base _f2')
    def __f3(self): print('Base __f3') # _Base__f3()

    def foo(self):
        self.f1(); 
        self._f2(); 
        self.__f3() # self._Base__f3()

class Derived(Base):
    def f1(self):   print('Derived f1')
    def _f2(self):  print('Derived _f2')
    def __f3(self): print('Derived __f3')
                    # _Derived__f3()

d = Derived()
d.foo()
print(Base.__dict__)
print(Derived.__dict__)
