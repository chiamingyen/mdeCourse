#@+leo-ver=4-thin
#@+node:mde.20130609005025.2832:@shadow c1/w1_server1.py
#@@language python
#coding: utf-8
# 伺服器程式
# 導入 socket 模組
import socket

# 建立一個通信套接物件
通信 = socket.socket()
# 取得主機名稱
主機 = socket.gethostname()
# 設定埠號
埠號 = 12345
# 利用通信連線的 bind 方法, 設定主機與埠號
通信.bind((主機, 埠號))

# 等待客戶端連線
通信.listen(5)
while True:
    # 接受客戶端連線
    # 接受連線
    連線, 位址 = 通信.accept()
    print('連結來自:', 位址)
    連線.send('您已經與伺服器連線!'.encode("utf-8"))
    # 關閉連線
    連線.close()
#@nonl
#@-node:mde.20130609005025.2832:@shadow c1/w1_server1.py
#@-leo
