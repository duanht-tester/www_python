# -*- encoding: UTF-8 -*-
# __author__ = 'lenovo'

# pass 语句
# Python pass是空语句，是为了保持程序结构的完整性。
#
# pass 不做任何事情，一般用做占位语句，如下实例
#
# 实例
# >>>while True:
# ...     pass  # 等待键盘中断 (Ctrl+C)
# 最小的类:
#
# 实例
# >>>class MyEmptyClass:
# ...     pass
# 以下实例在字母为 o 时 执行 pass 语句块:


# for letter in 'Runoob':
#     if letter == 'o':
#         pass
#         print("执行pass语句。")
#     print("当前字母：", letter)
#
# print("good bye!")

# if True:
#     print('hello')

# i = sum = 0
#
# while i <= 4:
#     sum += i
#     i += 1
#
# print(sum)

for char in "Python String":
    if char == ' ':
        break
    print(char, end='')

    if char == 'o':
        continue
