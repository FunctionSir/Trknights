'''
Author: FunctionSir
Date: 2021-09-21 09:43:20
LastEditTime: 2021-09-21 21:26:11
LastEditors: FunctionSir
Description: 第一次运行
FilePath: /Trknights/first.py
'''

import os
import mosc
import getch


def start():
    print("[W]所有先前存在的相关数据会删除")
    print("[I]继续么？按下y(es)/n(o)]")
    while True:
        ch = getch.getch()
        if ch == "y":
            print("[I]")
        elif ch == "n":
            print("[I]用户已取消")
            break
        else:
            print("[E]未知输入，可能是Caps Lock打开？请确保是小写y或小写n。")


print("[I]输入start来继续,exit来退出。")
print("INDEV!")
while True:
    c = input("player@tarknights: ~ $ ")  # 仿BASH
    if c == "exit":
        exit()
    elif c == "start":
        start()
    else:
        print("tarknights: "+c+": 未找到命令")
print("[EOF]")
