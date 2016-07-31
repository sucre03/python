# __str__
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object is %s ' % self.name


s = Student('sucre')
print(s)

# __iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100:
            raise StopIteration  # 退出循环
        return self.a


for n in Fib():
    print(n)


class Chain(object):
    def __init__(self, path=''):#相当于java的构造方法
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):#相当于java的toString()
        return self._path

    def __call__(self,path):
        return Chain('%s/%s' % (self._path,path))
print(Chain().status.user.timeline.list)