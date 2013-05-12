#encoding: utf-8
from PyQt4.Qt import *

# 私有方法
def _一旦按下():
    print("按下按鍵!")

應用程式 = QApplication([])
按鈕 = QPushButton("按按看!")
# 若按鈕被按下則 SIGNAL("clicked()") 將會送出, 而動作(slot) 則是執行"_一旦按下"回呼函式
#QObject.connect(按鈕, SIGNAL("clicked()"), _一旦按下)
# 也可以直接由按鈕的特定方法(clicked) 中的連結(connect)來啟動 slot 動作(即呼叫 callback function)
按鈕.clicked.connect(_一旦按下)
# 讓按鈕可以顯示
按鈕.show()
# 在 PyQt 4.5 與 Python3 環境下可以直接使用 exec() 但是也可以使用舊版的 exec_()
應用程式.exec_()
