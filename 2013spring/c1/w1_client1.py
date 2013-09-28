#coding: utf-8
# 客戶端程式
# 導入 socket 模組
import socket

# 建立一個通信套接物件
通信 = socket.socket()
# 取得主機名稱
主機 = socket.gethostname()
# 設定埠號
埠號 = 9000
# 利用通信套接物件的 connect 方法, 設定連線主機與埠號
通信.connect((主機, 埠號))

# 接收來自伺服器的封包, 並且將 bytes 資料解碼為字串
print((通信.recv(1024)).decode("utf-8"))
# 關閉通信套接物件
通信.close()
