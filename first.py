'''
Author: FunctionSir
Date: 2021-09-21 09:43:20
LastEditTime: 2021-11-13 23:04:19
LastEditors: FunctionSir
Description: 若第一次运行则执行的文件
FilePath: /Trknights/first.py
'''

import os
import getch
import cpsc
import ufio


def check_dirs():
    print(">检查与创建必要的文件夹<")
    print("[conf]\t", end="")
    if os.path.isdir("conf") == False:
        print("NE,MKDIR")
        cpsc.mkdir("", "conf")
    else:
        print("OK,PASS")
    print("[data]\t", end="")
    if os.path.isdir("data") == False:
        print("NE,MKDIR")
        cpsc.mkdir("", "data")
    else:
        print("OK,PASS")
    print("[temp]\t", end="")
    if os.path.isdir("temp") == False:
        print("NE,MKDIR")
        cpsc.mkdir("", "temp")
    else:
        print("OK,PASS")
    return 0


def check_conf_files():
    print(">检查与创建必要的配置文件<")
    print("[conf/env]\t", end="")
    if os.path.isfile(ufio.path_proc("conf/env", False)) == False:
        print("NE,MKFILE")
        ufio.new(True, "conf", "env")
    else:
        print("OK,PASS")
    print("[conf/main]\t", end="")
    if os.path.isfile(ufio.path_proc("conf/main", False)) == False:
        print("NE,MKFILE")
        ufio.new(True, "conf", "main")
    else:
        print("OK,PASS")
    return 0


def start():
    print("先前存在的相关数据可能被破坏。")
    print("要继续么？按下y(es)/n(o)]")
    while True:
        ch = getch.getch()
        if ch == "y":
            print("[I]开始执行操作。")
            check_dirs()
            check_conf_files()
            break
        elif ch == "n":
            print("[I]用户已取消")
            break
        else:
            print("[E]未知输入，可能是Caps Lock打开？请确保是小写y或小写n。")
    return 0


print("输入start来启动第一次运行向导,输入readme来查看README.md（包含有用的信息），exit来退出。")
print("推荐您仔细阅读README.md。")
while True:
    c = input("user@tarknights: ~ $ ")  # 仿BASH
    if c == "exit":
        exit()
    elif c == "start":
        start()
    elif c == "readme":
        cpsc.more("", "README.md")
        print()
    else:
        print("tarknights: "+c+": 未找到命令")
print("[EOF]")
