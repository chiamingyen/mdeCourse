
#encoding: utf-8
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

應用程式 = QApplication(sys.argv)

網際組件 = QWebView()
網際組件.load(QUrl("http://blog.kmol.info"))
網際組件.show()
應用程式.exec_()
