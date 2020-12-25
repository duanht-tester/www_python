# -*- encoding: UTF-8 -*-
# __author__ = 'lenovo'
"""
Python3 函数
函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了
许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。
定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：

函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号 : 起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方，
不带表达式的 return 相当于返回 None。
语法
Python 定义函数使用 def 关键字，一般格式如下：

def 函数名（参数列表）:
    函数体
    默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的。
"""

# def hello():
#     print("hello world!")
#
# hello()

# 函数中带上参数变量:
# def max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
# a = 4
# b = 5
# print(max(a, b))

# def area(width, height):
#     return width * height
#
# def print_welcome(name):
#     print("Welcome", name)
#     return
#
# print_welcome("runoob")
# w = 4
# h = 5
# print("width =", w, "height =", h, "area =", area(4, 5))

"""
函数调用
定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构。
这个函数的基本结构完成以后，你可以通过另一个函数调用执行，
也可以直接从 Python 命令提示符执行。

如下实例调用了 printme() 函数：
"""
# 定义函数
# def printme(str):
#     # 打印任何传入的字符串
#     print(str)
#     return
#
# # 调用函数
# printme("我要调用用户自定义函数!")
# printme("再次调用同一函数")

"""参数传递
在 python 中，类型属于对象，变量是没有类型的：
a=[1,2,3]
a="Runoob"
以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a
是没有类型，她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，
也可以是指向 String 类型对象。
"""
"""可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，
而 list,dict 等则是可以修改的对象。

不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，
再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。

可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个
元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

不可变类型：类似 C++ 的值传递，如 整数、字符串、元组。如 fun(a)，
传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a)）内部修改 a 的值，
则是新生成来一个 a。

可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la
真正的传过去，修改后 fun 外部的 la 也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不
可变对象和传可变对象。
"""

# python 传不可变对象实例
# 通过 id() 函数来查看内存地址变化：
# def change(a):
#     print(id(a))
#     a = 10
#     print(id(a))
#
# a = 1
# print(id(a))
# change(a)

# 传可变对象实例
# 可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：
# 可写函数说明
# def changeme(mylist):
#
#    # 修改传入的列表"
#     mylist.append([1, 2, 3, 4])
#     print("函数内取值：", mylist)
#     return
#
# # 调用changeme函数
# mylist = [10, 20, 30]
# changeme(mylist)
# print("函数外取值：", mylist)
"""
参数
以下是调用函数时可使用的正式参数类型：

必需参数
关键字参数
默认参数
不定长参数
"""
# 必需参数
# 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
#
# 调用 printme() 函数，你必须传入一个参数，不然会出现语法错误：
# 可写函数说明
# def printme(str):
#     '''打印任何传入的字符串'''
#     print(str)
#     return
#
# # 调用 printme 函数，不加参数会报错
# printme("Hello Python!")
# 关键字参数
# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python
# 解释器能够用参数名匹配参数值。
# 以下实例在函数 printme() 调用时使用参数名：
# 可写函数说明
# def printme(str):
#     """
#     :param str: 打印任何传入的字符串
#     :return:
#     """
#     print(str)
#     return
# # 调用printme函数
# printme(str="hello python!")

# 以下实例中演示了函数参数的使用不需要使用指定顺序：
# def printinfo(name, age):
#     """
#        "打印任何传入的字符串"
#     :param name: 名字
#     :param age: 年龄
#     :return:
#     """
#     print("名字:", name, end="\t\t")
#     print("年龄:", age)
#     return
#
# # 调用printinfo函数
# printinfo(age=50, name="小名")

# 默认参数
# 调用函数时，如果没有传递参数，则会使用默认参数。
# 以下实例中如果没有传入 age 参数，则使用默认值：

#可写函数说明
# def printinfo(name, age=35):
#     """
#    "打印任何传入的字符串"
#     :param name: 名字
#     :param age:  默认年龄35
#     :return:
#     """
#     print("名字：", name)
#     print("年龄：", age)
#     return
#
# # 调用printinfo函数
# printinfo(age=50, name="小名")
# print("-" * 50)
# # age 使用默认参数35
# printinfo(name="小王")

# 不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，
# 和上述 2 种参数不同，声明时不会命名。基本语法如下：

