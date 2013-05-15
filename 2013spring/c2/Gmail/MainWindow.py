#@+leo-ver=5-thin
#@+node:amd_yen.20130429221223.10925: * @file MainWindow.py
#coding: utf-8
# 主視窗 ui 設計


#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:amd_yen.20130429221223.10926: ** <<declarations>> (MainWindow)
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
#@+node:amd_yen.20130429221223.10927: ** class Ui_MainWindow
class Ui_MainWindow(object):
    #@+others
    #@+node:amd_yen.20130429221223.10928: *3* setupUi
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(602, 311)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.sendMailwidget = QtGui.QWidget(self.centralwidget)
        self.sendMailwidget.setGeometry(QtCore.QRect(0, 0, 601, 271))
        self.sendMailwidget.setObjectName(_fromUtf8("sendMailwidget"))
        self.label = QtGui.QLabel(self.sendMailwidget)
        self.label.setGeometry(QtCore.QRect(360, 10, 91, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.sendMailwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 60, 111, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(self.sendMailwidget)
        self.lineEdit.setGeometry(QtCore.QRect(360, 30, 201, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.sendMailwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 90, 201, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.textEdit = QtGui.QTextEdit(self.sendMailwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 321, 141))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_3 = QtGui.QLabel(self.sendMailwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 91, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.sendMailwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 54, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_3 = QtGui.QLineEdit(self.sendMailwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 210, 251, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.sendemailButton = QtGui.QPushButton(self.sendMailwidget)
        self.sendemailButton.setGeometry(QtCore.QRect(380, 200, 85, 27))
        self.sendemailButton.setObjectName(_fromUtf8("sendemailButton"))
        self.label_5 = QtGui.QLabel(self.sendMailwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 120, 71, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_4 = QtGui.QLineEdit(self.sendMailwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(360, 140, 201, 27))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSendMail = QtGui.QAction(MainWindow)
        self.actionSendMail.setObjectName(_fromUtf8("actionSendMail"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionSendMail)
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    #@+node:amd_yen.20130429221223.10929: *3* retranslateUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "主視窗標題", None))
        self.label.setText(_translate("MainWindow", "Your Gmail", None))
        self.label_2.setText(_translate("MainWindow", "Your Password", None))
        self.label_3.setText(_translate("MainWindow", "Your Mail", None))
        self.label_4.setText(_translate("MainWindow", "Sendto", None))
        self.sendemailButton.setText(_translate("MainWindow", "Send Email", None))
        self.label_5.setText(_translate("MainWindow", "Mail Topic", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionSendMail.setText(_translate("MainWindow", "SendMail", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
    #@-others
#@-others
#@-leo
