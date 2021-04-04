class Plus:
    
    def __call__(self, x, y):
        return x + y

p = Plus()

n = p(1, 2)  # p.__call__(1, 2)

print(n)

