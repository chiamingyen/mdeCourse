
#encoding: utf-8
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

應用程式 = QApplication(sys.argv)

網際組件 = QWebView()
網際組件.load(QUrl("http://blog.kmol.info"))
網際組件.show()
# 在 PyQt 4.5 與 Python3 環境下可以直接使用 exec() 但是也可以使用舊版的 exec_()
應用程式.exec_()
