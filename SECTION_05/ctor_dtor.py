class Car:
    def __init__(self, color = None, speed = None):
        print('constructor')

    def __del__(self):
        print('destructor')

c1 = Car()
c2 = Car(10, 20)

del c1 
print('=' * 20)
