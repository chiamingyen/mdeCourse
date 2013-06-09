import zmq
import random
import sys
import time

port = "5556"
內容 = zmq.Context()
通信 = 內容.socket(zmq.PAIR)
通信.connect("tcp://localhost:%s" % port)

while True:
    接收資料 = 通信.recv().decode("utf-8")
    print(接收資料)
    通信.send_unicode("連線到伺服器 1")
    通信.send_unicode("連線到伺服器 2")
    time.sleep(1)
