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
"""
print('Ru\noob')
print(r'Ru\noob')
word = 'Python'
print(word[0], word[5])
print(word[-1], word[-6])
"""
"""
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)

a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
print(a)
a[2:5] = []
print(a)
"""
"""
def reverseWords(input):

    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords=inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output

if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)
"""
"""
letters = ['c', 'h', 'e', 'c', 'k', 'i', 'o']
print(letters[1:4:2])
"""

