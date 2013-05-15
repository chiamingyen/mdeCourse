#!/usr/bin/env python
#@+leo-ver=5-thin
#@+node:amd.20130515005753.3872: * @file tiles.py
#@@first


#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:amd.20130515005753.3873: ** <<declarations>> (tiles)
from PyQt4.QtGui import QGraphicsRectItem,QBrush,QGraphicsItem,QPen,QColor,QPixmap
from PyQt4.QtCore import QRectF,Qt,SIGNAL,QObject
import settings
#@-<<declarations>>
#@+others
#@+node:amd.20130515005753.3874: ** class emitter
class emitter(QObject):
    #@+others
    #@+node:amd.20130515005753.3875: *3* __init__
    def __init__(self):
        QObject.__init__(self)
        self.emit(SIGNAL("steroidTaken"))
    #@-others
#@+node:amd.20130515005753.3876: ** class node
class node(QGraphicsRectItem,QObject):
    #@+others
    #@+node:amd.20130515005753.3877: *3* __init__
    def __init__(self):
        QGraphicsRectItem.__init__(self)
        QObject.__init__(self)
    #@-others
#@+node:amd.20130515005753.3878: ** class Wall
class Wall(node):
    #@+others
    #@+node:amd.20130515005753.3879: *3* __init__
    def __init__(self,x,y):
        node.__init__(self)
        self.setRect(QRectF(int(x),int(y),20,20))
        self.setBrush(QBrush(eval(settings.wall)))
        self.setPen(QPen(Qt.NoPen))
    #@-others
#@+node:amd.20130515005753.3880: ** class Player
class Player(node):
    #@+others
    #@+node:amd.20130515005753.3881: *3* __init__
    def __init__(self,x,y):
        node.__init__(self)
        self.setRect(QRectF(int(x),int(y),18,18))
        self.moveBy(1,1)
        self.setBrush(QBrush(eval(settings.player)))
        self.setPen(QPen(Qt.NoPen))
        self.setFlag(QGraphicsItem.ItemIsFocusable)
        self.steroidTaken = 0
    #@+node:amd.20130515005753.3882: *3* keyPressEvent
    def keyPressEvent(self,event):
        if event.key() == Qt.Key_Right:
            x = self.scenePos().x()+45  # Next pos
            y = self.scenePos().y()+25  # Hack

            if type(self.scene().itemAt(x,y)) == Steroid:
                self.steroidTaken += 1
                self.scene().itemAt(x,y).hide()
                self.scene().emit(SIGNAL("steroidTaken(int)"),self.steroidTaken)
            elif type(self.scene().itemAt(x,y)) == Oestrogen:
                self.steroidTaken -= 1
                self.scene().itemAt(x,y).hide()
                self.scene().emit(SIGNAL("steroidTaken(int)"),self.steroidTaken)

            if self.scene().itemAt(x,y) == None:
                self.moveBy(20,0)


        elif event.key() == Qt.Key_Up:
            x = self.scenePos().x()+25  # Hack
            y = self.scenePos().y()+5   # Next pos

            if type(self.scene().itemAt(x,y)) == Steroid:
                self.steroidTaken += 1
                self.scene().itemAt(x,y).hide()
                self.scene().emit(SIGNAL("steroidTaken(int)"),self.steroidTaken)
            elif type(self.scene().itemAt(x,y)) == Oestrogen:
                self.steroidTaken -= 1
                self.scene().itemAt(x,y).hide()
                self.scene().emit(SIGNAL("steroidTaken(int)"),self.steroidTaken)

            if self.scene().itemAt(x,y) == None:
                   self.moveBy(0,-20)


        elif event.key() == Qt.Key_Left:
            x = self.scenePos().x()+5   # Next pos
            y = self.scenePos().y()+25  # Hack

            if type(self.scene().itemAt(x,y)) == Steroid:
                self.steroidTaken += 1
                self.scene().itemAt(x,y).hide()
                self.scene().emit(SIGNAL("steroidTaken(int)"),self.steroidTaken)
            elif type(self.scene().itemAt(x,y)) == Oestrogen:
                self.steroidTaken -= 1
                self.scene().itemAt(x,y).hide()
                self.scene().emit(SIGNAL("steroidTaken(int)"),self.steroidTaken)

            if self.scene().itemAt(x,y) == None:
                self.moveBy(-20,0)


        elif event.key() == Qt.Key_Down:
            x = self.scenePos().x()+25  # Hack
            y = self.scenePos().y()+45  # Next pos

            if type(self.scene().itemAt(x,y)) == Steroid:
                self.steroidTaken += 1
                self.scene().itemAt(x,y).hide()
                self.scene().emit(SIGNAL("steroidTaken(int)"),self.steroidTaken)
            elif type(self.scene().itemAt(x,y)) == Oestrogen:
                self.steroidTaken -= 1
                self.scene().itemAt(x,y).hide()
                self.scene().emit(SIGNAL("steroidTaken(int)"),self.steroidTaken)

            if self.scene().itemAt(x,y) == None:
                self.moveBy(0,20)
    #@-others
#@+node:amd.20130515005753.3883: ** class Steroid
class Steroid(node):
    #@+others
    #@+node:amd.20130515005753.3884: *3* __init__
    def __init__(self,x,y):
        node.__init__(self)
        self.setRect(QRectF(int(x),int(y),20,20))
#        self.moveBy(2,2)
        self.setBrush(QBrush(eval(settings.steroid)))
        self.setPen(QPen(Qt.NoPen))
    #@-others
#@+node:amd.20130515005753.3885: ** class Oestrogen
class Oestrogen(node):
    #@+others
    #@+node:amd.20130515005753.3886: *3* __init__
    def __init__(self,x,y):
        node.__init__(self)
        self.setRect(QRectF(int(x),int(y),20,20))
        self.setBrush(QBrush(eval(settings.oestrogen)))
        self.setPen(QPen(Qt.NoPen))
    #@-others
#@-others
#@-leo
