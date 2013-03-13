# -*- coding: utf-8 -*-
# 這裡要導入 math 模組,呼叫 sin(), cos() 與 pi 等數學函式
import math
間隔數 = 10

def header():
    return "dbCells = [\n"
    
def footer():
    return "];\n"
    
def addSinGraph(start, end):
    # 繪圖大小為 640x480
    return '[3,0,"=graph(\'line\',\'Sin 函式繪圖\',A'+str(start)+':A'+str(end)+',B'+str(start)+':B'+ \
    str(end)+',\'x 軸\',\'y 軸\',640,480)",""], // D1\n'
    
def addCosGraph(start, end):
    # 繪圖大小為 640x480
    return '[3,1,"=graph(\'line\',\'Cos 函式繪圖\',C'+str(start)+':C'+str(end)+',B'+str(start)+':B'+ \
    str(end)+',\'x 軸\',\'y 軸\',640,480)",""], // D2\n'
    
def addTime(end):

    timeData = ""
    for 索引 in range(end):
        timeData += '[1,'+str(索引)+',"'+str(索引*間隔數)+'",""],\n'
    return timeData
    
def addSin(end):
    sinData = ""
    角度 = math.pi/180.
    for 索引 in range(end):
        # 利用 round()取到小數點 2 位
        sinData += '[0,'+str(索引)+',"'+str(round(math.sin(索引*角度*間隔數),2))+'",""],\n'
    return sinData
    
def addCos(end):
    cosData = ""
    角度 = math.pi/180.
    for 索引 in range(end):
        # 利用 round()取到小數點 2 位
        cosData += '[2,'+str(索引)+',"'+str(round(math.cos(索引*角度*間隔數),2))+'",""],\n'
    return cosData

繪圖點數 = int(360/間隔數)+1
輸出 = header()+addSinGraph(1,繪圖點數)+addCosGraph(1,繪圖點數)+addTime(繪圖點數)+ \
addSin(繪圖點數)+addCos(繪圖點數)+footer()

print(輸出)
