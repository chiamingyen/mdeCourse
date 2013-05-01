#@+leo-ver=4-thin
#@+node:amd_yen.20130429221223.2318:@shadow c2/pyqt_add1.py
#encoding: utf-8
# 一舉將所有的 Qt 物件導入
from PyQt4.Qt import *
'''
# 或者局部導入所用到的 Qt 物件
from PyQt4.QtGui import *
# 為了使用 Qt.Horizontal, 必須導入 PyQt4.QtCore
from PyQt4.QtCore import *
'''

應用程式 = QApplication([])

按鈕1 = QPushButton("&Quit")
按鈕2 = QPushButton("&Ok")
單行輸入區1 = QLineEdit("輸入第一數")
單行輸入區2 = QLineEdit("輸入第二數")
# 或者可以利用 setText() 設定顯示內容
單行輸入區1.setText("請輸入第一數")
文字顯示區1 = QTextBrowser()
滑動桿 = QSlider(Qt.Horizontal)
# 滑動桿數字範圍設定
滑動桿.setRange(200, 400)

數字軸 = QSpinBox()
# 數字軸前方加上 $ 符號
數字軸.setPrefix("$")
# 數字軸數字範圍設定
數字軸.setRange(200, 400)

# 將滑動桿與數字軸的資料互相連結
數字軸.valueChanged.connect(滑動桿.setValue)
滑動桿.valueChanged.connect(數字軸.setValue)

def updateUi():
    try:
        變數1 = float(單行輸入區1.text())
        變數2 = float(單行輸入區2.text())
        兩數相加 = 變數1 + 變數2
        文字顯示區1.append("%s+%s=%f" % (單行輸入區1.text(), 單行輸入區2.text(), 兩數相加))
    except:
        文字顯示區1.append( \
            "<font color=red>%s 資料錯誤!</font>" \
            % 單行輸入區1.text())

# 當按鈕2 按下後, 執行 updateUi 函式, updateUi 就是所謂的 callback (回呼)函式
按鈕2.clicked.connect(updateUi)


# QHBoxLayout 為 Horizontal (水平)配置方塊區
# QVBoxLayout 為 Vertical(垂直)配置方塊區
# 另外還有 QGridLayout 與 QFormLayout
方塊區 = QVBoxLayout()
方塊區.addWidget(按鈕1)
方塊區.addWidget(按鈕2)
方塊區.addWidget(滑動桿)
方塊區.addWidget(數字軸)
方塊區.addWidget(單行輸入區1)
方塊區.addWidget(單行輸入區2)
方塊區.addWidget(文字顯示區1)

組件 = QWidget()
組件.setLayout(方塊區)
# 其中只有按鈕1按下有反應
按鈕1.clicked.connect(組件.close)
組件.resize(400, 300)
組件.setWindowTitle("PyQt 視窗")
組件.show()
應用程式.exec_()

'''
# 有關 QGridLayout 用法
def buildLayout():
   grid_layout = QGridLayout()
   for row in range(3):
       for col in range(5):
           label = QLabel("Label %d,%d" % (row, col))
        grid_layout.addWidget(row, col, label)
  return grid_layout
  
# 有關 QFormLayout 用法
def buildLayout():
  form_layout = QFormLayout()
  form_layout.addRow("Name", QLineEdit())
  form_layout.addRow("Surname", QLineEdit())
  form_layout.addRow(QLabel("Custom text..."))
  return form_layout
'''
#@nonl
#@-node:amd_yen.20130429221223.2318:@shadow c2/pyqt_add1.py
#@-leo
