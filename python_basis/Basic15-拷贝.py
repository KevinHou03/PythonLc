# 1 变量的赋值
import math
a = 1
b = a
print(id(a))
print(id(b))


class cpu:
    pass


class disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk

        '''
        浅拷贝（Shallow Copy）是指创建一个新对象，该对象是原始对象的副本，但只复制原始对象的元素的引用，而不是元素本身。
        换句话说，浅拷贝创建了一个新的容器对象，然后将原始对象的元素放入其中，但是元素本身并没有被复制
        '''

'''
cpu = CPU是创建了一个类对象，相当于类本身 就算用深拷贝也是不变的，因为引用的是相同的类对象
cpu = CPU()是创建了实例对象，这样才能进行正确的深拷贝
'''
cpu1 = cpu()
disk1 = disk()
computer1 = Computer(cpu1, disk1)

import copy

computer2 = copy.copy(computer1)
print(computer1, id(computer1.cpu), id(computer1.disk))
print(computer2, id(computer2.cpu), id(computer2.disk))
'''
<__main__.Computer object at 0x1036956a0> 140313820742384 140313820776816
<__main__.Computer object at 0x1036b7340> 140313820742384 140313820776816 对象是新的，但是元素地址不变
'''

computer3 = copy.deepcopy(computer1)
print(computer1, id(computer1.cpu), id(computer1.disk))
print(computer3, id(computer3.cpu), id(computer3.disk))
'''
<__main__.Computer object at 0x1073a82e0> 4416100000 4416179360
<__main__.Computer object at 0x1073d7f40> 4416263216 4416679600  所有的都不同了
'''





