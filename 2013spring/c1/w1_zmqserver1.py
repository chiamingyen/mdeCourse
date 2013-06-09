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
