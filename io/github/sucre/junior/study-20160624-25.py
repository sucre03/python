#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#python字符串
print('包含中文的str')
#ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('是'))#这里只支持写一个汉字,因为ord是将一个character进行转换
print(chr(65))
print('\u4e2d\u6587')#用16进制表示汉字
print('abc'.encode('ascii'))#结果中的b表示byte
print('中文'.encode('utf-8'))
print(b'abc'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
#一个中文3个字节
print(len('abc'),len('中文'),len(b'abc'),len(b'\xe4\xb8\xad\xe6\x96\x87'))
#格式化
print('Hello, %s' % 'world')
print('Hello,%s,you have did %d.' % ('sucre',100000))
#注意占位,2d表示位数2位,后面的数字如果占位不到2位,其它位用空格代替
#03d表示位数3位,后面的数字如果占位不到3位,其它位用0代替
#.2表示小数点后两个有效
print('%2d-%03d' % (3,1),'%.2f' % 3.1415926,'%020d' % 1)
print('Age:%s.Gender:%s' %(25,True) )
#practise
s1=72
s2=85
r=(s2-s1)/s1*100
print('%.1f%%' % r)