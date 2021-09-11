'''
Author: FunctionSir
Date: 2021-09-11 21:42:18
LastEditTime: 2021-09-11 23:21:26
LastEditors: FunctionSir
Description: 起始
FilePath: /Trknights/start.py
'''

import os
from typing import no_type_check
import getch
import math


def play():
    os.system(Python+" "+"hall.py")


Python = 'python'
Version = "0.1-alpha"
EnvConfFile = open("config/env")
ConfLines = EnvConfFile.read().splitlines()
i = -1
for Line in ConfLines:
    i = i+1
    if Line == "[Python]":
        Python = ConfLines[i+1]
    elif Line == "[Ver]":
        Version == ConfLines[i+1]
Width = os.get_terminal_size().columns
Hight = os.get_terminal_size().lines
HCenter = math.trunc(Hight/2)
OutLine = 2
print(("正在使用Python："+Python).center(Width-10))
for i in range(HCenter-OutLine-1):
    print()
print("按下P来开始游戏".center(Width-10))
print("按下E来退出".center(Width-10))
for i in range(HCenter-OutLine):
    print()
print(("版本："+Version).center(Width-10))
while 1:
    i = getch.getch()
    if i == 'p':
        play()
        exit()
    elif i == 'e':
        exit()
print("[EOF]")
