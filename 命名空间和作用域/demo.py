# -*- encoding: UTF-8 -*-
# __author__ = 'lenovo'

# var_global = "global_var"       # 这个var_global就是全局作用域
# def globalFunc():
#     var_global = 'local_var'    # 这个就是局部变量
#
# class Demo():
#
#     class_demo_local_var = 'class member'   # 这里也是局部变量
#
#     def localFunc(self):
#         var_locals = 'local_func_var'    # 这里也是局部变量
"""
以上只是说明了全局变量仅仅是在 .py 文件中直接声明的变量叫全局变量，
还有在 .py 文件中直接写的逻辑代码块中，也是全局变量。也就是说在
if/elif/else/、try/except、for/while 等逻辑代码块中的变量。
这个教程中在介绍三种命令空间的时候，说查找变量的顺序为局部的命名
空间去 -> 全局命名空间 -> 内置命名空间，但是我理解的变量查找顺
序为：当前域 -> 外部域(如果有) -> 全局域 -> 内置域。
光说没有什么概念，我们来一段代码就清楚了。
我们以 demo1.py 为例子:
"""
# global_var = 'this  var  on  global space'
# '''
# 申明global_var这个位置就是全局域，也就是教程中所说的全局作用域，
# 同时它也是直接声明在文件中的，而不是声明在函数中或者类中的变量
# '''
#
# class Demo():
#     class_demo_local_var = 'class member'
#
#     '''
#   虽然class_demo_local_var在这里是局部变量，这个局部变量的域相对于var_locals是外部域，
#   所以可以直接被var_locals所在的更小的局部域访问
#     '''
#     def localFunc(self):
#         var_locals = 'local_func_var'
#         '''
#     这里也是局部变量，但是相对于class_demo_local_var变量，却是更小的域，
#     因此class_demo_local_var所在的哪个域无法访问到当前域来
#         '''
#         # 到这里会查找当前域中有没有class_demo_local_var这个变量，
#         # 然后再到相对于当前域的外部域去查找变量
#         print(self.class_demo_local_var)

"""
教程中写到 Python 中变量的查找顺序：“在局部找不到，便会去局部外的局部找（例如闭包），
再找不到就会去全局找，再去内置中找。可以看一个具体的例子。
Python 的一个内建值 int，我们首先将其赋值为 0，然后定义一个函数 fun1()。
"""
# int = 0
def fun1():
    # int = 1

    def fun2():
        # int = 2
        print(int)
    fun2()
    # 函数 fun1() 的作用就是调用函数 fun2() 来打印 int 的值。
    # 调用函数 fun1()：
fun1()

# 因为 local 中的 int = 2，函数将其打印出来。
# 将函数 fun2() 中的 int = 2 删除：
# 调用函数 fun1()：
# 因为 local 找不到 int 的值，就去上一层 non-local 寻找，发现 int = 1 并打印。
# 而进一步删除函数 fun1() 中的 int = 1：
# 因为 local 和 non-local 都找不到 int 的值，便去 global 中寻找，发现 int = 0 并打印。
# 若删除 int = 0这一条件：
# 因为 local、non-local、global 中都没有 int 的值，便去 built-in 中寻找 int 的值，即：




