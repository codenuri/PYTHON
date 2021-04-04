class add_emoticon:

    def __init__(self, emoticon):
        self.emoticon = emoticon

    def __call__(self, func):
        self.func = func
        def inner(*args, **kwargs):
            print(self.emoticon, end='')
            return self.func(*args, **kwargs)

        return inner


#@add_emoticon         # say_hello = add_emoticon(say_hello)
@add_emoticon('^-^;')  # say_hello = add_emoticon('^-^;')(say_hello)
def say_hello(name):
    print(f'hello, {name} !')

say_hello('kim')
print(type(say_hello))

