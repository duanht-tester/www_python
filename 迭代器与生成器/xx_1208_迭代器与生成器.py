# -*- encoding: UTF-8 -*-
# __author__ = 'lenovo'

#
# 迭代器
# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。
# 字符串，列表或元组对象都可用于创建迭代器：

# list = [1, 2, 3, 4]
# it = iter(list)  # 创建迭代器对象
#
# print(next(it))  # 输出迭代器的下1个元素
# print(next(it))  # 输出迭代器的下2个元素
# print(next(it))  # 输出迭代器的下3个元素
# print(next(it))  # 输出迭代器的下4个元素

# 迭代器对象可以使用常规for语句进行遍历：

# list = [1, 2, 3, 4]
# it = iter(list)  # 创建迭代器对象
#
# for x in it:
#     print(x, end=' ')

# 也可以使用 next() 函数：

# import sys  # 引入 sys 模块
#
# list = [1, 2, 3, 4]
# it = iter(list)  # 创建迭代器对象
#
# while True:
#     try:
#         print(next(it))
#
#     except StopIteration:
#         sys.exit()

# 创建一个迭代器
# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
# 如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python 的构造函数为 __init__(), 它会在对象初始化的时候执行。
# 更多内容查阅：Python3 面向对象
# __iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
# __next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。
# 创建一个返回数字的迭代器，初始值为 1，逐步递增 1：
#
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# StopIteration
# StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__()
#  方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
#
# 在 20 次迭代后停止执行：

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# for x in myiter:
#     print(x)


# 生成器
# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
# 调用一个生成器函数，返回的是一个迭代器对象。
# 以下实例使用 yield 实现斐波那契数列：

# import sys
#
# def fibonacci(n):
#     a, b, count = 0, 1, 0
#     while True:
#         if count > n:
#             return
#         yield a
#         a, b = b, a+b
#         count += 1
#
# f = fibonacci(5)
#
# while True:
#     try:
#         print(next(f), end=' ')
#
#     except StopIteration:
#         sys.exit()


# TODO: 来看一下有yield和没有yield的情况会对生成器了解多点：
# 第一种：使用 yield  第二种：注释yield,不使用 yield


# import sys
#
# def fibonacci(n, w=0):  # 生成器函数 - 斐波那契
#     a, b, count = 0, 1, 0
#     while True:
#         if count > n:
#             return
#         # yield a
#         a, b = b, a + b
#         print(" %d %d" % (a, b))
#         count += 1
#
# f = fibonacci(5, 0)   # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print(next(f), end=' ')
#     except StopIteration:
#         sys.exit()

# l = [i for i in range(0, 15)]
# print(l)
# m = (i for i in range(0, 15))
# print(m)
# for g in m:
#     print(g, end=',')

#
# 一个函数 f，f 返回一个 list，这个 list 是动态计算出来的（不管是数学上的计算还是逻辑上的读取格式化），
# 并且这个 list 会很大（无论是固定很大还是随着输入参数的增大而增大），这个时候，我们希望每次调用这个函数
# 并使用迭代器进行循环的时候一个一个的得到每个 list 元素而不是直接得到一个完整的 list 来节省内存，这个时候 yield 就很有用。
# 具体怎么使用 yield 参考：Python yield 使用浅析
# 以斐波那契函数为例，我们一般希望从 n 返回一个 n 个数的 list：

# import sys
# def fab(max):
#     n, a, b = 0, 0, 1
#     L = []
#     while n < max:
#         L.append(b)
#         a, b = b, a+b
#         n += 1
#     return L
#
# # 上面那个 fab 函数从参数 max 返回一个有 max 个元素的 list，当这个 max 很大的时候，会非常的占用内存。
# # 一般我们使用的时候都是这个样子的，比如：
#
# f = iter(fab(10))
#
# while True:
#     try:
#         print(next(f), end=',')
#     except StopIteration:
#         sys.exit()

# 这样我们实际上是先生成了一个 1000 个元素的 list:f，然后我们再去使用这个 f。
# 现在，我们换一个方法：
# 因为我们实际使用的是 list 的遍历，也就是 list 的迭代器。那么我们可以让这个函数 fab
# 每次只返回一个迭代器——一个计算结果，而不是一个完整的 list：

# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a+b
#         n += 1
#
# #  这样，我们每次调用fab函数，比如这样：
# f = fab(10)
# for x in f:
#     print(x)

# 打个比方的话，yield有点像断点。     加了yield的函数，每次执行到有yield的时候，
# 会返回yield后面的值 并且函数会暂停，直到下次调用或迭代终止；
# yield后面可以加多个数值（可以是任意类型），但返回的值是元组类型的。

# def get():
#     m = 0
#     n = 2
#     l = ['s',1,3]
#     k = {1:1,2:2}
#     p = ('2', 's', 't')
#     while True:
#         m += 1
#         yield m
#         yield m, n, l, k, p
#
# it = get()
#
# print(next(it))  # 1
# print(next(it))  # (1, 2, ['s', 1, 3], {1: 1, 2: 2}, ('2', 's', 't'))
#
# print(next(it))  # 2
# print(type(next(it)))
# #  如果再加一句:  所以返回值的类型，应该是当前调用时，yield 返回值的类型。
# print(type(next(it)))  # <class 'int'>  #返回的是整形


