#!/usr/bin/env python
#@+leo-ver=5-thin
#@+node:amd.20130515005753.3850: * @file main.py
#@@first


#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:amd.20130515005753.3851: ** <<declarations>> (main)
import PyQt4,sys,mainwindow

if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    window = mainwindow.MainWindow()
    window.show()
    app.exec_()
#@-<<declarations>>
#@+others
#@-others
#@-leo
