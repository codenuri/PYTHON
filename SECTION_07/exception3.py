
s = [ e for e in dir(__builtins__) 
        if e.endswith('Error')]

for er in s:
    print(er)

class DBError(Exception):
    pass 
