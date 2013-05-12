#@+leo-ver=4-thin
#@+node:amd_yen.20130317160119.1727:@shadow c2/pyqt_geardesign.py
#coding: utf-8
# 資料來源: http://www.wellho.net/resources/ex.php4?item=y206/Voter_qt.py
import sys

from PyQt4 import QtGui
from PyQt4 import QtCore

class MainWindow(QtGui.QDialog):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        QtGui.QMainWindow.__init__(self)
        self.resize(250,150)
        self.setWindowTitle('選擇齒型')

        齒型分類 = ['第一類','第二類','第三類','第四類']
        self.vote = QtGui.QPushButton("執行設計運算",self)
        self.quit = QtGui.QPushButton("退出",self)
        self.chooseBox = QtGui.QComboBox()
        self.chooseBox.addItems(齒型分類)
        self.feedback = QtGui.QLabel("請務必選擇一種齒型!")

        self.grid = QtGui.QVBoxLayout()

        self.grid.addWidget(self.chooseBox)
        self.grid.addWidget(self.vote)
        self.grid.addWidget(self.feedback)
        self.grid.addWidget(self.quit)
        self.setLayout(self.grid)

        self.connect(self.quit, QtCore.SIGNAL("clicked()"), self.退出)
        self.connect(self.vote, QtCore.SIGNAL("clicked()"), self.紀錄)

        self.i_likes = "沒有選擇"

    def 退出(self):
        sys.exit()

    def 紀錄(self):
        self.i_likes = self.chooseBox.currentText()
        self.feedback.setText("所選的齒型為 - " + self.i_likes)
        fh = open("geardesign.txt","a")
        fh.write("選擇齒型為 "+self.i_likes+"\n")
        fh.close()

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
# 在 PyQt 4.5 與 Python3 環境下可以直接使用 exec() 但是也可以使用舊版的 exec_()
sys.exit(app.exec_())
#@nonl
#@-node:amd_yen.20130317160119.1727:@shadow c2/pyqt_geardesign.py
#@-leo
