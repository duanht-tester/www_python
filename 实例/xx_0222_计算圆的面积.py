#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
圆的面积公式为 ：
S=πr*r
公式中 r 为圆的半径。
"""

# # # 定义一个方法来计算圆的面积
# def findArea(r):
#     PI = 3.142
#     return PI*(r*r)
#
# # 调用方法
# print('圆的面积为 %.6f' % findArea(5))

# 计算圆的面积

# PI = 3.14159265
# r = input('输入一个半径r的值：')
# if r.isdigit():  # 判断是否是数字字符串
#     s = PI*pow(float(r), 2)  # 参考方法，使用 pow() 函数：
#     print("半径为 {} 的圆面积为：{:.3f}".format(r,s))
# else:
#     print("输入错误！")


# 创建函数，可重复输入且非数字不会中断。
import math

# def cirarea():
#     r = 0
#     while r <= 0:
#         print('请输入大于0的数字！')
#         try:
#             r = float(input('您所要求的圆的半径是:'))
#         except:
#             print('输入错误，请输入数字！')
#     else:
#         p = math.pi
#         square = p*r**2
#         print('您所求的圆的面积为：%.4f'%square)
#
# cirarea()

# pi = math.pi
#
# def area_circle():
#     r = input('输入圆的半径：')
#
#     while r.isdigit() == False or float(r) <= 0:
#         print("请输入大于 0 的数字！")
#         r = input('请输入圆的半径:')
#     else:
#         r = float(r)
#         area = r*r*pi
#         print('圆的面积为 %d' % area)
#
# area_circle()


# 比较方便的不断计算圆的面积，也可以根据需求终止计算：
while True:
    print("请输入圆的半径r")
    try:
        r = float(input("请输入半径r:"))
    except ValueError:
        print("请重新输入正确的数字")
    else:
        if r >= 0:
            p = math.pi
            square = p *r**2
            print('您所求的圆的面积为：%.4f'%square)
        else:
            print()
        active = input('\n是否继续？(y/n): ')
        if active == 'n':
            break














