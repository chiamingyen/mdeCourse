
#encoding: utf-8
from PyQt4.QtGui import *
import sys

應用程式 = QApplication(sys.argv)
組件 = QWidget()
組件.resize(400, 300)
組件.setWindowTitle("PyQt 視窗")
組件.show()
應用程式.exec_()