#@+leo-ver=4-thin
#@+node:amd_yen.20130501090735.3346:@shadow c2/pyside/hello1.py
import sys
from PySide.QtCore import *
from PySide.QtGui import *

# Create a Qt application
app = QApplication(sys.argv)
# Create a Label and show it
label = QLabel("Hello World")
label.show()
# Enter Qt application main loop
app.exec_()
sys.exit()
#@nonl
#@-node:amd_yen.20130501090735.3346:@shadow c2/pyside/hello1.py
#@-leo
