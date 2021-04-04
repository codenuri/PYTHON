def f1(a, b):
    print(a, b)

f1(1, 2)     # ok
#f1(1, 2, 3)  # error


def f2(a, *args):
    print(a, args)

f2(1, 2, 3, 4) # f2( 1, (2,3,4) )
f2(1, 2, 3)    # f2( 1, (2,3) )
f2(1, 2)       # f2( 1, (2,) )
f2(1)          # f2( 1, () )

def f3(a, *args, c):
    print(a, args, c)

#f3(1,2,3,4) # error
f3(1,2,3,c=4) # 

print(1,2,3, sep='\t' )