
#encoding: utf-8
from PyQt4.QtGui import *
import sys

應用程式 = QApplication(sys.argv)

按鈕1 = QPushButton("&Quit")
按鈕2 = QPushButton("&Ok")
按鈕3 = QPushButton("&Quit1")
按鈕4 = QPushButton("&Ok1")
# QHBoxLayout 為 Horizontal (水平)配置方塊區
方塊區 = QHBoxLayout()
方塊區.addWidget(按鈕1)
方塊區.addWidget(按鈕2)
方塊區.addWidget(按鈕3)
方塊區.addWidget(按鈕4)

組件 = QWidget()
組件.setLayout(方塊區)
# 其中只有按鈕1按下有反應
按鈕1.clicked.connect(組件.close)
組件.resize(400, 300)
組件.setWindowTitle("PyQt 視窗")
組件.show()
# 在 PyQt 4.5 與 Python3 環境下可以直接使用 exec() 但是也可以使用舊版的 exec_()
應用程式.exec_()
