
#coding: utf-8
# 猜數字遊戲
import random
 
標準答案 = random.randint(1, 100)
你猜的數字 = int(input("請輸入您所猜的整數:"))
猜測次數 = 0
while 標準答案 != 你猜的數字:
    if 標準答案 < 你猜的數字:
        print("太大了，再猜一次 :)加油")
    else:
        print("太小了，再猜一次 :)加油")
    你猜的數字 = int(input("請輸入您所猜的整數:"))
    猜測次數 += 1
 
print("猜對了！總共猜了", 猜測次數, "次")
