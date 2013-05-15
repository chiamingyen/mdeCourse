#coding: utf-8
from PyQt4 import QtGui
# 從主視窗介面程式檔案中, 導入介面類別
from Ui_mainwindow import Ui_MainWindow

if __name__ == "__main__":
    應用程式 = QtGui.QApplication([])
    主視窗 = QtGui.QMainWindow()
    介面 = Ui_MainWindow()
    介面.setupUi(主視窗)
    主視窗.show()
    應用程式.exec_()
