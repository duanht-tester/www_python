# -*- coding:utf-8 -*-

"""
# 保留字
import keyword as kw
blz = kw.kwlist
print(blz)
"""
"""
# 注释
# 第一个注释
print("Hello, Python!")  # 第二个注释
# 第一个注释
# 第二个注释

'''
第三注释
第四注释
'''
'''
第五注释
第六注释
'''
print("Hello, Python!")
"""
"""
# 行与缩进
if True:
    print('True')
else:
    print('False')

if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
print ("False")    # 缩进不一致，会导致运行错误
"""
"""
# 多行语句
total = "item_one + \
    item_two +\
    item_three"
print(total)
total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']
print(total)
"""

# 字符串
str= 'Runoob'
print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str[:3])
print(str * 2)
print(str + "你好！")
print('--------------------')
print("hello\nrunoob!")
print(r"hello\nrunoob")