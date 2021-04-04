d = { 'name' : 'kim', 'age' : 20, 'addr' : 'seoul'}

# 1. [] 와 get
print(d['addr'])
print(d.get('addr'))

#print(d['weight'])         # KeyError: 'weight'
print(d.get('weight'))      # None
print(d.get('weight', 'Unknown'))  # Unkown

d['weight'] = 30       # 새로운 key/value 생성
print(d)





# 2. keys(), values(), items()
d = { 'name' : 'kim', 'age' : 20, 'addr' : 'seoul'}

keys   = d.keys()
values = d.values()
items  = d.items()

print(keys)    # dict_keys(['name', 'age', 'addr'])
print(values)  # dict_values(['kim', 20, 'seoul'])
print(items)   # dict_items([('name', 'kim'), ('age', 20), ('addr', 'seoul')])



for k in keys:
    print(k, end=', ')  # name, age, addr

print()
for v in values:
    print(v, end=', ')  # kim, 20, seoul

print()
for i in items:
    print(i, end=', ')  # ('name', 'kim'), ('age', 20), ('addr', 'seoul')


# 3. in, clear
d = { 'name' : 'kim', 'age' : 20, 'addr' : 'seoul'}

print( 'age' in d ) # True

d.clear()
print(d)    # {}
