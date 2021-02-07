# -*- encoding: UTF-8 -*-
# __author__ = 'lenovo'


number = 7
guess = -1
print("数字猜谜游戏！")


while guess != number:
    guess = int(input("请输入你认为的数字："))

    if guess == number:
        print("恭喜你答对了")
    elif guess > number:
        print("你的数字太大了。")
    elif guess < number:
        print("你的数字太小了。")

