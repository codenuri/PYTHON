
class Test:

    def foo(self):
        print('Test foo')

    @staticmethod
    def goo():
        print('Test goo')


t = Test()
t.foo()     # foo(t)
Test.foo(t) # 

# static 메소드 호출
Test.goo()  # 1. 클래스이름으로 호출
t.goo()     # goo(t)


