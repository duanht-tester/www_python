# -*- encoding: UTF-8 -*-
# __author__ = 'lenovo'


# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while
# 循环中终止，任何对应的循环 else 块将不执行。

# continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，
# 然后继续进行下一轮循环。

# n = 5
#
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#         # break
#
#     print(n)
# print("循环结束")

# for letter in 'Runoob':
#     if letter == 'b':
#         break
#     print("当前字母：%s" % letter)

# var = 10
#
# while var > 0:
#     # print("当前变量值为 %d" % var)
#
#     var -= 1
#     if var == 5:
#         # break
#         continue
#     print("当前变量值为 %d" % var)
#
#
# print("Good bye!")

# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为
#  false (以while循环)导致循环终止时被执行，但循环被 break 终止时不执行。

# 如下实例用于查询质数的循环例子:

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "等于", x, '*', n//x)
            break
    else:
        print(n, "是质数")