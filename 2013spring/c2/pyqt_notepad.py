#encoding: utf-8
import sys
from PyQt4.QtGui import QApplication, QMainWindow, QAction, QTextEdit, \
                                        QFileDialog, QMessageBox
from PyQt4.QtCore import pyqtSlot, QFile, QIODevice, QTextStream
 
class 文字編輯器(QMainWindow):
 
    def __init__(self, parent=None):
        super(文字編輯器, self).__init__(parent)
 
        # 定義功能表動作
        開檔 = QAction(self.tr("&Open..."), self)
        存檔 = QAction(self.tr("&Save..."), self)
        退出 = QAction(self.tr("&Exit"), self)
 
        # 設定事件處理訊號連結, 分別指到成員函式
        開檔.triggered.connect(self._open)
        存檔.triggered.connect(self._save)
        退出.triggered.connect(QApplication.instance().quit)
 
        # 建立下拉式功能表
        檔案功能表 = self.menuBar().addMenu(self.tr("&File..."))
 
        # 在檔案功能表區域增加開檔與存檔動作
        檔案功能表.addAction(開檔)
        檔案功能表.addAction(存檔)
 
        # 將退出動作作為獨立的功能表
        self.menuBar().addAction(退出)

        # 建立文字編輯物件
        self._textEdit = QTextEdit()
        # 將文字編輯物件放到組件中央
        self.setCentralWidget(self._textEdit)
 
        # 設定視窗標題
        self.setWindowTitle("文字編輯器")
 
    # 建立開檔的成員函式
    def _open(self):
        檔案名稱= QFileDialog.getOpenFileName(self,
                                               self.tr("Open file..."),
                                               "",
                                               self.tr("Text files (*.txt);;Python files (*.py *.pyw)"))
        if 檔案名稱:
            檔案物件 = QFile(檔案名稱)
            if not (檔案物件.open(QIODevice.ReadOnly)):
                QMessageBox.critical(self,
                                    # 利用 self.tr() 可以保障 PyQt 跨平台字串內容(?)
                                     self.tr("Error"),
                                     self.tr("Could not open file."))
                return
            # 利用 Stream line by line 讀取
            檔案內容 = QTextStream(檔案物件)
            # 利用 setCodec() 改變語系編碼
            檔案內容.setCodec("UTF-8")
            self._textEdit.setText(檔案內容.readAll())
            檔案物件.close()
 
 
    # 建立存檔的成員函式
    def _save(self):
        檔案名稱 = QFileDialog.getSaveFileName(self,
                                               self.tr("Save file"),
                                               '',
                                               self.tr("Text files (*.txt);;Python files (*.py *.pyw)"))
        if 檔案名稱:
            檔案物件 = QFile(檔案名稱)
            if not (file.open(QIODevice.WriteOnly)):
                QMessageBox.critical(self,
                                     self.tr("Error"),
                                     self.tr("Could not write to file."))
                return
            else:
                檔案內容 = QTextStream(檔案物件)
                # 利用 setCodec() 改變語系編碼
                檔案內容.setCodec("UTF-8")
                檔案內容 << self._textEdit.toPlainText()
                檔案內容.flush()
                檔案物件.close()
 
應用程式 = QApplication(sys.argv)
編輯器案例 = 文字編輯器()
編輯器案例.show()
應用程式.exec_()
