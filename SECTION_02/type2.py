n = 1020

#print( dir(int) )

print( n.bit_length() )

o = object()
#print( dir(object) )

print( issubclass(int, object))
print( issubclass(int, float))

print(int.mro())

print( isinstance(n, int )) # True
print( isinstance(n, object )) # True
