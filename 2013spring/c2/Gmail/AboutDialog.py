#@+leo-ver=5-thin
#@+node:amd_yen.20130429221223.10903: * @file AboutDialog.py
#encoding: utf-8
# AboutDialog ui 設計


#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:amd_yen.20130429221223.10904: ** <<declarations>> (AboutDialog)
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
#@-<<declarations>>
#@+others
#@+node:amd_yen.20130429221223.10905: ** class Ui_AboutDialog
class Ui_AboutDialog(object):
    #@+others
    #@+node:amd_yen.20130429221223.10906: *3* setupUi
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName(_fromUtf8("AboutDialog"))
        AboutDialog.resize(257, 151)
        self.label = QtGui.QLabel(AboutDialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 191, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(AboutDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 191, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(AboutDialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 90, 71, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)
    #@+node:amd_yen.20130429221223.10907: *3* retranslateUi
    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(_translate("AboutDialog", "Dialog", None))
        self.label.setText(_translate("AboutDialog", "This is a simple app for Gmail", None))
        self.label_2.setText(_translate("AboutDialog", "Author Gkatziouras Emmanouil", None))
        self.pushButton.setText(_translate("AboutDialog", "Ok", None))
    #@-others
#@-others
#@-leo
