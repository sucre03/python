# type()

class Hello(object):
    def hello(self, name='world'):
        print('Hello,%s.' % name)


h = Hello()
h.hello()
print(type(h))


def fn(self, name='world'):
    print('Hello,%s.' % name)


'''
type有三个参数:
1、class的名称；
2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
'''
Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello()


try:
    r = 10 / 0
except ZeroDivisionError as e:
    print('except is %s' % e)
finally:
    print('finally...')
