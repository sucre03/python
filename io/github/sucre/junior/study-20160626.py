#使用list和tuple
classmates=['Michal','Bob','John']
print(classmates,len(classmates),classmates[0],classmates[len(classmates)-1])
#insert
classmates.insert(1,'sucre')#insert要用到两个参数,一个是插入的位置,一个是插入的值
print(classmates[1])
#del
classmates.pop(1)
print(classmates[1])
#删除最后一个元素
classmates.pop()
print(classmates[len(classmates)-1])
#replace
classmates[1]='sucre'
print(classmates[1],classmates)
L=['Apple',13,True]
ss=['java','scala']
s=['asp','vb','c++',ss]
print(s,s[3][1])
LL=[]
print(len(LL))
#tuple与list差别就是:tuple一旦初始化就不能修改
t=('Michal','Bob','John')
print(t)
tt=('asp','vb','c',ss)
tt[3][1]='python'#这里改变的是ss的内容,但是ss在tt中的地址是没有改变的
print(tt)
only=(1,)#只有一个元素的情况下,要在元素的后面加个逗号,这是为了和单个数字进行区分
print(only)
#practise
PR = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(PR[0][0])
# 打印Python:
print(PR[1][1])
# 打印Lisa:
print(PR[2][2])

#条件判断
x=input('input your num:')
if int(x):#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
    print(x)
#practies
height = 1.75
weight = 80.5
bmi = weight/height**2#在python中,一个数的幂次用**来表示
print('%.1f' % bmi)
if bmi < 18.5:
    print('过轻')
elif bmi >=18.5 and bmi< 25:
    print('正常')
elif bmi >=25 and bmi < 28:
    print('过重')
elif bmi >=28 and bmi <32:
    print('肥胖')
else:
    print('严重肥胖')

##幂计算
import math #用开方函数时,要引入math
print(2**3,math.sqrt((2**2)),int(math.sqrt((3**2))))

#循环
books = ['java','scala','c','python','c++']
for name in books:
    print(name)
nums =[]
for n in range(101):#range为从0开始生成101个数,范围为[0,101)或[0,100]
    #print(n)
    nums.insert(n,n)#insert要用到两个参数,一个是插入的位置,一个是插入的值
#print(nums)
sum=0
for s in nums:
    sum+=s
print(sum)
while sum:#这里的条件和if一样,只要当前的值是非零数值、非空字符串、非空list等，就判断为True，否则为False
    sum -=1
print(sum)


