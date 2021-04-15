# -*- encoding: UTF-8 -*-
# __author__ = 'lenovo'


# 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。
# 例如1^3 + 5^3 + 3^3 = 153。
# 1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
# 以下代码用于检测用户输入的数字是否为阿姆斯特朗数：

# Python 检测用户输入的数字是否为阿姆斯特朗数

# 获取用户输入的数字
# num = int(input("请输入一个数字: "))
#
# # 初始化变量 sum
# sum = 0
# # 指数
# n = len(str(num))
#
# # 检测
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** n
#     temp //= 10
# # 输出结果
# if num == sum:
#     print(num, "是阿姆斯特朗数")
# else:
#     print(num, "不是阿姆斯特朗数")


# 获取指定期间内的阿姆斯特朗数
# lower = int(input("最小值: "))
# upper = int(input("最大值: "))
#
# for num in range(lower, upper + 1):
#     # 初始化 sum
#     sum = 0
#     # 指数
#     n = len(str(num))
#     # 检测
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** n
#         temp //= 10
#
#     if num == sum:
#         print(num)

# 获取小于指定数字的阿姆斯特朗数
# num = int(input("pleace input a number: "))
# arr = [0,0,0,0,0]
# print(num)
# for k in range(1, num):
#     n = len(str(k))
#     m = n
#     i = 0
#     sum = 0
#     while m > 0:
#         m -= 1
#         arr[i] = int(k / 10 ** m) % 10
#         sum += arr[i] ** n
#         i += 1
#     if k == sum:
#         print(k, end=',')

# 以下代码用于检测用户输入的数字是否为阿姆斯特朗数
# import math
#
# x = int(input('请输入一个正整数:'))
# x1 = x
# n = len(str(x))
# p = 0
# for i in range(1, n+1):
#     y = math.floor(x//pow(10, n-i))
#     print(y, end=',')
#     m = pow(y, n)  # 也可以表达为:   m=y**n
#     p = (m+p)
#     x = (x % pow(10, n-i))
# print(p)
# if p == x1:
#     print('输入的数字 %d 是一个阿姆斯特朗数'%x1)
# elif p != x1:
#     print('输入的数字 %d 不是一个阿姆斯特朗数'%x1)

# 获取指定期间内的阿姆斯特朗数
# lower = int(input("Please input a number: "))
# upper = int(input("Please input a number: "))
# sum = 0
# for num in range(lower, upper):
#     l = len(str(num))
#     for n in str(num):
#         sum = (sum+int(n)**l)
#     if num == sum:
#         print(num)
#     sum = 0

# 计算阿姆斯特朗数
# count = 0
# num = int(input('请输入一个正整数:'))  # 输入值并强制类型转换
# len = len(str(num))  # 获取输入数字位数
# list_num = list(str(num))  # 将数字转化为列表
# for i in list_num:   # 将列表中的每一个元素以该元素的lenth次幂累加至count
#     i = int(i)
#     i **= len
#     count += i
#
# if count == num:   # 判断count与输入的数字是否相等，若相等则为阿姆斯特朗数
#     print('是阿姆斯特朗数')
# else:
#     print('不是阿姆斯特朗数')

# 使用 lambda 表达式：
# def is_armstrong(n):
#     s = sum(map(lambda x: eval(x)**len(str(n)), str(n)))
#     return s == n
#
# b = []
# for i in range(1000):
#     if is_armstrong(i):
#         b.append(i)
#
# print(b)

# 使用 list 的映射解析来进一步简化代码：

# def is_armstrong(n):
#     return n == sum([eval(i)**len(str(n)) for i in str(n)])
#
# b = [i for i in range(1000) if is_armstrong(i)]
# print(b)


# 检查输入是否合法:
# while True:
#
#     try:
#         lower = int(input("最小值: "))
#         upper = int(input("最大值: "))
#     except ValueError:
#         print("非法输入")
#         continue
#     if lower > upper:
#         print("请检查输入大小")
#         continue
#     for num in range(lower, upper):
#         sum = 0
#         n = len(str(num))
#         temp = num
#         while temp > 0:
#             digit = temp %10
#             sum += digit ** n
#             temp //= 10
#         if num == sum:
#             print(num, end=' ')
#     break

# 输出指定区间内的所有阿姆斯特朗数
# try:
#     lower = int(input("最小值："))
#     upper = int(input("最大值："))
# except ValueError:
#     print("所输入内容非整数!")
#     exit(1)
#
# for num in range(lower, upper+1):
#     sum = 0
#     n = len(str(num))
#     for i in str(num):
#         sum += int(i) ** n
#     if sum == num:
#         print(num, end=' ')

# 一个推导式搞定一个3位数的算法
# y = [(x//100)**3+((x//10) % 10)**3+(x % 10)**3 for x in range(100, 1000)
#      if (x//100)**3+((x//10) % 10)**3+(x % 10)**3 == x]
#
# print(y)




print((123//100))

















