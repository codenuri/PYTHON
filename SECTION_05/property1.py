class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

p = People('kim', 20)

print(p.age)
p.age = -10
