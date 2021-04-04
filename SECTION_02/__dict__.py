class Base:
    base_member = 100

class AAA(Base):
    sx = 10
    def __init__(self):
        self.x = 10
        self.y = 20

    def f1(self):
        pass

    def f2(self):
        pass 

print(AAA.__dict__.keys())
print('=' * 50)
print(dir(AAA))
print('=' * 50)
a = AAA()
print(a.__dict__.keys())
print('=' * 50)
print(dir(a ))
