def foo():
    raise NameError('Unknown Name')

#foo()

try:
    foo()
except:
    print('catch exception')


try:
    foo()
except NameError:
    print('catch exception')


try:
    foo()
except NameError as e:
    print(f'catch exception : {e.args}')


try:
    foo()
except NameError as e:
    print('catch exception(NameError)')
    
except TypeError as e:
    print('catch exception(TypeError)')


try:
    foo()
except (NameError, TypeError) as e:
    print('catch exception')



