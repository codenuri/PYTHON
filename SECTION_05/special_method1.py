
class Sentence:

    def __init__(self, s):
        self.words = s.split()  

    def __len__(self):
        return len(self.words)

s = Sentence('I am a boy')

print( s.words ) # ['I', 'am', 'a', 'boy']


print( len('hello') )     # 5
print( len([1,2,3,4,5]) ) # 5

print( len( s ) )         # 4
print( s.__len__())



