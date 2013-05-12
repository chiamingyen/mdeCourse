#@+leo-ver=4-thin
#@+node:amd_yen.20130501090735.3350:@shadow c2/pyside/browser1.py
#encoding: utf-8

import sys
from PySide import QtGui, QtCore, QtWebKit

class Browser(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)

		self.setWindowTitle("Web Browser")
		
		self.statusBar().showMessage("Ready", 5000)

		self.progress = 0
		self.homeURL = "http://www.google.com/"

		self.view = QtWebKit.QWebView(self)
		self.view.load(QtCore.QUrl(self.homeURL))
		self.view.loadProgress.connect(self.setProgress)
		self.view.titleChanged.connect(self.setTextProgress)
		self.view.loadFinished.connect(self.adjustLocation)
		self.view.loadFinished.connect(self.finishLoading)

		self.urlEdit = QtGui.QLineEdit(self)
		self.urlEdit.returnPressed.connect(self.chLocation)

		toolbar = self.addToolBar("Navigation")
		toolbar.addAction(self.view.pageAction(QtWebKit.QWebPage.Back))
		toolbar.addAction(self.view.pageAction(QtWebKit.QWebPage.Forward))
		toolbar.addWidget(self.urlEdit)
		toolbar.addAction(self.view.pageAction(QtWebKit.QWebPage.Reload))
		toolbar.addAction(self.view.pageAction(QtWebKit.QWebPage.Stop))

		closeAction = QtGui.QAction("&Exit", self)
		aboutAction = QtGui.QAction("&About", self)
		closeAction.triggered.connect(self.close)
		aboutAction.triggered.connect(self.aboutMess)

		menubar = QtGui.QMenuBar()
		fileMenu = QtGui.QMenu("&File")
		helpMenu = QtGui.QMenu("&Help")
		fileMenu.addAction(closeAction)
		helpMenu.addAction(aboutAction)
		menubar.addMenu(fileMenu)
		menubar.addMenu(helpMenu)
		self.setMenuBar(menubar)

		self.setCentralWidget(self.view)
	
	def aboutMess(self):
		QtGui.QMessageBox.information(self, "About Browser",
		                              "Tis is a simple web broswer\nVisit: http://samuelbr.com/",
		                              QtGui.QMessageBox.Ok)

	def setProgress(self, n):
		self.progress = n
		self.setTextProgress()
		self.adjustLocation()
	
	def setTextProgress(self):
		if 0 < self.progress < 100:
			self.setWindowTitle( "%s - BroWeb" % (self.view.title()) )
			self.statusBar().showMessage( "%s (%s%%)" % (self.view.url().toString(), self.progress) )
		else:
			self.setWindowTitle( "%s - BroWeb" % (self.view.title()) )
			self.statusBar().showMessage("Finished")
	
	def adjustLocation(self):
		self.urlEdit.setText(self.view.url().toString())
		self.urlEdit.setCursorPosition(0)
	
	def finishLoading(self):
		self.progress = 100
		self.setTextProgress()
		self.adjustLocation()
	
	def chLocation(self):
		url = QtCore.QUrl.fromUserInput(self.urlEdit.text())
		self.view.load(url)
		self.view.setFocus()

app = QtGui.QApplication(sys.argv)
b = Browser()
b.showMaximized()
# 在 PyQt 4.5 與 Python3 環境下可以直接使用 exec() 但是也可以使用舊版的 exec_()
sys.exit(app.exec_())
#@-node:amd_yen.20130501090735.3350:@shadow c2/pyside/browser1.py
#@-leo
