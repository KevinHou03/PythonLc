# try-except 结构
try:
    a = int(input('Enter the first number'))
    b = int(input('Enter the second number'))
    result = a / b
    print('The result is ', result)
except ZeroDivisionError:
    print('Zero as divisor')
except ValueError:
    print('Only number allowed')
except BaseException:  # 这个是最general的case了
    print('wrong')
else:  # 只有没有错误才会执行以下语句
    print('End of execution')
finally:
    print('Finally will be executed no matter the program is wrong or correct')
# 如果else没有抛出异常 则执行else 抛出异常 则执行except
