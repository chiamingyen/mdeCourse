#@+leo-ver=4-thin
#@+node:amd_yen.20130429141318.2218:@shadow c2/pyqt_browser3.py
#@@language python

import sys
from PyQt4 import QtCore, QtGui, QtWebKit

class Browser(QtGui.QMainWindow):

    def __init__(self):
        """
            Initialize the browser GUI and connect the events
        """

        QtGui.QMainWindow.__init__(self)
        self.resize(800,600)
        self.centralwidget = QtGui.QWidget(self)

        self.mainLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setMargin(1)

        self.frame = QtGui.QFrame(self.centralwidget)

        self.gridLayout = QtGui.QVBoxLayout(self.frame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)

        self.horizontalLayout = QtGui.QHBoxLayout()
        self.tb_url = QtGui.QLineEdit(self.frame)
        self.bt_back = QtGui.QPushButton(self.frame)
        self.bt_ahead = QtGui.QPushButton(self.frame)

        self.bt_back.setText("<")
        self.bt_ahead.setText(">")

        self.horizontalLayout.addWidget(self.bt_back)
        self.horizontalLayout.addWidget(self.bt_ahead)
        self.horizontalLayout.addWidget(self.tb_url)
        self.gridLayout.addLayout(self.horizontalLayout)

        self.html = QtWebKit.QWebView()
        self.gridLayout.addWidget(self.html)
        self.mainLayout.addWidget(self.frame)
        self.setCentralWidget(self.centralwidget)

        self.connect(self.tb_url, QtCore.SIGNAL("returnPressed()"), self.browse)
        self.connect(self.bt_back, QtCore.SIGNAL("clicked()"), self.html.back)
        self.connect(self.bt_ahead, QtCore.SIGNAL("clicked()"), self.html.forward)

        self.default_url = "http://blog.kmol.info/"
        self.tb_url.setText(self.default_url)
        self.browse()

    def browse(self):
        """
            Make a web browse on a specific url and show the page on the
            Webview widget.
        """

        url = self.tb_url.text() if self.tb_url.text() else self.default_url
        self.html.load(QtCore.QUrl(url))
        self.html.show()

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    main = Browser()
    main.show()
    # 在 PyQt 4.5 與 Python3 環境下可以直接使用 exec() 但是也可以使用舊版的 exec_()
    sys.exit(app.exec_())
#@nonl
#@-node:amd_yen.20130429141318.2218:@shadow c2/pyqt_browser3.py
#@-leo
