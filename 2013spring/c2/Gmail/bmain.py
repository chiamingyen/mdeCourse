#@+leo-ver=5-thin
#@+node:amd_yen.20130429221223.10908: * @file bmain.py
#encoding: utf-8
# 從 MainWindow 導入 UI_Mainwindow 物件


#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:amd_yen.20130429221223.10909: ** <<declarations>> (bmain)
from MainWindow import Ui_MainWindow
from About import About
from PyQt4 import QtGui,QtCore
from Missing import Missing
from GMail import GMail
#@-<<declarations>>
#@+others
#@+node:amd_yen.20130429221223.10910: ** class Main
class Main(QtGui.QMainWindow, Ui_MainWindow):
    #@+others
    #@+node:amd_yen.20130429221223.10911: *3* __init__
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.sendMailwidget.hide()

        self.lineEdit_2.setEchoMode(True)
        # 訊號與 slot(動作) 的連結,  動作依靠回呼函式的呼叫執行
        self.connect(self.actionSendMail,QtCore.SIGNAL('triggered()'),self.ShowsendMailwidget)
        self.connect(self.actionExit,QtCore.SIGNAL('triggered()'),QtCore.SLOT('close()'))
        self.connect(self.actionAbout,QtCore.SIGNAL('triggered()'),self.aboutMessage)
        self.connect(self.sendemailButton,QtCore.SIGNAL('clicked()'),self.sendMailaction)
    #@+node:amd_yen.20130429221223.10912: *3* ShowsendMailwidget
    def ShowsendMailwidget(self):
        self.sendMailwidget.show()
    #@+node:amd_yen.20130429221223.10913: *3* sendMailaction
    def sendMailaction(self):
        emptyfields = self.checkEmptyfields()
        if len(emptyfields) !=0:
            self.missing = Missing(emptyfields)
            self.missing.show()
        else:
            self.gmail = GMail(str(self.lineEdit.text()),str(self.lineEdit_2.text()))
            self.gmail.sendMail(str(self.lineEdit_3.text()),str(self.lineEdit_4.text()),str(self.textEdit.toPlainText()))
            self.widgetHide()
    #@+node:amd_yen.20130429221223.10914: *3* aboutMessage
    def aboutMessage(self):
        self.sendMailwidget.hide()
        self.about = About()
        self.about.show()
    #@+node:amd_yen.20130429221223.10915: *3* widgetHide
    def widgetHide(self):
        self.sendMailwidget.hide()
    #@+node:amd_yen.20130429221223.10916: *3* checkEmptyfields
    def checkEmptyfields(self):
        emptyfields = set([])
        if len(self.lineEdit.text())==0:
            emptyfields.add("Your gmail")
        if len(self.lineEdit_2.text())==0:
            emptyfields.add("Your password")
        if len(self.lineEdit_3.text())==0:
            emptyfields.add("Receiver mail")
        if len(self.textEdit.toPlainText())==0:
            emptyfields.add("Your mail")
        return emptyfields
    #@-others
#@-others
#@-leo
