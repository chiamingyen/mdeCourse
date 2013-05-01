#@+leo-ver=5-thin
#@+node:amd_yen.20130429221223.10896: * @file main.py
#encoding: utf-8


#@@language python
#@@tabwidth -4

#@+<<declarations>>
#@+node:amd_yen.20130429221223.10897: ** <<declarations>> (main)
import sys
from PyQt4.Qt import *
# 從 bmain.py 導入 Main 方法
from bmain import Main
#@-<<declarations>>
#@+others
#@+node:amd_yen.20130429221223.10898: ** main
def main():
    應用程式 = QApplication([])
    主視窗 = Main()
    主視窗.show()
    sys.exit(應用程式.exec_())
    
main()
#@-others
#@-leo
