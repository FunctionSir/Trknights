'''
Author: FunctionSir
Date: 2021-09-21 09:35:07
LastEditTime: 2021-09-21 09:58:16
LastEditors: FunctionSir
Description: MultiOSCommands，自动判断操作系统的系统并执行指令
FilePath: /Trknights/mosc.py
'''

import os
import platform


def is_win():
    if platform.system() == "Windows":
        return(True)


def clear():
    if is_win():
        os.system("cls")
    else:
        os.system("clear")
    return(platform.system())
