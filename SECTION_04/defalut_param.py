
# def foo(x = 10):
"""
def add_sharp(s = []):
    s.append('#')
    return s
"""
def add_sharp(s = None):
    if s is None:
        s = []
    s.append('#')
    return s

s1 = [1,2,3]
print( add_sharp(s1) ) # [1,2,3,'#']

print( add_sharp.__defaults__ ) # []
print( add_sharp() )   # ['#']

print( add_sharp.__defaults__ ) # ['#']
print( add_sharp() )   # ['#']

print( add_sharp.__defaults__ ) # ['#', '#']

print( add_sharp() )   # ['#']