class Sentence:

    def __init__(self, s):
        self.words = s.split()  

    def __str__(self):
        return f'Sentence({self.words})'


    def __add__(self, other):

        if isinstance(other, Sentence):
            return Sentence( ' '.join(self.words + other.words))
            
        elif isinstance(other, str):
            s = self.words.copy()
            s.append(other)
            return Sentence(' '.join(s))
        return NotImplemented


    def __radd__(self, other):
        if isinstance(other, str):
            s = self.words.copy()            
            s.insert(0, other)
            return Sentence(' '.join(s))
        return NotImplemented


s1 = Sentence('To Be Or')
s2 = Sentence('Not To Be')

print(s1 + s2)      # s1.__add__(s2)
print(s1 + 'AAA')   # s1.__add__('AAA')
print('AAA' + s1)

1 + s1