class Sentence:

    def __init__(self, s):
        self.words = s.split()  

    def __len__(self):
        return len(self.words)

    def __getitem__(self, idx):
        return self.words[idx]

s = Sentence('To Be Or Not To Be')

print( s[1] )  # s.__getitem__(1)

