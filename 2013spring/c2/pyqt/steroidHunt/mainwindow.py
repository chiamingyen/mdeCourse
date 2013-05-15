#@+leo-ver=5-thin
#@+node:amd.20130515005753.3852: * @file mainwindow.py
#coding: utf-8
#!/usr/bin/env python


#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:amd.20130515005753.3853: ** <<declarations>> (mainwindow)
from PyQt4.QtGui import QWidget,QFont,QLabel,QGraphicsView,QVBoxLayout,QPalette,QBrush,QColor,QHBoxLayout,QLCDNumber,QFrame
from PyQt4.QtCore import Qt,SIGNAL,SLOT
import scene
#@-<<declarations>>
#@+others
#@+node:amd.20130515005753.3854: ** class MainWindow
class MainWindow(QWidget):
    #@+others
    #@+node:amd.20130515005753.3855: *3* __init__
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(640,480)

        top = QWidget()
        topLayout = QHBoxLayout()
        top.setLayout(topLayout)

        title = QLabel("尋寶遊戲");
        title.setFont(QFont("verdana",25,QFont.Bold))
        topLayout.addWidget(title)

        lcd = QLCDNumber()
        lcd.setSegmentStyle(QLCDNumber.Flat)
        lcd.setFrameStyle(QFrame.StyledPanel|QFrame.Plain)
        topLayout.addWidget(lcd)

        self.myScene = scene.Scene()
        self.connect(self.myScene, SIGNAL("steroidTaken(int)"), lcd, SLOT("display(int)"))

        view = QGraphicsView()
        view.setAutoFillBackground(True)
        view.setScene(self.myScene)

        layout = QVBoxLayout()
        layout.addWidget(top)
        layout.addWidget(view)

        self.setLayout(layout)
    #@-others
#@-others
#@-leo