# 字符串，列表或元组对象都可用于创建迭代器。
# 字符串（Strings）：
# 普通的旧字符串也是可迭代的。
# for s in 'hello':
#     print(s)

# 列表（Lists）：
# 这些可能是最明显的迭代。
# for x in [None,3,4.5,"foo",lambda : "moo",object,object()]:
#     print("{0} ({1})".format(x, type(x)))

# 元组（Tuples）：
# 元组在某些基本方面与列表不同，注意到以下示例中的可迭代对象使用圆括号而不是方括号，但输出与上面列表示例的输出相同
# for x in (None,3,4.5,"foo",lambda : "moo",object,object()):
#     print("{0} ({1})".format(x, type(x)))

# 字典（Dictionaries）：
# 字典是键值对的无序列表。当您使用for循环遍历字典时，您的虚拟变量将使用各种键填充。

# a = {
#       'apples' : 'tasty',
#   'bananas' : 'the best',
#   'brussel sprouts' : 'evil',
#   'cauliflower' : 'pretty good'
# }
#
# for sKey in a:
#     print("{0} are ({1})".format(sKey, a[sKey]))

# 使用自定义迭代器实现斐波那契数列
# class Fibonacci:
#
#     def __init__(self, count):
#         self.count = count
#
#     def __iter__(self):
#         self.i = 0
#         self.a, self.b = 0, 1
#         return self
#
#     def __next__(self):
#         if self.i < self.count:
#             self.i += 1
#             a_old = self.a
#             self.a, self.b = self.b, self.a+self.b
#             return a_old
#         else:
#             raise StopIteration
#
# for i in Fibonacci(10):
#     print(i, end=' ')

# 如教程所说，迭代器和生成器算是 Python 一大特色，其核心是基于迭代器协议来的。
# 而平时我们经常使用的 for in 循环体，本质就是迭代器协议的一大应用。
# 同时 Python 内置的集合类型（字符、列表、元组、字典）都已经实现了迭代器协议，所以才能使用
# for in 语句进行迭代遍历。for in 循环体在遇到 StopIteration 异常时，便终止迭代和遍历。
# 再说下可迭代、迭代器、生成器三个概念的联系和区别。
# 1、可迭代概念范围最大，生成器和迭代器肯定都可迭代，但可迭代不一定都是迭代器和生成器，
# 比如上面说到的内置集合类数据类型。可以认为，在 Python 中，只要有集合特性的，都可迭代。
# 2、迭代器，迭代器特点是，均可以使用 for in 和 next 逐一遍历。
# 3、生成器，生成器一定是迭代器，也一定可迭代。
# 至于 Python 中为何要引入迭代器和生成器，除了节省内存空间外，也可以显著提升代码运行速度。
# 自定义迭代器类示例和说明如下

# class MyIter():
#
#     def __init__(self):
#         """        为了示例，用一个简单的列表作为需迭代的数据集合，
#         并且私有化可视情况变为其他类型集合
#         """
#         self.__list1 = [1, 2, 3, 4]
#         self.__index = 0
#
#     def __iter__(self):
#         """
#         #该魔法方法，必须返回一个迭代器对象，如果self已经定义了__next__()魔法方法，则只需要返回self即可
#     #因为如上面所述，生成器一定是迭代器
#         """
#         return iter(self.__list1)
#
#     def __next__(self):
#         """#此处的魔法函数，python会自动记忆每次迭代的位置，无需再使用yield来处理
#     #在使用next(obj)时，会自动调用该魔法方法
#         """
#         res = self.__list1[self.__index]
#         self.__index += 1
#         return res

# 以上为自定义迭代器类的机制。
# 下面再示例说明下，如何自定义生成器函数，因为大多数实战场景中，
# 使用生成器函数可能会更多一些:

# def my_gene_func():
#     index = 0
#     li = [1, 2, 3, 4]
#     yield li[index]
#
# # 调用以上函数时，会返回一个生成器对象，然后对该生成器对象，
# # 使用 next() 逐一返回:
# gene = my_gene_func()
# print(next(gene))

# 其实核心的概念还是记忆上次迭代的位置，类中直接使用 __next__ 魔法方法实现，
# 函数中使用 yield 实现。且怀疑，类中的 __next__ 魔法方法底层也是使用 yield
#  来实现的。
# 迭代器和生成器具体应用场景，就凡是需要提升运行效率或节约内存资源，
# 且遍历的数据是集合形式的，都可以考虑。
# 另外一个小众的使用场景，是变相实现协程的效果，即在同一个线程内，
# 实现不同任务交替执行
def mytask1():
    print('task1 开始执行')
    '''task code'''
    yield

def mytask2():

     print('task2 开始执行')
     '''task code'''
     yield


genel = mytask1()
gene2 = mytask2()

for i in range(100):
    next(genel)
    next(gene2)