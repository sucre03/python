# sorted
# 这里有一个重要的内部函数itemgetter
students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 对名称进行排序
from operator import itemgetter

print(sorted(students, key=itemgetter(0)))
# 按分数进行排序
print(sorted(students, key=itemgetter(1), reverse=True))

print(sorted(students, key=lambda t: t[1]))


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2016-07-05')


now()
# 这个和log(now())是等价的
print(log(now()))

import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2016-07-06')


now()
