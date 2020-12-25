# -*- encoding: UTF-8 -*-
# __author__ = 'lenovo'


age = int(input("请输入狗的年龄："))

print("")

if age == 0:
    print("你是在逗我吗。")
elif age == 1:
    print("相当于14岁的人")
elif age >= 2:
    human = 22 + (age - 2) *5
    print("相当于人类年龄22岁。", human)

input("点击enter键退出！")

