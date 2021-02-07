# -*- encoding: UTF-8 -*-
# __author__ = 'lenovo'

"""
输入和输出
在前面几个章节中，我们其实已经接触了 Python 的输入输出的功能。本章节我们将具
体介绍 Python 的输入输出。
输出格式美化
Python两种输出值的方式: 表达式语句和 print() 函数。
第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
"""
# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。
# s = "hello Runoob"
# print(str(s))
# print(repr(s))
# print(str(1/7))
# x = 10*3.25
# y = 200*200
# s = "x 的值为：" + repr(x) + ", y 的值为：" + repr(y)
# print(s)
# #  repr() 函数可以转义字符串中的特殊字符
# hello = "hello Runoob\n"
# hellos = repr(hello)
# print(hellos)
# # repr() 的参数可以是 Python 的任何对象
# print(repr((x, y, ('Google', 'Runoob'))))
# 这里有两种方式输出一个平方与立方的表:
# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
#     # 注意前一行 'end' 的使用
#     print(repr(x*x*x).rjust(4))
#
# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
"""
注意：在第一个例子中, 每列间的空格由 print() 添加。
这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西,
它们仅仅返回新的字符串。
"""
# 另一个方法 zfill(), 它会在数字的左边填充 0，如下所示：
# aaa = '12'.zfill(5)
# print(aaa)
# print('-3.14'.zfill(7))
# print('3.14159265359'.zfill(5))
# str.format() 的基本使用如下:
# print('{}网址： “{}!”'.format('菜鸟教程', 'www.runoob.com'))
# 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
# 在括号中的数字用于指向传入对象在 format() 中的位置，如下所示：
# print("{0} 和 {1}".format('Google', 'Runoob'))
# print("{1} 和 {0}".format('Google', 'Runoob'))
# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
# print("'{name}网址：{site}'".format(name='菜鸟教程', site='www.runoob.com'))
# # 位置及关键字参数可以任意的结合:
# print("站点列表{0}，{1}，和 {other}.".format('Google', 'Runoob', other='Taobao'))
# # !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
# import math
# print("常量PI 的值近似为：{}。".format(math.pi))
# print("常量PI 的值近似为：{!r}。".format(math.pi))
# 可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。
# 下面的例子将 Pi 保留到小数点后三位：
# import math
# print("常量 PI 的值为：{0:.3f}".format(math.pi))
# # 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
# table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# for name, number in table.items():
#     print("{0:10} ==> {1:10d}".format(name, number))
#
# print("Runoob:{0[Runoob]:d}; Google:{0[Google]:d};Taobao{0[Taobao]:d}".format(table))
#
# # 也可以通过在 table 变量前使用 ** 来实现相同的功能：
# print("Runoob:{Runoob:d};Google:{Google:d};Taonbao:{Taobao:d}".format(**table))
"""
旧式字符串格式化
% 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串,
而将右边的代入, 然后返回格式化后的字符串. 例如:
"""
# import math
# print("常量PI的值近似为：%5.3f." % math.pi)
# # 因为 str.format() 是比较新的函数， 大多数的 Python 代码仍然使用 % 操作符。但是
# # 因为这种旧式的格式化最终会从该语言中移除, 应该更多的使用 str.format().

"""
读取键盘输入
Python提供了 input() 内置函数从标准输入读入一行文本，默认的标准输入是键盘。
input 可以接收一个Python表达式作为输入，并将运算结果返回。
"""
# str = input("请输入：")
# print("你输入的内容是：", str)
"""
读和写文件
open() 将会返回一个 file 对象，基本语法格式如下:
open(filename, mode)
filename：包含了你要访问的文件名称的字符串值。
mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
不同模式打开文件的完全列表：


模式	描述
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
"""
# 以下实例将字符串写入到文件 foo.txt 中：
# 打开一个文件
f = open("./foo.txt", 'w')
f.write("Python 是一门非常好的语言。\n是的，的确非常好！！\n")

# 关闭打开文件
f.close()
# 第一个参数为要打开的文件名。
# 第二个参数描述文件如何使用的字符。 mode 可以是 'r' 如果文件只读, 'w' 只用于写
# (如果存在同名文件则将被删除), 和 'a' 用于追加文件内容; 所写的任何数据都会被自
# 动增加到末尾. 'r+' 同时用于读写。 mode 参数是可选的; 'r' 将是默认值。
# 此时打开文件 foo.txt,显示如下：
# $ cat /tmp/foo.txt
"""
f.tell()
f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
f.seek()
如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示
文件的结尾，例如：
seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
seek(x,1) ： 表示从当前位置往后移动x个字符
seek(-x,2)：表示从文件的结尾往前移动x个字符
"""
# from_what 值为默认为0，即文件开头。下面给出一个完整的例子：
# f = open("./foo.txt", 'rb+')
# print(f.write(b'0123456789abcdef'))
# print(f.seek(5))    # 移动到文件的第六个字节
# print(f.read(1))
# print(f.seek(-3, 2))   # 移动到文件的倒数第三字节
# print(f.read(1))
"""
f.close()
在文本文件中 (那些打开文件的模式下没有 b 的), 只会相对于文件起始位置进行定位。
当你处理完一个文件后, 调用 f.close() 来关闭文件并释放系统的资源，如果尝
试再调用该文件，则会抛出异常。
"""
# f = open("./foo.txt", 'rb+')
# f.close()
# f.read()
# 当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后,
# 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短:
with open("./foo.txt", 'r') as f:
    read_data = f.read()

