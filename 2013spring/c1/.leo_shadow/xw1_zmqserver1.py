#@+leo-ver=4-thin
#@+node:mde.20130609005025.2837:@shadow c1/w1_zmqserver1.py
# zmq is the answer: http://vimeo.com/20605470
import zmq
import random
import sys
import time

埠號 = "5556"
內容 = zmq.Context()
通信 = 內容.socket(zmq.PAIR)
通信.bind("tcp://*:%s" % 埠號)

while True:
    通信.send_unicode("連線到伺服器 3")
    接收資料 = 通信.recv().decode("utf-8")
    print(接收資料)
    time.sleep(1)
#@nonl
#@-node:mde.20130609005025.2837:@shadow c1/w1_zmqserver1.py
#@-leo
