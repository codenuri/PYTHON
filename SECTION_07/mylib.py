def add(x, y):
    return x + y

def sub(x, y):
    return x - y

class Car:
    def __init__(self):
        print('Car __init__')
    
    def Go(self):   
        print('Car Go')
        
    def Stop(self): 
        print('Car Stop')

print(__name__)