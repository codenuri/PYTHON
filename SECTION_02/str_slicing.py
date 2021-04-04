s = 'ABCDEFGHIJK'

c = s[0]  # A


sc = slice(1, 4) # slice 객체를 생성하고
s1 = s[sc]       # [] 연산자의 인자로 slice 객체 전달
print(s1)        # BCD


print( s[ slice(1, 7, 2) ] )    # BDF
print( s[ slice(-1, -8, -2) ] ) # KIGE
print( s[ slice( 5 ) ] )        # ABCDE
print( s[ slice( len(s) ) ] )   # ABCDEFGHIJK

# [:] 또는 [::]
print( s[1:7] )         # BCDEFG,   slice(1, 7)    
print( s[1:7:2] )       # BDF,      slice(1, 7, 2)    
print( s[-1:-8:-2] )    # KIGE,     slice(-1, -8, -2) 
print( s[5::] )         # FGHIJK
print( s[::] )          # ABCDEFGHIJK
print( s[-1::-1])       # KJIHGFEDCBA      

