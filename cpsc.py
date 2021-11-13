'''
Author: FunctionSir
Date: 2021-09-21 09:35:07
LastEditTime: 2021-11-13 23:01:30
LastEditors: FunctionSir
Description: CrossPlatformSystemCommands，自动判断操作系统的系统并执行指令
FilePath: /Trknights/cpsc.py
'''

import os
import platform
import ufio


def is_win():
    r = False
    winSymbol = "Windows"
    if os.path.isfile("thisiswindows.lck"):
        r = True
    elif os.path.isfile("thisisnotwindows.lck"):
        r = False
    else:
        if platform.system() == winSymbol:
            r = True
        else:
            r = False
    return r


def clear():
    r = -32768
    winCmd = "cls"
    unixLikeCmd = "clear"
    if is_win():
        r = os.system(winCmd)
    else:
        r = os.system(unixLikeCmd)
    return r


def mkfile(path, name):
    r = -32768
    path = ufio.path_proc(path, True)
    winCmd = "copy nul " + path + name
    unixLikeCmd = "touch " + path + name
    if is_win():
        r = os.system(winCmd)
    else:
        r = os.system(unixLikeCmd)
    return r


def mkdir(path, name):
    r = -32768
    path = ufio.path_proc(path, True)
    winCmd = "mkdir " + path + name
    unixLikeCmd = "mkdir " + path + name
    if is_win():
        r = os.system(winCmd)
    else:
        r = os.system(unixLikeCmd)
    return r


def rmfile(path, name):
    r = -32768
    path = ufio.path_proc(path, True)
    winCmd = "del " + path + name
    unixLikeCmd = "rm " + path + name
    if is_win():
        r = os.system(winCmd)
    else:
        r = os.system(unixLikeCmd)
    return r


def ping(dest):
    r = -32768
    winCmd = "ping " + dest
    unixLikeCmd = "ping -c 4 " + dest
    if is_win():
        r = os.system(winCmd)
    else:
        r = os.system(unixLikeCmd)
    return r


def more(path, name):
    r = -32768
    path = ufio.path_proc(path, True)
    winCmd = "more " + path + name
    unixLikeCmd = "more " + path + name
    if is_win():
        r = os.system(winCmd)
    else:
        r = os.system(unixLikeCmd)
    return r
