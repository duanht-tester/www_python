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
"""
"""
# 等待用户输入
input("\n\n按下enter键退出。")
"""
"""
# 同一行显示多条语句
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
"""
"""
# Print 输出
x = 'a'
y = 'b'
print(x)
print(y)
print('---------')
print(x, end='')
print(y, end='')
"""
"""
# 导入 sys 模块
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print(i)
print ('\n python 路径为', sys.path)
from sys import argv,path
print('================python from import===================================')
print('path', path)
"""




