#@+leo-ver=5-thin
#@+node:amd_yen.20130429221223.10930: * @file Missing.py
#coding: utf-8


#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:amd_yen.20130429221223.10931: ** <<declarations>> (Missing)
from MissingDialog import Ui_MissingDialog
from PyQt4 import QtGui,QtCore
#@-<<declarations>>
#@+others
#@+node:amd_yen.20130429221223.10932: ** class Missing
class Missing(QtGui.QDialog,Ui_MissingDialog):
    #@+others
    #@+node:amd_yen.20130429221223.10933: *3* __init__
    def __init__(self,emptiness,parent=None):
        super(Missing,self).__init__(parent)
        self.setupUi(self)
        self.emptiness = emptiness
        self.connect(self.pushButton,QtCore.SIGNAL('clicked()'),QtCore.SLOT('close()'))
        labelstring = ""
        for i in range(len(self.emptiness)):
            labelstring = labelstring+" "+self.emptiness.pop()            
        self.missingValueslabel.setText(labelstring);
    #@-others
#@-others
#@-leo
