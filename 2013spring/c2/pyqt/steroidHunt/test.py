#!/usr/bin/env python
#@+leo-ver=5-thin
#@+node:amd.20130515005753.3868: * @file test.py
#@@first


#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:amd.20130515005753.3869: ** <<declarations>> (test)
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
#@-<<declarations>>
#@+others
#@+node:amd.20130515005753.3870: ** class Main
class Main(QWidget):
    #@+others
    #@+node:amd.20130515005753.3871: *3* __init__
    def __init__(self):
        QWidget.__init__(self)
        layout = QHBoxLayout()
        view = QGraphicsView()
        self.scene = QGraphicsScene()
        rect = QRectF(20,20,60,60)
        item = QGraphicsRectItem(rect)

        self.setLayout(layout)
        layout.addWidget(view)
        view.setScene(self.scene)

        self.scene.addItem(item)

        self.scene.setBackgroundBrush(QBrush(QColor(30,100,30)))
        self.scene.setSceneRect(0,0,200,200)
        view.setAutoFillBackground(True)
    #@-others
#@-others
app = QApplication(sys.argv)
main = Main()
main.show()
app.exec_()
#@-leo
