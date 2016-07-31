#函数参数
#python中的默认参数与scala中的默认参数可以说是一样一样的
def power(x,y=2):
    return x**y
print(power(3),pow(4,3))
#scala里面是允许这样写的,看来python里也是支持的,不按默认顺序写的时候,要指定参数key
print(power(y=5,x=3))
#默认参数一定要指向不可变对象
def add_s(L=[]):
    L.append('S')
    return L
print(add_s(),add_s(),add_s())#输出结果:['S', 'S', 'S'] ['S', 'S', 'S'] ['S', 'S', 'S'],不是我们想要的
def add_sc(L=None):
    if L is None:
        L=[]
    L.append('S')
    return L
print(add_sc())#一直是['S']
#可变参数,用*来表示,可变参数在函数内部*号会自动组装成一个tuple
def getBooks(*names):
    for name in names:
        print(name)
getBooks('java','python','scala')
ns=['c','c++','c#']
getBooks(ns)
getBooks()
#关键字参数,用**表示,关键字参数在函数内部会自动组装为一个dict(map)
def person(name,age,**extend):
    print('name:',name,'age:',age,'other:',extend)
    extend['addtest']='test'#在里面修改pi的值,不会影响到传入前的pi,这里与java的传引用不一样,这里应该是传值,而不是传引用
person('sucre',20,city='beijing')

pi={}
pi['city']='bj'
pi['job']='engineer'
pi['gender']='male'
person('sucre',20,**pi)#这里要用**进行输入,否则什么也不会输出
print(pi)
#命名关键字参数
#命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name,age,*,city,job):
    print(name,age,city,job)
#命名关键字参数必须传入参数名,它和位置参数不一样
person('sucre',20,city='bj',job='engineer')
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name,age,*extend,city,job):
    print(name,age,extend,city,job)
person('sucre',20,'ha','ha',city='bj',job='engineer')#结果:sucre 20 ('ha', 'ha') bj engineer

#小结
'''
要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''