class Base:
    def __init__(self):
        self.x = 100

    def print(self):
        print(self.x)

class Derived(Base):
    def __init__(self):
        super().__init__()

b = Base()
b.print()

d = Derived()
d.print()





