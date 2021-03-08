# -*- coding: utf-8 -*-
# __author__ = 'lenovo'

# 以下实例用于判断用户输入的年份是否为闰年：
# year = int(input("输入一个年份: "))
# if (year%4) == 0:
#     if (year%100) == 0:
#         if (year%400) == 0:
#             print("{0} 是闰年".format(year))  # 整百年能被400整除的是闰年
#         else:
#             print("{0} 不是闰年".format(year))
#     else:
#         print("{0} 是闰年".format(year))  # 非整百年能被4整除的为闰年
# else:
#     print("{0} 不是闰年".format(year))

# year = int(input("请输入一个年份："))
# if year%4 == 0 and year%100 != 0 or year%4 == 0:
#     print("{0}是闰年".format(year))
# else:
#     print("{0}不是闰年".format(year))

# 但其实 Python 的 calendar 库中已经封装好了一个方法 isleap() 来实现这个判断是否为闰年：
# import calendar
#
# print(calendar.isleap(2000))
# print(calendar.isleap(1900))
# year = int(input("请输入年份："))
# check_year = calendar.isleap(year)
# if check_year == True:
#     print("闰年")
# else:
#     print("平年")

# 简洁的代码最漂亮
year = int(input("请输入年份："))
print('闰年' if (year%4 == 0 and year%100 != 0) or year%400 ==0 else '平年')




















