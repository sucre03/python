#函数
#什么时候为true,什么时候为false,可以参看study-20160626中的条件判断
#在python中,程序都是根据Truth Value Testing来判断对错的,看看官方的说法
'''
Any object can be tested for truth value, for use in an if or while condition or as operand of the Boolean operations below. The following values are considered false:

None

False

zero of any numeric type, for example, 0, 0.0, 0j.

any empty sequence, for example, '', (), [].

any empty mapping, for example, {}.

instances of user-defined classes, if the class defines a __bool__() or __len__() method, when that method returns the integer zero or bool value False.

All other values are considered true — so objects of many types are always true.

Operations and built-in functions that have a Boolean result always return 0 or False for false and 1 or True for true, unless otherwise stated. (Important exception: the Boolean operations or and and always return one of their operands.)
'''
print(bool(0),bool(''),bool(1))
#也可以这样
b = bool
print(b(1))
#自定义函数
def self_abs(x):
    if x >=0:
        return x
    else:
        return -x
print(self_abs(888))
#也可以提前预测一下传入参数的类型
def self_abs_1(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
#print(self_abs_1('A'))
#空函数,即什么都不做的函数,也叫占位函数
#修改一下上面的代码,先占着位,等想好了功能再去实现
def sel_abx(x):
    pass
#返回多值
#这里其实是用到了python中的tuple
import random
def getPosition():
    x = random.randint(0,100)
    y = random.uniform(0,100)
    return x,y
print(getPosition())#从输出的结果中可以看出是tuple
#practise
import math
def quadratic(a,b,c):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
        raise TypeError('bad operand type')
    if a !=0 and b**2 > 4*a*c:
        x=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        y=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        return x,y
    else:
        pass
print(quadratic(2, 3, 1),quadratic(1, 3, -4))