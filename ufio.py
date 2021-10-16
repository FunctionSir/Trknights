'''
Author: FunctionSir
Date: 2021-09-21 19:06:36
LastEditTime: 2021-10-16 22:04:48
LastEditors: FunctionSir
Description: UniversalFilesIO 通用文件IO
FilePath: /Trknights/ufio.py
'''

from math import isfinite
import os
import cpsc


def path_proc(path, slashAtEnd):
    if cpsc.is_win():
        path = path.replace("/", "\\")
    else:
        path = path.replace("\\", "/")
    if slashAtEnd and path[-1] != "/" and path[-1] != "\\":
        if cpsc.is_win():
            path = path + "\\"
        else:
            path = path + "/"
    return path


def new(overWritten, path, name):
    if overWritten and os.path.isfile(path_proc(path, True)+name):
        cpsc.rmfile(path, name)
    cpsc.mkfile(path, name)
