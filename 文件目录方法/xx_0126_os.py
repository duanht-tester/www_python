# -*- encoding: UTF-8 -*-
# __author__ = 'lenovo'


"""
OS 文件/目录方法
os 模块提供了非常丰富的方法用来处理文件和目录。常用的方法如下表所示：


序号	             方法及                                     描述
1   os.access(path, mode)                               检验权限模式
2	os.chdir(path)                                      改变当前工作目录
3	os.chflags(path, flags)                             设置路径的标记为数字标记。
4	os.chmod(path, mode)                                更改权限
5	os.chown(path, uid, gid)                            更改文件所有者
6   os.chroot(path)                                     改变当前进程的根目录
7   os.close(fd)                                        关闭文件描述符 fd
8   os.closerange(fd_low, fd_high)                      关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
9   os.dup(fd)                                          复制文件描述符 fd
10  os.dup2(fd, fd2)                                    将一个文件描述符 fd 复制到另一个 fd2
11  os.fchdir(fd)                                       通过文件描述符改变当前工作目录
12  os.fchmod(fd, mode)                                 改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
13  os.fchown(fd, uid, gid)                             修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
14  os.fdatasync(fd)                                    强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。
15  os.fdopen(fd[, mode[, bufsize]])                    通过文件描述符 fd 创建一个文件对象，并返回这个文件对象
16  os.fpathconf(fd, name)                              返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，
                                                        这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
17  os.fstat(fd)                                        返回文件描述符fd的状态，像stat()。
18  os.fstatvfs(fd)                                     返回包含文件描述符fd的文件的文件系统的信息，Python 3.3 相等于 statvfs()。
19  os.fsync(fd)                                        强制将文件描述符为fd的文件写入硬盘。
20  os.ftruncate(fd, length)                            裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。
21  os.getcwd()                                         返回当前工作目录
22  os.getcwdu()                                        返回一个当前工作目录的Unicode对象
23  os.isatty(fd)                                       如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
24  os.lchflags(path, flags)                            设置路径的标记为数字标记，类似 chflags()，但是没有软链接
25  os.lchmod(path, mode)                               修改连接文件权限
26  os.lchown(path, uid, gid)                           更改文件所有者，类似 chown，但是不追踪链接。
27  os.link(src, dst)                                   创建硬链接，名为参数 dst，指向参数 src
28  os.listdir(path)                        返回path指定的文件夹包含的文件或文件夹的名字的列表。
29  os.lseek(fd, pos, how)                  设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos;
                                            SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效
30  os.lstat(path)                                  像stat(),但是没有软链接
31  os.major(device)                                从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
32  os.makedev(major, minor)                        以major和minor设备号组成一个原始设备号
33  os.makedirs(path[, mode])               递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。
34  os.minor(device)                            从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。
35  os.mkdir(path[, mode])                      以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
36  os.mkfifo(path[, mode])                     创建命名管道，mode 为数字，默认为 0666 (八进制)
37  os.mknod(filename[, mode=0600, device])         创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。
38  os.open(file, flags[, mode])                打开一个文件，并且设置需要的打开选项，mode参数是可选的
39  os.openpty()                                打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
40  os.pathconf(path, name)                     返回相关文件的系统配置信息。
41  os.pipe()                                   创建一个管道. 返回一对文件描述符(r, w) 分别为读和写
42  os.popen(command[, mode[, bufsize]])        从一个 command 打开一个管道
43  os.read(fd, n)                          从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
44  os.readlink(path)                       返回软链接所指向的文件
45  os.remove(path)                         删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
46  os.removedirs(path)                 递归删除目录。
47  os.rename(src, dst)                 重命名文件或目录，从 src 到 dst
48  os.renames(old, new)                    递归地对目录进行更名，也可以对文件进行更名。
49  os.rmdir(path)                          删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
50  os.stat(path)                           获取path指定的路径的信息，功能等同于C API中的stat()系统调用。
51  os.stat_float_times([newvalue])         决定stat_result是否以float对象显示时间戳
52  os.statvfs(path)                        获取指定路径的文件系统统计信息
53  os.symlink(src, dst)                    创建一个软链接
54  os.tcgetpgrp(fd)                        返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组
55  os.tcsetpgrp(fd, pg)                    设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。
56  os.tempnam([dir[, prefix]])                 Python3 中已删除。返回唯一的路径名用于创建临时文件。
57  os.tmpfile()                        Python3 中已删除。返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。
58  os.tmpnam()Python3 中已删除。为创建一个临时文件返回一个唯一的路径
59  os.ttyname(fd)              返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。
60  os.unlink(path)             删除文件路径
61  os.utime(path, times)       返回指定的path文件的访问和修改的时间。
62  os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
                                    输出在文件夹中的文件名通过在树中游走，向上或者向下。
63  os.write(fd, str)               写入字符串到文件描述符 fd中. 返回实际写入的字符串长度
64  os.path 模块                      获取文件的属性信息。
65  os.pardir()                         获取当前目录的父目录，以字符串形式显示目录名。
"""
import os
import os.path
"""获取指定目录及其子目录下的 py 文件路径说明：l 用于存储找到的
 py 文件路径 get_py 函数，递归查找并存储 py 文件路径于 l"""
