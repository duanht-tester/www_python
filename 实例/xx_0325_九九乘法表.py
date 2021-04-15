# -*- encoding: UTF-8 -*-
# __author__ = 'lenovo'

# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("{0}*{1}={2}\t".format(j, i, i * j), end='')
#     print()

# 通过指定end参数的值，可以取消在末尾输出回车符，实现不换行。

# # 乘法表左边的数要比右边的小，如下实例:
# class MultiplicationTable():
#     def paint(self, n=9):
#         for row in range(1, n+1):
#             for col in range(1, row + 1):
#                 print("{1}*{0}={2}\t".format(row, col, row * col), end='')
#             print()
#
#
# table = MultiplicationTable()
# table.paint(9)
# table.paint(10)  # 打印 "10x10" 的乘法表

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         if i == j:
#             print("{0}*{1}={2}\t".format(i, j, i * j))
#         else:
#             print('{1}×{0}={2}'.format(i, j, i * j), end='\t')
# 这样写可以有效去除每一行的最后一个空格,输出如下：
# 一句话输出99乘法表，可以参考一下：
# 用列表生成器打印九九乘法表:
# print("\n".join(' '.join("%d*%d=%-2d" % (x, y, x*y) for x in range(1, y + 1)) for y in range(1, 10)))

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%dx%d=%d\t" % (j, i, j*i), end='')
#     print()

# print('\n'.join(['\t'.join(['%d * %d = %d' % (y, x, x*y) for y in range(1, x+1)])for x in range(1, 10)]))

# 分享给像我这种门外汉，稍微好理解一些，Python3 支持中文变量真好。
# for 行 in range(1, 10):
#     for 列 in range(1, 行+1):  # 内循环中，确保列 <= 行。
#         print("{}*{}={}\t".format(列, 行, 列*行), end="")   # 确保同一行内容连续
#     print()     # 另起一行！！！
#
# input()  # 防止程序一闪而过，不在编译器中也能使用




























