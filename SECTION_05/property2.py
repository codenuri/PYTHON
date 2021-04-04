class People:
    
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def get_age(self):
        print('get_age')
        return self._age 

    def set_age(self, age):
        print('set_age')
        if age < 0:
            raise ValueError("age can not be negative")
        self._age = age

p = People('kim', 20)
print( p.get_age() )
p.set_age(-10)
