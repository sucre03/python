##使用__slots__限制只能添加指定的属性
# 定义的属性仅对当前类实例起作用，对继承的子类是不起作用的


class Student(object):
    __slots__ = ('name', 'age')


s = Student()
s.name = 'sucre'
s.age = '20'


# s.score='100'


class JuniorStudent(Student):
    pass


j = JuniorStudent()
j.score = '100'


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432,'1024*768 = %d ?'% s.resolution
