
#encoding: utf-8
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

應用程式 = QApplication(sys.argv)

網際組件 = QWebView()
框架 = 網際組件.page().mainFrame()
# 允許使用 Firefox 所安裝的 plugin
網際組件.settings().setAttribute(QWebSettings.PluginsEnabled, True)
網際組件.settings().setAttribute(QWebSettings.JavascriptEnabled, True)
網際組件.settings().setAttribute(QWebSettings.AutoLoadImages, False)
網際組件.settings().setAttribute(QWebSettings.JavaEnabled, False)
框架.evaluateJavaScript("alert('這裡先執行了 JavaScript 程式');")
網際組件.load(QUrl("http://xh.edx.tw"))
網際組件.show()
# 在 PyQt 4.5 與 Python3 環境下可以直接使用 exec() 但是也可以使用舊版的 exec_()
應用程式.exec_()
