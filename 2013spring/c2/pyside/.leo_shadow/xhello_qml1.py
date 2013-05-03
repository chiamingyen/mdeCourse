#@+leo-ver=4-thin
#@+node:amd_yen.20130501090735.3347:@shadow c2/pyside/hello_qml1.py
# -*- coding: utf-8 -*-
 
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import QDeclarativeView
 
# Create Qt application and the QDeclarative view
app = QApplication(sys.argv)
view = QDeclarativeView()
# Create an URL to the QML file
url = QUrl('view.qml')
# Set the QML file and show
view.setSource(url)
view.show()
# Enter Qt main loop
sys.exit(app.exec_())
#@nonl
#@-node:amd_yen.20130501090735.3347:@shadow c2/pyside/hello_qml1.py
#@-leo
