#encoding: utf-8
# MissingDialog ui 設計
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

class Ui_MissingDialog(object):
    def setupUi(self, MissingDialog):
        MissingDialog.setObjectName(_fromUtf8("MissingDialog"))
        MissingDialog.resize(402, 136)
        self.label = QtGui.QLabel(MissingDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.missingValueslabel = QtGui.QLabel(MissingDialog)
        self.missingValueslabel.setGeometry(QtCore.QRect(20, 40, 321, 21))
        self.missingValueslabel.setText(_fromUtf8(""))
        self.missingValueslabel.setObjectName(_fromUtf8("missingValueslabel"))
        self.pushButton = QtGui.QPushButton(MissingDialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 90, 71, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(MissingDialog)
        QtCore.QMetaObject.connectSlotsByName(MissingDialog)

    def retranslateUi(self, MissingDialog):
        MissingDialog.setWindowTitle(_translate("MissingDialog", "Missing Fields", None))
        self.label.setText(_translate("MissingDialog", "Missing Fields !!!", None))
        self.pushButton.setText(_translate("MissingDialog", "Ok", None))

