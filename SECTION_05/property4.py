class People:
    
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        print('get_age')
        return self._age 

    @age.setter
    def age(self, age):
        print('set_age')
        if age < 0:
            raise ValueError("age can not be negative")
        self._age = age


p = People('kim', 20)
print( p.age  )
p.age = -10
