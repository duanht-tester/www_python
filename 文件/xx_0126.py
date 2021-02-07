# -*- encoding: UTF-8 -*-
# __author__ = 'lenovo'


# 获取文件后缀：
# def getfile_fix(filemname):
#     return filemname[filemname.rfind('.') + 1:]
#
# print(getfile_fix('runoob.txt'))

"""
用户输入"xxx.txt"类文档文件名
用户输入被替换的"待替换字"
用户输入替换目标"新的字"
用户判断是否全部替换 yes/no
"""
# def file_replace(file_name, rep_world, new_world):
#     f_read = open(file_name)
#
#     content = []
#     count = 0
#
#     for eachline in f_read:
#         if rep_world in eachline:
#             count = count + eachline.count(rep_world)
#             eachline = eachline.replace(rep_world, new_world)
#         content.append(eachline)
#
#     decide = input('\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】：' \
#                    % (file_name, count, rep_world, rep_world, new_world))
#     if decide in ['YES', 'Yes', 'yes']:
#         f_write = open(file_name, 'w')
#         f_write.writelines(content)
#         f_write.close()
#
#     f_read.close()
#
#
# file_name = input('请输入文件名：')
# rep_world = input('请输入需要替换的单词或字符：')
# new_world = input('请输入新的单词或字符：')
# file_replace(file_name, rep_world, new_world)

"""
在上面的例子中，write(),read() 方法默认是写入到当前 .py 同文件夹下面的，
此外 w+ 的使用方法：不能直接 write() 后，在进行读取，这样试读不到数据的，
因为数据对象到达的地方为文件最后，读取是向后读的，因此，会读到空白，
应该先把文件对象移到文件首位
"""
# f = open("test0126.txt", 'w+', encoding='utf-8')
# f.write("可以 ，你做的很好！ 6666")  # 此时文件对象在最后一行，如果读取，将读不到数据
# s = f.tell()   # 返回文件对象当前位置
# f.seek(0, 0)   # 移动文件对象至第一个字符
# str = f.read()
# print(s, str, len(str))
"""
看上面分享的笔记，有个大佬打开文件然后没有关闭。。。
一般来说推荐以下方法：
"""
# # 写
# with open('test0126.txt', 'w', encoding='utf-8') as f:
#     f.write('test')
#
# # 读
# with open('test0126.txt', 'r', encoding='utf-8') as f:
#     f.readlines()
#     # 执行完自动close，避免忘记关闭文件导致资源的占用。

"""
由于文件读写时都有可能产生 IOError，一旦出错，后面的 f.close() 就不会调用。
所以，为了保证无论是否出错都能正确的关闭文件，可以使用 try...finally 来实现：
"""
# try:
#     f = open("./test0126.txt", 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
""" 替换文本中的字符串 """
import os

def Replace(file_name, rep_word, new_word):
    with open(file_name) as f:
        content = []
        count = 0

        for eachline in f:
            if rep_word in eachline:
                count += eachline.count(rep_word)
                eachline = eachline.replace(rep_word, new_word)
            content.append(eachline)

        decide = input('文件 {0} 中共有{1}个【{2}】\n您确定要把所有的【{3}】替换为【{4}】吗？\n【YES/NO】：'.\
                       format(file_name, count, rep_word, rep_word, new_word))
        if decide in ['YES', 'Yes', 'yes']:
            with open(file_name, 'w') as f:
                f.writelines(content)
            print('Succeed')
        else:
            print('Exit')


if __name__ == '__main__':
    while True:
        file_name = input('请输入文件名：')

        if file_name in os.listdir():
            rep_word = input('请输入需要替换的单词或字符：')
            new_word = input('请输入新的单词或字符：')
            Replace(file_name, rep_word, new_word)
            break
        else:
            print('Do not find such a file {}'.format(file_name))





