# l = []
# def get_py(path, l):
#     fileList = os.listdir(path)    # 获取path目录下所有文件
#     for filename in fileList:
#         pathTmp = os.path.join(path, filename)  # 获取path与filename组合后的路径
#         if os.path.isdir(pathTmp):  # 如果是目录
#             get_py(pathTmp, l)       # 则递归查找
#         elif filename[-3:].upper() == '.PY':  # 不是目录,则比较后缀名
#             l.append(pathTmp)
#
# path = input('请输入路径:').strip()
# get_py(path, l)
# print('在%s目录及其子目录下找到%d个py文件\n分别为：\n'% (path, len(l)))
# for filepath in l:
#     print(filepath + '\n')

# 显示所有视频格式文件，mp4，avi，rmvb
# import os
#
# def search_file(start_dir, target):
#     os.chdir(start_dir)
#     for each_file in os.listdir(os.curdir):
#         ext = os.path.splitext(each_file)[1]
#         if ext in target:
#             vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)
#         if os.path.isdir(each_file):
#             search_file(each_file, target)  # 递归调用
#             os.chdir(os.pardir)     # 递归调用后切记返回上一层目录
#
# start_dir = input('请输入待查找的初始目录：')
# program_dir = os.getcwd()
#
# target = ['.mp4', '.avi', '.rmvb']
# vedio_list = []
# search_file(start_dir, target)
#
# f = open(program_dir + os.sep + 'vedioList.txt', 'w')
# f.writelines(vedio_list)
# f.close()

"""
批量修改文件名
python 对文件进行批量改名用到的是 os 模块中的 listdir 方法和 rename 方法。
 os.listdir(dir) : 获取指定目录下的所有子目录和文件名
 os.rename(原文件名，新文件名） : 对文件或目录改名
把混乱的文件名改成有序的文件名:
"""
# import os
#
# path = input('请输入文件路径(结尾加上/)：')
#
# # 获取该目录下所有文件，存入列表中
# fileList = os.listdir(path)
#
# n = 0
# for i in fileList:
#
#     # 设置旧文件名（就是路径+文件名）
#     oldname = path + os.sep + fileList[n]
#     # 设置新文件名
#     newname = path + os.sep + 'a' +str(n+1) + 'JPG'
#
#     # 用os模块中的rename方法对文件改名
#     os.rename(oldname, newname)
#     print(oldname, '=====>', newname)
#
#     n += 1

"""
os.replace(old, new) 将文件重命名。
首先创建两个文件：
 1.txt 内容是1
 2.txt 内容是2
 """
import os
os.replace('1.txt', '2.txt')
"""
执行后发现只剩下一个：2.txt，但内容是 1。
所以 os.replace(file1,file2) 这个函数相当于用 file2 给
file1 重命名，并删除 file2。
"""













