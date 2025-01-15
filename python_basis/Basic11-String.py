"""
字符串的驻留机制
Str是不可变类型的序列
"""

# 性质1：abc的地址是一样的,注意==比的是内容，is比的是地址
a = 'Python'
b = "Python"
c = '''Python'''
print(a is b is c)  # True
print(a.join(b))

"""
字符串的基本操作
/index()查找substring第一次出现的位置，找不到抛error
/rindex()查找substring最后一次出现的位置，找不到抛error
/find()查找substring第一次出现的位置，找不到-1
/rfind()查找substring最后一次出现的位置，找不到-1
"""

d = "hello,hello"
print(d.index('lo'))  # 3
print(d.find('lo'))  # 3
print(d.rindex('lo'))  # 9
print(d.rfind('lo'))  # 9

'''
/upper()全转大些
/lower()全转小写
/swapcase()有大转小，有小转大
/capiyalize()第一个大写，其余的小写
/title()每个单词第一个大写，其余小写

执行以上操作之后，是new了一个新对象，地址值不一样了，== True, is False
'''

"""
center()居中对齐 第一个参数是宽度，第二个是填充符 默认都是空格，设置宽度小于实际宽度会返回原str
ljust()左对齐 第一个参数是宽度，第二个是填充符
rjust()右对齐第一个参数是宽度，第二个是填充符
zfill() 右对齐，左边用0填充 只有一个参数，就是宽度
"""

d = "hello,hello"
print(d.center(20, '*'))  # ****hello,hello*****
print(d.ljust(20, '*'))  # hello,hello*********
# 填充符不写，默认空格

"""
split() 从左边开始分割，默认劈分字符是空格字符串，返回的是一个列表
"""
e = "hello world Python"
list1 = e.split()
print(list1)  # ['hello', 'world', 'Python']

e1 = "hello|world|Python"
list2 = e1.split(sep='|')
print(list2)

print(e1.split(sep='|', maxsplit=1))  # ['hello', 'world|Python'] 只有第一个，后面的就不管了

print(e.rsplit())  # ['hello', 'world', 'Python']左右分割结果一样
print(e.rsplit(sep='|', maxsplit=1))  # ['hello world Python']

"""
isidentifier()判断str是不是合法
isspace()判断是否全部由空白字符，如回车换行等，组成
isalpha()是否全部字母
isdecimal() 全部由十进制数字
isnumeric()全部由数字
isalnum()全部由数字和字母
"""

"""
replace()第一个参数指定被替换者，第二个是替换物，第三个参数可选，为最大替换次数。
join() 将列表或者元组中字符串合并为一。
"""
e = "hello world Python"
print(e.replace('hello', 'HELLO'))

e = "hello world Python"

list3 = ['hello', 'java', 'Python']
print(''.join(list3))  # 直接连起来

list4 = [1, 2, 3, 4]
print('Love'.join(list3))  # 用love吧他们连起来 helloLovejavaLovePython

print('*'.join('Python'))  # P*y*t*h*o*n

"""
比大小
"""

a = 'apple'
b = 'app'
print(a > b)  # True

"""
字符串str切片
"""
s = 'hello,python'
print(s[:5])  # hello 没有指定开始，从0开始
print(s[6:])  # python 没有指定结束，切到最后

print(s[1:5:1])  # ello 1 开始 5结束 1步长
print(s[::2])  # hlopto
print(s[::-1])  # nohtyp,olleh倒着来。
print(s[-6::1])  # python

"""
String的格式化
%s字符串 %i or %d 整数 %f 浮点
使用%，
"""
# 1
name = 'Kevin'
age = 19

print("my name is %s, my age is %d  years old" % (name, age))  # my name is Kevin, my age is 19 years old

# 2 use {}占位符

print('my name is {0}, my age is {1}'.format(name, age))  # my name is Kevin, my age is 19 years old

# 3 f-string
print(f'my name is {name}, my age is {age}')
