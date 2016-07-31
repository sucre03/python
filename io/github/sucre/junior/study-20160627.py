#使用dict和set
#dict相当于java中的map
d={'Michal':98,'Bob':89,"John":99}
print(d['Bob'])
d['sucre']=100
print(d)#每次执行时map中的内容顺序都不一样
if 'sucre' in d:#判断key是否存在
    print(d['sucre'])
#另一种方法,如果key不存在,则返回指定的值或默认值None
print(d.get('clare'),d.get('clare',-1))
#map删除时也是用pop,和list一样
d.pop('sucre')
print(d)
#set
s=set([2,3,4,5,6])
print(s)
s.add(8)
print(s)
#通过remove删除
s.remove(3)
print(s)
#set的交集或并集
s1=set([1,2,3,4,5])
s2=set([3,4,5,6,7])
#s1 and s2取s2 --两集合and,取后者
#s1 or s2取s1  --两集合or,取前者
print(s1&s2,s1|s2,s1 and s2,s2 and s1,s1 or s2,s2 or s1,s1-s2,s1^s2,s2-s1)
#str的不可变性
a='abc'
b='Abc'
c=a.replace('a','A')
print(a,b,c,b==c)#说明a的值根本没有发生改变