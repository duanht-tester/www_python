# -*- encoding: UTF-8 -*-
# __author__ = 'lenovo'


# range()函数
# 如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，例如:
#
# 实例
# >>>for i in range(5):
# ...     print(i)
# ...
# 0
# 1
# 2
# 3
# 4
#
# for i in range(5, 9):
#     print(i)

# for i in range(0, 10, 3):
#     print(i)

# for i in range(-10, -100, -30):
#     print(i)

a = ['Google', 'baidu', 'runoob', 'qq']
for i in range(len(a)):
    print(i, a[i])