# def functionname([formal_args,] *var_args_tuple):
#    "函数_文档字符串"
#     funtion_suite
#     return [expression]
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 可写函数说明
# def printinfo(arg1, *vartuple):
#     """
#        "打印任何传入的参数"
#     :param arg1:       普通参数
#     :param *vartuple:    元组参数
#     :return:
#     """
#     print("输出：")
#     print(arg1)
#     print(vartuple)
#     return
#
# printinfo(70, 60, 50)
# 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向
# 函数传递未命名的变量。如下实例：
# 可写函数说明
# def printinfo(arg1, *vartuple):
#     """
#        "打印任何传入的参数"
#     :param arg1:
#     :param vartuple:
#     :return:
#     """
#     print("输出")
#     print(arg1)
#     # 遍历元组里的数据
#     for var in vartuple:
#         print(var)
#     return
#
# printinfo(10)
# printinfo(70, 60, 50)
# 还有一种就是参数带两个星号 **基本语法如下：
# def functionname([formal_args,] **var_args_dict ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]

# def printinfo(arg1, **vardic):
#     """
#        "打印任何传入的参数"
#     :param arg1:   普通参数
#     :param vardic: 字典参数
#     :return:
#     """
#     print("输出")
#     print(arg1)
#     print(vardic)
#     return
#
# # 调用printinfo 函数
# printinfo(1, a=2, b=3)
# 声明函数时，参数中星号 * 可以单独出现，例如:
# def f(a, b, *, c):
#     """
#     :param a: 普通参数
#     :param b: 普通参数
#     :param c: 关键字参数
#     :return:
#     """
#     print(a+b+c)
#     return a+b+c
#
# f(1, 2, c=3)
"""
匿名函数
python 使用 lambda 来创建匿名函数。
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装
有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是
调用小函数时不占用栈内存从而增加运行效率。
"""
# 语法
# lambda 函数的语法只包含一个语句，如下：
# lambda [arg1 [,arg2,.....argn]]:expression
# #匿名函数只有一句好
# sum = lambda arg1, arg2: arg1+arg2:
#
# # 调用sum函数
# print("相加后的和为：", sum(10, 20))
# print("相加后的和为：", sum(20, 30))
#
"""
return语句
return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。
不带参数值的return语句返回None。之前的例子都没有示范如何返回数值，
以下实例演示了 return 语句的用法：
"""
# def sum(agr1, arg2):
#     total = arg2+agr1
#     print("函数内：", total)
#     return total
#
# total = sum(10, 20)
# print("函数外：", total)
"""
强制位置参数
Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，
不能使用关键字参数的形式。

在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或
关键字形参，而 e 或 f 要求为关键字形参:
"""
# def f(a, b, /, c, d, *, e, f):
#     print(a, b, c, d, e, f)
#     return
#
# f(10, 20, 30, d=40, e=50, f=60)
# 以下使用方法会发生错误:
# f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
# f(10, 20, 30, 40, 50, f=60)           # e 必须使用关键字参数的形式

