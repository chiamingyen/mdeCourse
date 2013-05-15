#@+leo-ver=5-thin
#@+node:amd_yen.20130429221223.10899: * @file About.py
#coding: utf-8


#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:amd_yen.20130429221223.10900: ** <<declarations>> (About)
from AboutDialog import Ui_AboutDialog
from PyQt4 import QtGui,QtCore
#@-<<declarations>>
#@+others
#@+node:amd_yen.20130429221223.10901: ** class About
class About(QtGui.QMainWindow,Ui_AboutDialog):
    #@+others
    #@+node:amd_yen.20130429221223.10902: *3* __init__
    def __init__(self,parent=None):
        super(About,self).__init__(parent)
        self.setupUi(self)
        self.connect(self.pushButton,QtCore.SIGNAL('clicked()'),QtCore.SLOT('close()'))
    #@-others
#@-others
#@-leo
