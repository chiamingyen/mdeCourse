#!/usr/bin/env python
#@+leo-ver=5-thin
#@+node:amd.20130515005753.3856: * @file scene.py
#@@first


#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:amd.20130515005753.3857: ** <<declarations>> (scene)
from PyQt4.QtGui import QGraphicsScene,QBrush,QColor,QPixmap
from PyQt4.QtCore import Qt
import tiles,settings
import os
#@-<<declarations>>
#@+others
#@+node:amd.20130515005753.3858: ** class Parser
class Parser(object):
    #@+others
    #@+node:amd.20130515005753.3859: *3* __init__
    def __init__(self,mapName):
        self.mapDir = os.getcwd()+"/maps/"
        self.maps = os.listdir(self.mapDir)
        self.map = 0
        self.read()
    #@+node:amd.20130515005753.3860: *3* read
    def read(self):
        file = open(self.mapDir+self.maps[self.map])
        map = file.read()
        lines = map.split("\n")
        self.tileList = []
        x = 0
        y = 0
        for y in range(len(lines)):
            nodes = lines[y].split("|")
            for x in range(len(nodes)):
                if nodes[x] == "wall" or nodes[x] == "w":
                    self.node = tiles.Wall(x*20,y*20)
                    self.tileList.append(self.node)
                elif nodes[x] == "player" or nodes[x] == "p":
                    self.node = tiles.Player(x*20,y*20)
                    self.tileList.append(self.node)
                elif nodes[x] == "steroid" or nodes[x] == "s":
                    self.node = tiles.Steroid(x*20,y*20)
                    self.tileList.append(self.node)
                elif nodes[x] == "oestrogen" or nodes[x] == "o":
                    self.node = tiles.Oestrogen(x*20,y*20)
                    self.tileList.append(self.node)
    #@+node:amd.20130515005753.3861: *3* list
    def list(self):
        return self.tileList
    #@+node:amd.20130515005753.3862: *3* nextMap
    def nextMap(self):
        self.map += 1
        self.read()
    #@-others
#@+node:amd.20130515005753.3863: ** class Scene
class Scene(QGraphicsScene):
    #@+others
    #@+node:amd.20130515005753.3864: *3* __init__
    def __init__(self):
        QGraphicsScene.__init__(self)
#        self.setSceneRect(0,0,560,420)
        self.setBackgroundBrush(QBrush(eval(settings.scene)))
        self.load()
    #@+node:amd.20130515005753.3865: *3* load
    def load(self):
        self.myParser = Parser("testmap.sth")
        self.nodes = self.myParser.list()

        for item in self.nodes:
            self.addItem(item)
            if type(item) == tiles.Player:
                player = item
                self.setFocusItem(item)
    #@-others
#@-others
#@-leo
