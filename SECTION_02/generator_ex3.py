f = open('generator_ex3.py', 'r')

it = iter(f)
print(next(it), end='')
print(next(it), end='')
print(next(it), end='')
f.close()
print('=' * 20)


def file_reader(file_name):
    for row in open(file_name, "r"):
        yield row

g = file_reader('generator_ex3.py')

print(next(g), end='')
print(next(g), end='')
print(next(g), end='')
print(next(g), end='')
