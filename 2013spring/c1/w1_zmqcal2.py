
#coding: utf-8
# 負責執行運算的 w1_zmqcal2.py
# 可以 cal1 或 cal2 先後執行, 都能得到相同結果, 在行動商務網路, cal1 代表來自輕薄的行動商務硬體
# 而 cal2 則在遠端的超級運端主機上執行.
import os
import zmq

內容 = zmq.Context()

通信 = 內容.socket(zmq.REP)
通信.connect("tcp://localhost:7788")

print('Worker %s 正在執行中 ...' % os.getpid())

while True:
    # 接收兩個亂數
    第一數, 第二數 = 通信.recv_multipart()
    第一數 = int(第一數.decode("utf-8"))
    第二數 = int(第二數.decode("utf-8"))

    print('計算 %s + %s 並將結果傳回' % (第一數, 第二數))
    通信.send_unicode(str(第一數 + 第二數))
