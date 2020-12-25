# -*- encoding: UTF-8 -*-
# __author__ = 'lenovo'


# for 语句
# Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
#
# for循环的一般格式如下：
#
# for <variable> in <sequence>:
#     <statements>
# else:
#     <statements>

# languages = ["c", "c++", "java", "python"]
#
# for x in languages:
#     print(x)


# 以下 for 实例中使用了 break 语句，break 语句用于跳出当前循环体：

sites = ["Baidu", "Google", "Runoob", "Taobao"]

for site in sites:
    if site =="Runoob1":
        print("菜鸟教程")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据。")
print("完成循环。")