f.close()
# 文件对象还有其他方法, 如 isatty() 和 trucate(), 但这些通常比较少用。
"""
pickle 模块
python的pickle模块实现了基本的数据序列和反序列化。
通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
基本接口：
pickle.dump(obj, file, [,protocol])
有了 pickle 这个对象, 就能对 file 以读取的形式打开:
x = pickle.load(file)
注解：从 file 中读取一个字符串，并将它重构为原来的python对象。
file: 类文件对象，有read()和readline()接口。

"""
# import pickle
#
# # 使用pickle模块将数据对象保存到文件
# data01 = {'a': [1, 2.0, 3, 4+6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}
#
# selfref_list = [1, 2, 3]
# selfref_list.append(selfref_list)
#
# output = open("data.pkl", 'wb')
#
# # Pickle字典使用协议0。
# pickle.dump(data01, output)
#
# # Pickle使用可用的最高协议列表。
# pickle.dump(selfref_list, output, -1)
#
# output.close()

# import pprint, pickle
#
# pkl_file = open("data.pkl", 'rb')
#
# data02 = pickle.load(pkl_file)
# pprint.pprint(data02)
#
# data03 = pickle.load(pkl_file)
# pprint.pprint(data03)
#
# pkl_file.close()
# python文件写入也可以进行网站爬虫,我的python版本是3.6，以下代码是打开
# project.txt文件，并向里面写入http://www.baidu.com网站代码。
# from urllib import request
#
# # 打开网站
# response = request.urlopen('https://www.baidu.com/?tn=40020637_4_oem_dg')
# # open一个txt文件
# fi = open("project.txt", 'w')
# # 网站代码写入
# page = fi.write(str(response.read()))
# # 关闭txt文件
# fi.close()

# # input() 默认输入的为 str 格式，若用数学计算，则需要转换格式，例：
# a = input("请输入数字：")
# print(a*2)
# 假设输入数值为3，则上例中得出结果为：
# a = int(input("请输入数字："))
# print(a*2)

# 通过 pickle 序列化实现一个简单联系人信息管理：
import pickle
import os
datafile = "person.data"
line = "====================="
message = '''
==============================
Welcome bookmark:
    press 1 to show list
    press 2 to add pepole
    press 3 to edit pepole
    press 4 to delete pepole
    press 5 to search pepole
    press 6 to show menu
    press 0 to quit
=======================================
'''
print(message)

class Person(object):
    """通讯录联系人"""
    def __init__(self, name, number):
        self.name = name
        self.number = number

# 获取数据
def get_data(filename=datafile):
    if os.path.exists(filename) and os.path.getsize(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    return None

# 写入数据
def set_data(name, number, filename=datafile):
    personList = {} if get_data() == None else get_data()
    with open(filename, 'wb') as f:
        personList[name] = Person(name, number)
        pickle.dump(personList, f)

# 保存字典格式的数据到文件
def save_data(dicPerson, filename=datafile):
    with open(filename, 'wb') as f:
        pickle.dump(dicPerson, f)

# 显示所有联系人
def show_all():
    personList = get_data()
    if personList:
        for v in personList.values():
            print(v.name, v.number)
        print(line)
    else:
        print("not yet person,please add person")
        print(line)

# 添加联系人
def add_person(name, number):
    set_data(name, number)
    print('success add person')
    print(line)

# 编辑联系人
def edit_person(name, number):
    personList = get_data()
    if personList:
        personList[name] = Person(name, number)
        save_data(personList)
        print('success edit person')
        print(line)

# 删除联系人
def delete_person(name):
    personList = get_data()
    if personList:
        if name in personList:
            del personList[name]
            save_data(personList)
            print("success delete person")
        else:
            print(name, "is not exists in dict")
        print(line)

# 搜索联系人
def search_person(name):
    personList = get_data()
    if personList:
        if name in personList.keys():
            print(personList.get(name).name, personList.get(name).number)
        else:
            print('No this person of ', name)
        print(line)


while True:
    num = input('>>')

    if num == '1':
        print('show all personList:')
        show_all()
    elif num == '2':
        print('add person:')
        name = input('add person:')
        number = input('input number>>')
        add_person(name, number)
    elif num == '3':
        print('edit person:')
        name = input('input name>>')
        number = input('input number>>')
        edit_person(name, number)
    elif num == '4':
        print('delete person:')
        name = input('input name>>')
        delete_person(name)
    elif num == '5':
        print('search :')
        name = input('input name>>')
        search_person(name)
    elif num == '6':
        print(message)
    elif num == '0':
        break
    else:
        print('input error, please retry')





























