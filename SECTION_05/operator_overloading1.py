class Sentence:

    def __init__(self, s):
        self.words = s.split()  

    def __add__(self, other):
        print('__add__')

    def __iadd__(self, other):
        print('__iadd__')

    def __radd__(self, other):
        print('__radd__')

s1 = Sentence('To Be Or')
s2 = Sentence('Not To Be')

s = s1 + s2  # s1.__add__(s2)

s1 += s2     # s1 = s1 + s2

s = s2 + 'AA'  # s2.__add__('AA')

s = 'AA' + s2  # s2.__radd__('AA')
        # str.__add__



