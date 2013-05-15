# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'V:\tmp\mainwindow.ui'
#
# Created: Tue May 14 09:50:49 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(391, 372)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 20, 160, 82))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEdit1 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit1.setObjectName(_fromUtf8("lineEdit1"))
        self.verticalLayout.addWidget(self.lineEdit1)
        self.lineEdit_2 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 61, 80))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label1 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.verticalLayout_2.addWidget(self.label1)
        self.label2 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label2.setObjectName(_fromUtf8("label2"))
        self.verticalLayout_2.addWidget(self.label2)
        self.label3 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label3.setObjectName(_fromUtf8("label3"))
        self.verticalLayout_2.addWidget(self.label3)
        self.label4 = QtGui.QLabel(self.centralWidget)
        self.label4.setGeometry(QtCore.QRect(20, 130, 58, 15))
        self.label4.setObjectName(_fromUtf8("label4"))
        self.textBrowser = QtGui.QTextBrowser(self.centralWidget)
        self.textBrowser.setGeometry(QtCore.QRect(100, 120, 171, 231))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton1 = QtGui.QPushButton(self.centralWidget)
        self.pushButton1.setGeometry(QtCore.QRect(280, 20, 93, 28))
        self.pushButton1.setObjectName(_fromUtf8("pushButton1"))
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 70, 93, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.pushButton1, QtCore.SIGNAL(_fromUtf8("clicked()")), self.getAverage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label1.setText(_translate("MainWindow", "num1", None))
        self.label2.setText(_translate("MainWindow", "num2", None))
        self.label3.setText(_translate("MainWindow", "num3", None))
        self.label4.setText(_translate("MainWindow", "result", None))
        self.pushButton1.setText(_translate("MainWindow", "average", None))
        self.pushButton_2.setText(_translate("MainWindow", "exit", None))
    
    def getAverage(self):
        # 利用 text() 方法取得 lineEdit 所輸入的內容
        第一數 = float(self.lineEdit1.text())
        第二數 = float(self.lineEdit_2.text())
        第三數 = float(self.lineEdit_3.text())
        平均 = (第一數+第二數+第三數)/3
        字串 = str(第一數)+"+"+str(第二數)+"+"+str(第三數)+"平均為:"+str(平均)
        # 利用 append() 方法將內容字串插入 textBrowser 資料框中
        self.textBrowser.append(字串)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

