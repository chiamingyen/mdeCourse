#@+leo-ver=4-thin
#@+node:mde.20130609005025.2839:@shadow c1/w1_zmqcal1.py
#@@language python

#coding: utf-8
# 負責送出運算請求變數的 w1_zmqcal1.py
import zmq
import random
import time

內容 = zmq.Context()

通信 = 內容.socket(zmq.REQ)
通信.bind("tcp://*:7788")

# 等待所有 worker 完成連線
time.sleep(1)

計算次數 = 100

for 索引 in range(1, 計算次數+1):
    亂數1 = random.randint(0, 100)
    亂數2 = random.randint(0, 100)
    print('第 %d 次計算 %s + %s' % (索引, 亂數1, 亂數2), end="")

    # 將兩個亂數送到另一台電腦或執行緒進行運算
    通信.send_multipart([str(亂數1).encode("utf-8"), str(亂數2).encode("utf-8")])

    # 接收運算結果
    接收運算結果 = 通信.recv().decode("utf-8")
    print(' =', 接收運算結果)
#@nonl
#@-node:mde.20130609005025.2839:@shadow c1/w1_zmqcal1.py
#@-leo
