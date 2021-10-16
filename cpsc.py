'''
Author: FunctionSir
Date: 2021-09-21 09:35:07
LastEditTime: 2021-10-16 22:13:16
LastEditors: FunctionSir
Description: CrossPlatformSystemCommands，自动判断操作系统的系统并执行指令
FilePath: /Trknights/cpsc.py
'''

import os
import platform
import ufio


def is_win():
    winString = "Windows"
    if platform.system() == winString:
        return(True)


def clear():
    winCmd = "cls"
    unixLikeCmd = "clear"
    if is_win():
        os.system(winCmd)
    else:
        os.system(unixLikeCmd)
    return(platform.system())


def mkfile(path, name):
    winCmd = "copy nul "  # 别忘记了结尾的空格，那很重要！
    unixLikeCmd = "touch "  # 别忘记了结尾的空格，那很重要！
    if is_win():
        os.system(winCmd+ufio.path_proc(path, True)+name)
    else:
        os.system(unixLikeCmd+ufio.path_proc(path, True)+name)


def mkdir(path, name):
    winCmd = "mkdir "
    unixLikeCmd = "mkdir "
    path = ufio.path_proc(path, True)
    if is_win():
        os.system(winCmd+path+name)
    else:
        os.system(unixLikeCmd+path+name)


def rmfile(path, name):
    winCmd = "del "  # 别忘记了结尾的空格，那很重要！
    unixLikeCmd = "rm "  # 别忘记了结尾的空格，那很重要！
    path = ufio.path_proc(path, True)
    if is_win():
        os.system(winCmd+path+name)
    else:
        os.system(unixLikeCmd+path+name)