# def foo(x):
#     """
#     递归函数调用
#     :param x:
#     :return:
#     """
#     if x == 1:
#         return 1
#     else:
#         return x+foo(x-1)
#
# print(foo(4))
# 默认参数必须放在最后面，否则会报：
# # 可写函数说明
# def printinfo( age=35,name):   # 默认参数不在最后，会报错
#     "打印任何传入的字符串"
#     print("名字: ", name)
#     print("年龄: ", age)
#     return
# def(**kwargs) 把N个关键字参数转化为字典:
# def func(county, province, **kwargs):
#     print(county, province, kwargs)
#     return
#
# func("China", "Sichuan", city="Chengdu", section="jingjiang")
# lambda 匿名函数也是可以使用"关键字参数"进行参数传递
# g = lambda x, y: x**2 + y**2
# print(g(2, 3))
# print(g(y=3, x=2))
# # 同样地，lambda 匿名函数也可以设定默认值
# g = lambda x=0, y=0: x**2 + y**2
# print(g(2, 3))
# print(g(2))
# print(g(y=3))
# # 注意：如果只打算给其中一部分参数设定默认值，那么应当将其放在靠后的位置
# # （和定义函数时一样，避免歧义），否则会报错。
"""
关于可更改与不可更改类型， 以及其它语言的值类型与引用类型的介绍，一直一来感觉都不太严谨， 说法是否正确有待验证。

简单的说就是，不可更改类型传到函数里重新赋值后，两次输出值不一样，而可更改类型传到函数里对对象的"属性" 重新赋值后输出值一样。

这里照搬一下例子：
"""
# def changeme(mylist):
#     # "修改传入的列表"
#     # mylist.append([1, 2, 3, 4])
#     mylist = [1, 2, 3, 4]
#     print("函数内取值：", mylist)
#     return
#
# # 调用changeme函数
# mylist = [10, 20, 30]
# changeme(mylist)
# print("函数外取值：", mylist)
"""
请注意：上面特意用了引号标准的部分，对可变类型或者引用的操作修改的是传过来的对象
的属性。
可以这么理解(例子有点随意)：我在画画，小明来了说他也要画，我让他和我一起画，
他如果和我在同一个画板上画，那么我们两的画就会同时改变。 而如果他说不，我要另
外用一块画板，然后重新拿了块画板画起来了，那么我们两的画自然就不一样了。
同理可更改类型 的属性进行操作，这只是对引用的内存块里面的值进行操作，引用并没
变，自然所有引用它的对象的值都变了。而对不可更改的对象进行操作，因为它引用的
内存块只是对应一个固定的值，不能进行修改，要重新复制实际上就是更新引用。
如果我们运行下面的例子，对可更改类型的引用进行修改，结果就不一样了。
"""
"""
对于变量作用域，变量的访问以 L（Local） –> E（Enclosing） –> G（Global）
 –>B（Built-in） 的规则查找，即：在局部找不到，便会去局部外的局部找
 （例如闭包），再找不到就会去全局找，再者去内建中找。
观察以下几个例子，均从内部函数输出变量 x：
"""
# # 1. 局部作用域
# x = int(3.3)
# x = 0
# def outer():
#     x = 1
#
#     def inner():
#         x = 2
#         # # 执行结果为 2，因为此时直接在函数 inner 内部找到了变量 x。
#         print(x)
#
#     inner()
#
# outer()
# # 2.闭包函数外的函数中
#
# x = int(3.3)
#
# x = 0
# def outer():
#     x = 1
#
#     def inner():
#         i = 2
#         # # 执行结果为 1，因为在内部函数 inner 中找不到变量 x，继续去局
#         # 部外的局部——函数 outer 中找，这时找到了，输出 1。
#         print(x)
#     inner()
#
# outer()
# # 3.全局作用域
# x = int(3.3)
# x = 0
# def outer():
#     o = 1
#
#     def inner():
#         i = 2
#         # # 执行结果为 0，在局部（inner函数）、局部的局部（outer函数）
#         # 都没找到变量 x，于是访问全局变量，此时找到了并输出。
#         print(x)
#     inner()
#
# outer()
# # 4. 内建作用域
# x = int(3.3)
# g = 0
# def outer():
#     o = 1
#
#     def inner():
#         i = 2
#         # 执行结果为 3，在局部（inner函数）、局部的局部（outer函数）
#         # 以及全局变量中都没有找到变量x，于是访问内建变量，此时找到了并输出。
#         print(x)
#     inner()
#
# outer()
# 函数内可以访问全局变量，但不能更新(修改)其值！
# a = 10
# def sum(n):
#     global a
#     n += a
#     a = 11
#     print('a=', a, end=" ,")
#     print("n=", n)
#
# sum(3)
# print('外 a = ', a)
# 函数也可以以一个函数为其参数:
# def hello():
#     print("Hello world")
#     return
#
# def excute(f):
#
#     f()
#
# excute(hello)
# 可以通过 函数名.__doc__ 的方式来显示函数的说明文档，感觉这个如果在阅读
# 比较大的程序时应该会有用，同时也在提示自己在写函数时注意添加文档说明。
# def add(a, b):
#     "这是add 函数文档。"
#     return a+b
#
# print(add.__doc__)
# 函数返回值的注意事项: 不同于 C 语言，Python 函数可以返回多个值，
# 多个值以元组的方式返回:
# def fun(a, b):
#     "返回多个值，结果为元组。"
#     return a, b, a+b
#
# print(fun(1, 2))
# 函数的装饰器
# 在不改变当前函数的情况下, 给其增加新的功能:
# def log(pr):  # 将被装饰函数传入
#     def wrapper():
#         print("*" * 50)
#         return pr  # 执行被装饰的函数
#     return wrapper()  # 将装饰完之后的函数返回（返回的是函数名）
#
# @log
# def kr():
#     print("我是小小羊。")
#
# kr()
# 回调函数和返回函数的实例就是装饰器。
# 1.内部函数，不修改全局变量可以访问全局变量
# a = 10
# def test():
#     b = a + 2  # 仅仅访问全局变量 a
#     print(b)
#
# test()
# 2.内部函数，修改同名全局变量，则python会认为它是一个局部变量
# （同教程最后一个例子）
# a = 10
# def test():
#     global a
#     a = a+1  # 修改同名的全局变量，则认为是一个局部变量
#     print(a)
#
# test()
# 3.在内部函数修改同名全局变量之前调用变量名称（如print sum），
# 则引发Unbound-LocalError
# 在这里补充一点关于 global 和 nonlocal 的知识：
# nonlocal 只能修改外层函数的变量而不能修改外层函数所引用的全局变量，
# 给一个例子如下：
# x = 0
# def outer():
#     global x
#     x = 1
#
#     def inner():
#         nonlocal x
#         x = 2
#         print(x)
#
#     inner()
#
# outer()
# print(x)
# global 关键字会跳过中间层直接将嵌套作用域内的局部变量变为全局变量:
# 测试代码如下:
# num = 20
# def outer():
#     num = 10
#
#     def inner():
#         global num
#         print(num)
#         num = 100
#         print(num)
#
#     inner()
#     print(num)
#
#
# outer()
# print(num)
# Python 定义一个 class 可以编写一个它的构造函数 _init_() 其中形参
# self 在实例化时相当于 myname：
# class demo:
#
#     name = ""
#
#     def __init__(self):
#         pass
#         # self.ex()
#         # self.start()
#
#     def inputName(self):
#         global name
#         name = input("输入你的姓名：")
#
#     def getFirstName(self):
#         if len(name) <= 0:
#             x = "请输入姓名："
#             return x
#         else:
#             x = name[0]
#             return x
#
#     def getLastName(self):
#         if len(name) <= 1:
#             y = "名字长度不够："
#             return y
#         else:
#             y = name[1:]
#             return y
#
#
# myname = demo()
# myname.inputName()
# print(myname.getFirstName())
# print(myname.getLastName())
"""
函数的参数分为形参和实参。
1. 什么是形参
对于函数来说，形式参数简称形参，是指在定义函数时，定义的一个变量名。
下面的代码中，x、y、z 就是形参。
"""
# def foo(x, y, z):
#       print("x=", x)
#       print("y=", y)
#       print("z=", z)
#
# # 调用函数
# foo(1, 3, 5)  # 此处的1,3,5是实参
# # 形参的作用：是用来接收调用函数时输入的值。
# 2. 什么是实参
# 对于函数来说，实际参数简称实参。
# 是指在调用函数时传入的实际的数据，这会被绑定到函数的形参上。
# 函数调用时，将值绑定到变量名上，函数调用结束，解除绑定，
# 并且实参将不再存在于程序中。
# 在编写函数的过程中，可以显式指定函数的参数类型及返回值类型：
#
# import sys
# sys.setrecursionlimit(1000000)  # 例如这里设置为一百万
#
# def function_demo(param_A: int, param_B: float, param_C: list,
#                   param_D: tuple):
#     pass

# 这种 “将数据类型写死在代码中” 的行为在集成开发环境/代码编辑器时尤为方便，
# 通过显式地指定函数的参数类型和返回值，能够让智能补全组件提前获知标识符的
# 数据类型，提供有利的辅助开发功能。
# 对于上面提到的向函数中传递函数对象的用法，我这里进一步补充。
# 1.向函数传递的函数本身可以是有参数的:
def demo(*p):
    i = 0
    for var in p:
        var(i)
        i += 1

def d1(i):
    print("这里是第一个子函数,输入的数是", i)

def d2(i):
    print("这里是第二个子函数,输入的数是", i)

def d3(i):
    print("这里是第三个子函数,输入的数是", i)

def d4(i):
    print("这里是第四个子函数,输入的数是", i)

demo(d1, d2, d3, d4)
# 上面的代码执行起来没问题。
# .就算你的函数是有参数的，将这个函数传递给另一个函数的时候也不能加参数
# ，还是上面的例子:
# demo(d1(7), d2, d3, d4)
# 这样就会报错，因为此时 d1(7) 就是 d1() 的返回值，是不可以在方法内部传
# 递参数并且调用。



