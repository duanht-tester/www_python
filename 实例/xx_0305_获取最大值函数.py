# -*- coding: utf-8 -*-
# __author__ = 'lenovo'

# # 最简单的
# print(max(1, 2))
# print(max('a', 'b'))
#
# # 也可以对列表和元组使用
# print(max([1, 2]))
# print(max((1, 2)))

# 更多实例
# print("80, 100, 1000 最大值为: ", max(80, 100, 1000))
# print("-20, 100, 400最大值为: ", max(-20, 100, 400))
# print("-80, -20, -10最大值为: ", max(-80, -20, -10))
# print("0, 100, -400最大值为:", max(0, 100, -400))


"""
 max() 函数
 描述
max() 方法返回给定参数的最大值，参数可以为序列。

语法
以下是 max() 方法的语法:

max( x, y, z, .... )
参数
x -- 数值表达式。
y -- 数值表达式。
z -- 数值表达式。
返回值
返回给定参数的最大值。
实例
以下展示了使用 max() 方法的实例：
"""

# print("max(80, 100, 1000) : ", max(80, 100, 1000))
# print("max(-20, 100, 400) : ", max(-20, 100, 400))
# print("max(-80, -20, -10) : ", max(-80, -20, -10))
# print("max(0, 100, -400) : ", max(0, 100, -400))
"""
>>> a='1,2,3,4'
>>> type(a)             #类型为字符串
<type 'str'>
>>> max(a)              #max 返回了最大值
'4'
>>> a=[1,2,3,4]
>>> type(a)             #类型是列表
<type 'list'>
>>> max(a)              #max函数也返回了最大值
4
>>>
>>>
>>> a=[(1,2),(2,3),(3,4)]                #假设列表里面是元组构成元素呢
>>> max(a)                                     #按照元素里面元组的第一个元素的排列顺序，输出最大值（如果第一个元素相同，则比较第二个元素，输出最大值）据推理是按ascii码进行排序的
(3, 4)
>>> a=[('a',1),('A',1)]                     #实验推测是按ascii码进行排序，比较  a  和   A 的值，得出a > A   ,  因为ascii 码里面，按照排列顺序 小 a在 A的后面
>>> max(a)
('a', 1)
>>> a=[(1,2),(2,3),(3,1)]
>>> a=[(1,3),(2,2),(3,1)]                #列表里面的元素都由元组构成，元组都由数字组成，输出最大值
>>> max(a)
(3, 1)
>>> a=[(1,3),(2,2),(3,1),(3,1)]
>>> max(a)
(3, 1)
>>> a=[(1,3),(2,2),(3,1),(3,2)]
>>> max(a)
(3, 2)
>>>
>>> a=[(1,3),(2,2),(3,1),(3,'b'),('a',1)]
>>> max(a)
('a', 1)
>>> a=[(1,3),(2,2),(3,1),(3,'b'),('a',1),('f',3)]
>>> max(a)
('f', 3)
>>>
>>> a={1:2,2:2,3:1,4:'aa'}                  #比较字典里面的最大值，会输出最大的键值
>>> max(a)
4
"""

# max 里可以加入一个 key 的索引。
# import re
#
# reg = re.compile('a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*')
# # 返回一个字符串里按字母表排序的最长子字符串
# def longest(s):
#     print(reg.findall(s))
# # ['abcde', 'ap', 'bcdef', '']
#     return max(reg.findall(s), key=len)
# # 加或不加效果相同
# print(longest('abcdeapbcdef'))

# 对比任意多个数字的大小
n = int(input('输入需要对比大小数字的个数：'))
print("请输入需要对比的数字：")
num = []
for i in range(1, n+1):
    temp = int(input('输入第 %d 个数字' % i))
    num.append(temp)
print('您输入的数字为：',num)
print('最大值为：', max(num))

# 参考方法：
n = int(input('输入需要对比大小数字的个数：\n'))
num = [int(input('请输入第 %d 个对比数字 \n' % (i))) for i in range(1, n+1)]

print('您输入的数字为:', list(num))
print('最大值为: ', max(num))


# 相比以上不用输入对比大小数字的个数:
a = []
while True:
    """输入q来结束输入数字"""
    try:
        a.append(int(input("输入数字: ")))
        break
    except ValueError:
        print("输入的不是数字")
while a[-1] != 'q':
    c = input("输入数字: ")
    if c != 'q':
        try:
            a.append(int(c))
        except ValueError:
            print("输入的不是数字")
    else:
        a.append(c)
del a[-1]
print("最大数字是",max(a))















