
#encoding: utf-8
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

應用程式 = QApplication(sys.argv)

網際組件 = QWebView()
框架 = 網際組件.page().mainFrame()
框架.evaluateJavaScript("alert('這裡先執行了 JavaScript 程式');")
網際組件.load(QUrl("http://xh.edx.tw"))
網際組件.show()
應用程式.exec_()
