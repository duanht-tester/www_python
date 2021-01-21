# -*- encoding: UTF-8 -*-
# __author__ = 'lenovo'

# 斐波那契(fibonacci)数列模块
def fib01(n):      # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print('\n'"============")

def fib02(n):       # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

