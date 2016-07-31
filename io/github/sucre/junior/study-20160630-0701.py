#递归函数
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式
def fact_iter(n, param):
    if n==1:
        return param
    return fact_iter(n-1,n*param)


def fact(n):
    return fact_iter(n,1)
print(fact(3))

#切片,取你想取的数,让循环下岗
l=list(range(100))
print(l[0:10])#注意,:分号的取值范围为左开右闭[)  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l[:10:3])#从0开始取10个数,每隔3个数取一个数,0可以省略[0, 3, 6, 9]
print(l[::3])#对于所有数,从0开始取数,每隔3个数取一个数
#[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
l1=l[:]#复制的功能,将l复制给ll
l2=l
print(l1)
print(l2)

#迭代
#在java中遍历map是很麻烦的,来看看python
m={'a':1,'b':2,'c':3}
for k,v in m.items():#遍历map的时候要用到items
    print(k,v)
#判断一个对象是否可迭代,可以通过collections模块的Iterable类型判断
from collections import Iterable
print(isinstance(m,Iterable),isinstance(123,Iterable))#Ture False
#遍历list的下标和值
l=['a','b','c']
for i,v in enumerate(l):
    print(i,v)
#遍历list中的tuple
lp=[(1,2),(3,4),('a','b'),('c','d')]
for x,y in lp:
    print(x,y)
#列表生成式
print([x*x for x in range(1,11)])
#只想要偶数
print([x*x for x in range(1,11) if x%2==0])
#二层循环
print([m+n for m in 'ABC' for n in 'XYZ'])
#practise
L1 = ['Hello', 'World', 18, 'Apple', None]
#使用str判断每个元素是不是字符串
L2 = [x.lower() for x in L1 if isinstance(x,str)]
print(L2)
'''
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

'''
#map与reduce
def f(x):
    return x*x
x=map(f,range(1,11))
print(list(x))
from functools import reduce
def add(x,y):
    return x+y

y=reduce(add,range(1,11))
print(y)

def mul(x,y):
    return 10*x+y
print(reduce(mul,range(1,11)))
#转字符串
print(list(map(str,range(1,11))))
#practise
#首字母大写,其它小写
def normalize(name):
    return name[0].upper() + name[1:].lower()
#也可以直接用函数
def normalize_(name):
    return name.capitalize()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
L3 = list(map(normalize_,L1))
print(L2,L3)
#lambda是指在创建匿名函数时使用
from functools import reduce

def prod(L):
    return reduce(lambda x,y:x*y,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
