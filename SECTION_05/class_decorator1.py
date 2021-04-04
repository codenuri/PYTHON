class add_emoticon:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(':-) ', end='')
        return self.func(*args, **kwargs)

@add_emoticon         
def say_hello(name):
    print(f'hello, {name} !')

say_hello('kim')
print(type(say_hello))

