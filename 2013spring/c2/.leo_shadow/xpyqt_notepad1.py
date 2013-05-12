#@+leo-ver=4-thin
#@+node:amd_yen.20130429141318.2176:@shadow c2/pyqt_notepad1.py
#@@language python

#encoding: utf-8
# 導入 QTextEdit 組件
from PyQt4.QtGui import QApplication, QTextEdit
import sys

應用程式 = QApplication(sys.argv)
文字編輯組件 = QTextEdit()
文字編輯組件.setText("編輯區內容")
文字編輯組件.setWindowTitle("文字編輯器")
文字編輯組件.show()
# 在 PyQt 4.5 與 Python3 環境下可以直接使用 exec() 但是也可以使用舊版的 exec_()
應用程式.exec_()
#@nonl
#@-node:amd_yen.20130429141318.2176:@shadow c2/pyqt_notepad1.py
#@-leo
