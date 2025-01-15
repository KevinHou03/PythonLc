class School:
    pass  # 空代码块


class HKY:
    name = 'Kai-yuan Hou'
    age = 19
    gender = 'male'
    married = False

    # 实例方法
    def drink(self):  # 定义在内部的称为方法，self表示调用该方法的实例对象自身
        print('drink water')

    # 静态方法
    @staticmethod
    def method():  # 静态方法不能用self
        print('method')

    # 类方法
    @classmethod
    def cm(cls):
        print(260)

    '''
    实例方法用于操作实例的状态，静态方法用于与类的状态无关的通用操作，类方法用于操作和访问类的状态
    '''

    # constructor __init__是初始化专用
    def __init__(self, name, age):
        self.name = name
        self.age = age


def eat():  # 定义在外部的成为函数
    print('eat', HKY.name)


# 创建hky对象，根据init来创建
hky1 = HKY('hky', 8)
hky2 = HKY('hxg', 9)
# 执行他的方法
hky1.drink()
hky1.method()
print(hky1.age)
print(hky2.age)
HKY.method()

hky1.age = 99
print(hky1.age)


# python 　可以在类外面更改属性


class Student:
    def __init__(self, age):
        self.__age = age
        self.setAge(age)

    def setAge(self, age):
        if 0 <= age <= 120:
            self.__age = age

    def getAge(self):
        return self.__age


# 如果不希望类属性age在类外部被访问更改，在赋值的时候在前面加__

stu1 = Student(10)


# print(stu1.__age) 报错 因为不可访问和更改双下划线类属性


# 继承
class Person(Student):  # 这里表示Person继承了Student
    def __init__(self, name, age, race):
        super().__init__(age)  # 这个必须有，在子类构造器里面调用父类构造器
        self.name = name
        self.age = age
        self.race = race

    def info(self):
        print(self.name, self.age)


class Teacher(Student):
    def __init__(self, subject, age):
        super().__init__(age)
        self.subject = subject

    @classmethod
    def Teaching(cls, studentnumber):
        print("i am teaching", studentnumber, "student")


person = Person('hky', 18, 'Asian')
print(person.age, person.name, person.race)

person.info()  # 这就是调用父类的方法了


# 多重继承
class Children(Teacher, HKY):
    def __init__(self, subject, age):
        super().__init__(subject, age)  # 调用父类Teacher的构造器，父类的父类不用管
        self.subjct = 'Math'
        self.age = age

    def Teaching(cls, studentnumber):
        super().Teaching(7)  # 这是利用super关键字调用父类的方法原件，没有的话 只会输出下面这一行的东西
        print('this is override')

    def __str__(self):
        return "str是一个内置函数，将你创造的对象转化为一个字符串"


child = Children('English', 7)
print(child.age, child.subjct)  # 依旧是math，不是english
child.Teaching(8)
print(child)  # 输出str函数内容


def use(obj):
    obj.Teaching(8)


use(Teacher)  # 在teacher类中 Teaching是一个类方法  @classmethod ， 所以可以直接把类放进去
use(child)  # 而在children类中 Teaching是一个实例方法 没有用  @classmethod 所以不能放类，但是可以放 实例


# 运算符的重载 一般情况下两个类的对象不能相加，但是一旦我们重载运算符，就可以了
class Computer:
    def __init__(self, price):
        self.price = price

    def __add__(self, other):
        return self.price + other.price  # 或者return（self.price,other.price)分别得到两个价格的一个元组

    def __len__(self):
        return len(str(self.price))  # 重载len方法使其返回price的长度,但是他只能返回str类型，所以我们cast到str


com1 = Computer(4700)
com2 = Computer(2800)
com3 = Computer(199)
print(com1 + com2)  # 7500
print(len(com1))

'''
在 Python 中，对象的创建过程分为两个主要阶段：__new__ 和 __init__。
__new__ 负责实际地创建对象，返回一个新的实例；而 __init__ 负责初始化对象的状态。
__init__ 在 __new__ 创建实例后调用，接收 __new__ 返回的实例以及其他参数作为参数。
'''


class Customer:
    def __new__(cls, *args, **kwargs):
        newInstance = super().__new__(cls)
        return newInstance

    def __init__(self, name):
        self.name = name


obj = Customer('Jack')
print(obj.name)
'''
cls/__new__是类对象
obj/init是实例对象
'''
