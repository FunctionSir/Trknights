'''
Author: FunctionSir
Date: 2021-09-11 21:42:18
LastEditTime: 2021-09-21 21:26:29
LastEditors: FunctionSir
Description: 起始
FilePath: /Trknights/start.py
'''

import os
import getch
import math
import mosc


def play():
    os.system(python+" "+"hall.py")


def first_run():
    os.system(python+" "+"first.py")


python = 'python'
version = "0.1-alpha"
envConfFile = open("config/env")
confLines = envConfFile.read().splitlines()
i = -1
for line in confLines:
    i = i+1
    if line == "[python]":
        python = confLines[i+1]
    elif line == "[Ver]":
        version == confLines[i+1]
width = os.get_terminal_size().columns
hight = os.get_terminal_size().lines
hCenter = math.trunc(hight/2)
outLine = 2
print(("正在使用python："+python).center(width-5))  # "-5"中5是全角字符和中文的数量。
for i in range(hCenter-outLine-1):
    print()
while os.path.isfile("data/first.lck") == False:
    print("似乎还没有进行第一次运行配置，即将进入第一次运行配置".center(width-26))
    for i in range(hCenter-outLine+1):
        print()
    print(("版本："+version).center(width-3))
    mosc.clear()
    first_run()
    mosc.clear()
    exit()
print("按下[P]来开始游戏".center(width-7))
print("按下[E]来退出".center(width-5))
for i in range(hCenter-outLine+1):
    print()
print(("版本："+version).center(width-3))
while True:
    i = getch.getch()
    if i == 'p':
        play()
        mosc.clear()
        exit()
    elif i == 'e':
        mosc.clear()
        exit()
print("[EOF]")  # 正常情况下不应执行至输出EOF。
