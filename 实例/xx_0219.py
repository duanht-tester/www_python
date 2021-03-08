#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @file   : Cartesian.py
# @author : shlian
# @date   : 2018/5/29
# @version: 1.0
# @desc   : 用python实现求笛卡尔积

# import itertools
#
# class Cartesian(object):
#
#     def __init__(self):
#         self._data_list = []
#
#     def add_data(self, data=[]):   # 添加生成笛卡尔积的数据列表
#         self._data_list.append(data)
#
#     def build(self):  # 计算笛卡尔积
#         for item in itertools.product(*self._data_list):
#             print(item)
#
#
# if __name__ == "__main__":
#     car = Cartesian()
#     car.add_data([1, 2, 3, 4])
#     car.add_data([5, 6, 7, 8])
#     car.add_data([9, 10, 11, 12])
#     car.build()

# 以下实例为学习Python的第一个实例，即如何输出"Hello World!"：
# 该实例输出 Hello World!
# print('Hello World!')

# 以下实例为通过用户输入两个数字，并计算两个数字之和：
# 用户输入数字
# num1 = input('请输入一个数字：')
# num2 = input("输入第二个数字：")
# # 求和
# sum = float(num1) + float(num2)
# # 显示计算结果
# print("数字{0} 和 {1} 相加结果为： {2}".format(num1, num2, sum))

"""
在该实例中，我们通过用户输入两个数字来求和。使用了内置函数 input() 来获取用户的输入，input()
返回一个字符串，所以我们需要使用 float() 方法将字符串转换为数字。
两数字运算，求和我们使用了加号 (+)运算符，除此外，还有 减号 (-), 乘号 (*)
, 除号 (/), 地板除 (//) 或 取余 (%)。更多数字运算可以查看我们的Python 数字运算。

我们还可以将以上运算，合并为一行代码：
"""
# print("两数之和为 %.1f" % (float(input('输入一个数字：'))+ float(input('输入第二个数字：'))))

# 尝试写了一个报错重新输入的处理处理:
# while 1:
#     x = input('输入第一个数：')
#     y= input('输入第二个数：')
#     try:
#         sum = float(x) + float(y)
#
#     except:
#         print("输入的数字格式不正确,请重新输入")
#         continue
#
#     else:
#         print("数字{0} 和 {1} 相加结果为： {2}".format(x, y, sum))
#         break

# 平方根，又叫二次方根，表示为〔√￣〕，如：数学语言为：√￣16=4。语言描述为：根号下16=4。
# 以下实例为通过用户输入一个数字，并计算这个数字的平方根：
# num = float(input('输入一个数字：'))
# num_sqrt = num ** 0.5
# print("%0.3f 的平方根为 %0.3f" % (num, num_sqrt))

# 在该实例中，我们通过用户输入一个数字，并使用指数运算符 ** 来计算该数的平方根。
# 该程序只适用于正数。负数和复数可以使用以下的方式：

import cmath

# num = float(input('输入一个数字：'))
# num_sqrt = cmath.sqrt(num)
# print("{0} 的平方根为 {1:0.3f}+{2:0.3f}j".format(num, num_sqrt.real,
#                                            num_sqrt.imag))
# 该实例中，我们使用了 cmath (complex math) 模块的 sqrt() 方法。

# 求复数的平方根。
# a = float(input('输入第一个数：'))
# b = float(input('输入第二个数：'))
# num_sqrt = cmath.sqrt(complex(a, b))
# print('{0:0.3f}+ {1:0.3f}j 8的平方根为 {2:0.3f}+{3:0.3f}j'.format(a, b, num_sqrt.real, num_sqrt.imag))

"""
先假设我们会用input读取一个输入，它是一个字符串格式的，然后数字常用的是
有小数点的浮点数float和整型int,再考虑可能输入带负号，那么求出的平方根
是复数 complex, 所以可以分类讨论，下面的代码缺点是还没考虑到 long 型的。
可以依次输入 ： -2.56 -9 1.44 16 来检验。
"""

import cmath

# def sqrt():
#     # 计算实数和复数平方根  # 导入复数数学模块 isinstance(num ,  (float,int) )
#     num = input('输入第一个数自:')
#     if num.__contains__('-') and num.__contains__('.'):  # 负数、浮点数
#         num_sqrt = cmath.sqrt(float(num))
#         print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(float(num), num_sqrt.real, num_sqrt.imag))
#     elif num.__contains__('-'):  # 负数、整数
#         num_sqrt = cmath.sqrt(int(num))
#         print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(int(num), num_sqrt.real, num_sqrt.imag))
#     else:
#         if num.__contains__('.'):   # 非负数、浮点数 整数
#             num_sqrt = float(num) ** 0.5
#             print(' %0.3f 的平方根为 %0.3f' % (float(num), num_sqrt))
#         else:  # 非负数、整数
#             num_sqrt = int(num) ** 0.5
#             print(' %0.3f 的平方根为 %0.3f' % (int(num), num_sqrt))
#
# sqrt()

# 异常报错+正数+负数
try:
    num = float(input("请输入一个数字"))
except:
    print("输入的数字格式不正确,退出")
else:
    if num >= 0:
        num_sqrt = num**0.5
        print("{0}的平方根是{1:.3f}".format(num, num_sqrt))
    else:
        num_sqrt=cmath.sqrt(num)
        print("{0}的平方根是{1:.3f}+{2:.3f}j".format(num, num_sqrt.real, num_sqrt.imag))



