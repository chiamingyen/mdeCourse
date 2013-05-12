#@+leo-ver=4-thin
#@+node:amd_yen.20130429141318.2173:@shadow c2/pyqt_2.py
#@@language python

#encoding: utf-8
from PyQt4.QtGui import *
import sys

應用程式 = QApplication(sys.argv)
組件 = QWidget()
組件.resize(400, 300)
組件.setWindowTitle("PyQt 視窗")
組件.show()
# 在 PyQt 4.5 與 Python3 環境下可以直接使用 exec() 但是也可以使用舊版的 exec_()
應用程式.exec_()
#@nonl
#@-node:amd_yen.20130429141318.2173:@shadow c2/pyqt_2.py
#@-leo
