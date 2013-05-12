
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

class Dictionary(QWidget):

    def __init__(self, parent = None):
        super(Dictionary, self).__init__(parent)
        self.createLayout()
        self.createConnection()

    def search(self):
        baseUrl = "http://tw.dictionary.yahoo.com/search?ei=UTF-8&p="
        word = self.lineEdit.text()
        url = QUrl(baseUrl + word)
        self.webView.load(url)

    def createLayout(self):
        self.lineEdit = QLineEdit()
        self.goButton = QPushButton("&GO")
        h1 = QHBoxLayout()
        h1.addWidget(self.lineEdit)
        h1.addWidget(self.goButton)

        self.webView = QWebView()

        self.quitButton = QPushButton("&Quit")
        h2 = QHBoxLayout()
        h2.addStretch(1)
        h2.addWidget(self.quitButton)

        layout = QVBoxLayout()
        layout.addLayout(h1)
        layout.addWidget(self.webView)
        layout.addLayout(h2)

        self.setLayout(layout)

    def createConnection(self):
        self.lineEdit.returnPressed.connect(self.search)
        self.lineEdit.returnPressed.connect(self.lineEdit.selectAll)
        self.goButton.clicked.connect(self.search)
        self.goButton.clicked.connect(self.lineEdit.selectAll)
        self.quitButton.clicked.connect(self.close)


app = QApplication(sys.argv)

dictionary = Dictionary()
dictionary.show()
# 在 PyQt 4.5 與 Python3 環境下可以直接使用 exec() 但是也可以使用舊版的 exec_()
app.exec_()
