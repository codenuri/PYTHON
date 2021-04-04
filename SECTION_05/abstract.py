from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def Draw(self):
        pass 

class Rect(Shape):
    def Draw(self):
        pass

r = Rect()
#s = Shape()