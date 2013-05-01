#encoding: utf-8
from PyQt4.Qt import *
# 用來顯示 PyQt painter 所產生的圖檔
from PIL import Image

應用程式 = QApplication([])

class 組件(QWidget):
    def __init__(self):
        super(組件, self).__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('簡單的繪圖')
        self.resize(400, 300)
        self.show()
    def paintEvent(self, e):
        ''' 假如要存成圖檔
        繪圖影像 = QImage(400, 300, QImage.Format_ARGB32)
        繪圖物件 = QPainter(im)
        '''
        繪圖物件 = QPainter()
        繪圖物件.begin(self)
        繪圖物件.setPen(Qt.red)
        繪圖物件.fillRect(0, 0, 400, 300, Qt.white)
        繪圖物件.drawRect(100, 100, 200, 160)
        繪圖物件.drawLine(100, 100, 200, 25)
        繪圖物件.drawLine(300, 100, 200, 25)
        繪圖物件.drawRect(185, 220, 40, 40)
        繪圖物件.drawEllipse(150, 125, 35, 35)
        繪圖物件.drawEllipse(250, 125, 35, 35)
        繪圖物件.drawText(110, 75, 180, 25, \
                         Qt.AlignCenter,  \
                         "簡單的畫圖!")
        繪圖物件.end()
        ''' 假如要存成圖檔
        繪圖影像.save("test1.png
        '''

組件案例 = 組件()
'''在存檔情況下, 以 PIL 開啟檢視
影像檢視=Image.open('test1.png')
影像檢視.show()
'''
應用程式.exec_()
