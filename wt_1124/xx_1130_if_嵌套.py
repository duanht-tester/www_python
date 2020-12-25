# -*- encoding: UTF-8 -*-
# __author__ = 'lenovo'


num = int(input("请输入一个数字。"))

if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的数字可以整除3也可以整除2.")
    else:
        print("你输入的数字可以整除2，但不可以整除3.")
else:
    if num % 3 == 0:
        print("你输入的数字可以整除3，不可以整除2.")
    else:
        print("你输入的数字既不能整除2也不能整除3.")

