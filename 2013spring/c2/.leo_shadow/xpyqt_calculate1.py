#@+leo-ver=4-thin
#@+node:amd_yen.20130429221223.2322:@shadow c2/pyqt_calculate1.py
#encoding: utf-8
import sys
from math import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit(
            "Type an expression and press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.connect(self.lineedit,
            SIGNAL("returnPressed()"),
            self.updateUi)
        self.setWindowTitle("Calculate")

    def updateUi(self):
        try:
            text = self.lineedit.text()
            self.browser.append(
                "%s = <b>%s</b>" % (text, eval(text)))
        except:
            self.browser.append(
                "<font color=red>%s is invalid!</font>"
                % text)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
#@nonl
#@-node:amd_yen.20130429221223.2322:@shadow c2/pyqt_calculate1.py
#@-leo
