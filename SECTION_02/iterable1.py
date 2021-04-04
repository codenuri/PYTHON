s = "ABCD"

#it = iter(s)
it = reversed(s)

print(type(s))    # class 'str'
print(type(it))   # class 'str_iterator'  
                  # class 'reversed'

print( next(it) ) # A
print( next(it) ) # B
print( next(it) ) # C
print( next(it, -1) ) # D
#print( next(it) ) # StopIteration
#print( next(it, -1) )
print( next(it, None) )

