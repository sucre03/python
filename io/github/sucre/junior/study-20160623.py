#20160623
###python2和python3的区别,在print上2没有(),而3有()
print('hello,world')
##一个逗号代表一个空格
print('hello world','do you like scala','yes but i like python better')
print('The quick brown fox', 'jumps over', 'the lazy dog')
print(333)
print(111+222)
name=input('please enter your name:')
print('hello',name)
print('1024*768=',1024*768)
a=-100
#这样看来python的语法好简单,缩进一律用4个空格,':'后面代表代码块
if a>=0:
    print(a)
else:
    print(-a)
print('I\' m ok')
print('I\'m learning\npython')
print('\\\n\\')

print(123)
print(456.789)
print('\'Hello,world\'')
print('\'Hello,\\\'Adam\\\'\'')
print('r\'\'\'Hello,')
print('Lisa!\'\'\'')
#//为取整,%为取余
print(7//2)
print(7%2)
#Python还允许用r''表示''内部的字符串默认不转义
