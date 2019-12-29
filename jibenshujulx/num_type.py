# -*- coding:UTF-8 -*-
# __author__ = 'lenovo'

"""
counter = 100          # 整型变量
miles = 1000.0       # 浮点型变量
name = "runoob"     # 字符串

print(counter)
print(miles)
print(name)
"""
"""
# 多个变量赋值
a = b = c = 1
print(a)
print(b)
print(c)
a, b, c = 1, 2, 'runoob'
print(a)
print(b)
print(c)
"""
"""
# 数字
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
# 用 isinstance 来判断
a = 1111
b = isinstance(a, int)
print(b)

"""
"""
str = 'Runoob'

print(str)          # 输出字符串
print(str[0:-1])    # 输出第一个到倒数第二个的所有字符
print(str[0])       # 输出字符串第一个字符
print(str[2:5])     # 输出从第三个开始到第五个的字符
print(str[2:])      # 输出从第三个开始的后的所有字符
print(str * 2)      # 输出字符串两次
print(str + "TEST") # 连接字符串
print(str[-5])
print(str[1])
print(str[-1])
print(str[-6])
print(str[5])
"""

print('Ru\noob')
print(r'Ru\noob')
word = 'Python'
print(word[0], word[5])
print(word[-1], word[-6])