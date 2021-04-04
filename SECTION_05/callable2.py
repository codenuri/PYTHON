#cnt = 0

def add(x, y):
    add.cnt += 1  # add.cnt = add.cnt + 1
    return x + y

add.cnt = 0
n1 = add(1,2)


class Plus:

    def __init__(self):
        self.cnt = 0

    def __call__(self, x, y):
        self.cnt += 1
        return x + y

p = Plus()
n2 = p(1, 2)  

print(p.cnt)





