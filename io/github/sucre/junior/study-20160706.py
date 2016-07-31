import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World!')
    elif len(args) == 2:
        print('Hello %s!' % args[1])
    else:
        print('too many args')


if __name__ == '__main__':
    test()

test()


# 在python私有方法和变量定义时用 _打头


def __getGold(num):
    print('give you %s gold' % num)


def __getMoney(num):
    print('give you %s money' % num)


def choice(num):
    if len(num) == 1:
        __getMoney(num)
    else:
        __getGold(num)


choice('300')


class Student(object):
    def __init__(self, name, score):
        self.__name = name  # 加上双下划线就变成私有属性了
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))


aa = Student('bob', 60)
bb = Student('clare', 90)

aa.print_score()
bb.print_score()

aa.name = 'sucre'
aa.score = 100
aa.print_score()


class Animal(object):
    def run(self):
        print("animal is running......")


class Dog(Animal):
    def run(self):
        print("dog is running.....")
    #pass

Dog().run()

print(dir('ABC'))