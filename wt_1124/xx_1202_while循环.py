# -*- encoding: UTF-8 -*-
# __author__ = 'lenovo'


# n = 5
# sum = 0
# counter = 1
#
# while counter <= n:
#     sum = sum + counter
#     counter += 1
#
# print("1 到 %d 之和为： %d" % (n, sum))


# 无限循环
# 我们可以通过设置条件表达式永远不为 false 来实现无限循环

# var = 1
#
# while var == 1:  # 表达式永远为 true
#     num = int(input("输入一个数字："))
#     print("你输入的数字是:")
#
# print("Good bye!")


# while 循环使用 else 语句
# 在 while … else 在条件语句为 false 时执行 else 的语句块。
#
# 语法格式如下：
#
# while <expr>:
#     <statement(s)>
# else:
#     <additional_statement(s)>

# count = 0
# while count < 5:
#     print(count, "小于5")
#     count += 1
# else:
#     print(count, "大于或等于5.")

# 简单语句组
# 类似if语句的语法，如果你的while循环体中只有一条语句，
# 你可以将该语句与while写在同一行中， 如下所示：

flag = 1

while (flag):
    print("'欢迎访问菜鸟教程!'")

print(" Good bye!")
