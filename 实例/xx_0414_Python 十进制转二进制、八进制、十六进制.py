# -*- encoding: UTF-8 -*-
# __author__ = 'lenovo'

# 获取用户输入十进制数
# dec = int(input("输入数字："))
# print("十进制数为：", dec)
# print("转换为二进制为：", bin(dec))
# print("转换为八进制为：", oct(dec))
# print("转换为十六进制为：", hex(dec))

# 十进制到二进制：
# def dec2bin(num):
#     l = []
#     if num < 0:
#         return '-' + dec2bin(abs(num))
#     while True:
#         num, remainder = divmod(num, 2)
#         l.append(str(remainder))
#         if num == 0:
#             return ''.join(l[::-1])
#
# a = dec2bin(5)
# print(a)

# 十进制到八进制：
# def dec2oct(num):
#     l = []
#     if num < 0:
#         return '-' + dec2oct(abs(num))
#     while True:
#         num, remainder = divmod(num, 8)
#         l.append(str(remainder))
#         if num == 0:
#             return ''.join(l[::-1])
#
# a = dec2oct(100)
# print(a)

# 十进制到十六进制：
# base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A')+6)]
#
# def dec2hex(num):
#     l = []
#     if num < 0:
#         return '-' + dec2hex(abs(num))
#     while True:
#         num, rem = divmod(num, 16)
#         l.append(base[rem])
#         if num == 0:
#             return ''.join(l[::-1])
#
# a = dec2hex(0)
# print(a)

# 十进制数转化成二进制数（float）
# while True:
#     number = int(input("请输入一个正数:(输入q退出程序）"))
#     if number in ['q', 'Q']:
#         break
#     elif not float(number) > 0:
#         print("请输入一个正数（输入q退出程序）：")
#     else:
#         number = float(number)
#         array1 = []
#         array2 = []
#         integer = int(number)
#         float = number -integer
#         while integer != 0:
#             array1.append(integer%2)
#             integer = integer//2
#         else:
#             array1.append(0)
#         array1.reverse()
#         while float > 0.00001:
#             array2.append(int(2*float))
#             float = float*2 -int(float*2)
#         else:
#             array2.append(0)
#         array1.append('.')
#         array = array1 + array2
#         for x in array:
#             print(x, end='')
#         print("\n")




























