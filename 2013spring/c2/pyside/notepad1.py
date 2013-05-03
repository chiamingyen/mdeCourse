import sys
from PySide import QtGui, QtCore

class Editor(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        self.setWindowTitle("Text Editor")
        self.resize(640, 480)
        
        self.txtEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.txtEdit)
        
        self.statusBar().showMessage("Ready", 5000)
        
        openFile = QtGui.QAction("&Open", self)
        openFile.setShortcut(QtGui.QKeySequence.Open)
        openFile.setStatusTip("Open a file")
        
        newFile = QtGui.QAction("&New", self)
        newFile.setShortcut(QtGui.QKeySequence.New)
        newFile.setStatusTip("Create a new file")
        
        saveFile = QtGui.QAction("&Save", self)
        saveFile.setShortcut(QtGui.QKeySequence.Save)
        saveFile.setStatusTip("Save the file")
        
        saveAsFile = QtGui.QAction("S&ave as", self)
        saveAsFile.setShortcut(QtGui.QKeySequence.SaveAs)
        saveAsFile.setStatusTip("Save the file as")
        
        closeApp = QtGui.QAction("&Quit", self)
        closeApp.setShortcut(QtGui.QKeySequence.Close)
        closeApp.setStatusTip("Exit the application")
        
        openFile.triggered.connect(self.openFile)
        newFile.triggered.connect(self.newFile)
        saveFile.triggered.connect(self.saveFile)
        saveAsFile.triggered.connect(self.saveAsFile)
        closeApp.triggered.connect(self.close)
        
        undoEdit = QtGui.QAction("&Undo", self)
        undoEdit.setShortcut(QtGui.QKeySequence.Undo)
        undoEdit.setStatusTip("Undo")
        
        redoEdit = QtGui.QAction("&Redo", self)
        redoEdit.setShortcut(QtGui.QKeySequence.Redo)
        redoEdit.setStatusTip("Redo")
        
        cutText = QtGui.QAction("C&ut", self)
        cutText.setShortcut(QtGui.QKeySequence.Cut)
        cutText.setStatusTip("Cut")
        
        copyText = QtGui.QAction("&Copy", self)
        copyText.setShortcut(QtGui.QKeySequence.Copy)
        copyText.setStatusTip("Copy")
        
        pasteText = QtGui.QAction("&Paste", self)
        pasteText.setShortcut(QtGui.QKeySequence.Paste)
        pasteText.setStatusTip("Paste")
        
        selectAll = QtGui.QAction("&Select All", self)
        selectAll.setShortcut(QtGui.QKeySequence.SelectAll)
        selectAll.setStatusTip("Select All")
        
        undoEdit.triggered.connect(self.txtEdit.undo)
        redoEdit.triggered.connect(self.txtEdit.redo)
        cutText.triggered.connect(self.txtEdit.cut)
        copyText.triggered.connect(self.txtEdit.copy)
        pasteText.triggered.connect(self.txtEdit.paste)
        selectAll.triggered.connect(self.txtEdit.selectAll)
        
        formatText = QtGui.QAction("&Format", self)
        formatText.setStatusTip("Text Format")
        
        formatText.triggered.connect(self.formatText)
        
        menubar = QtGui.QMenuBar()
        fileMenu = QtGui.QMenu("&File")
        editMenu = QtGui.QMenu("&Edit")
        formatMenu = QtGui.QMenu("&Format")
        fileMenu.addAction(openFile)
        fileMenu.addAction(newFile)
        fileMenu.addSeparator()
        fileMenu.addAction(saveFile)
        fileMenu.addAction(saveAsFile)
        fileMenu.addSeparator()
        fileMenu.addAction(closeApp)
        editMenu.addAction(undoEdit)
        editMenu.addAction(redoEdit)
        editMenu.addSeparator()
        editMenu.addAction(cutText)
        editMenu.addAction(copyText)
        editMenu.addAction(pasteText)
        editMenu.addSeparator()
        editMenu.addAction(selectAll)
        formatMenu.addAction(formatText)
        menubar.addMenu(fileMenu)
        menubar.addMenu(editMenu)
        menubar.addMenu(formatMenu)
        self.setMenuBar(menubar)    
    
    def openFile(self):
        try:
            self.filename = QtGui.QFileDialog.getOpenFileName(self, "Open file")
            self.setWindowTitle("Text Editor - %s" % self.filename[0])
            f = open(self.filename[0], encoding="utf-8")
            self.txtEdit.setText(f.read())
        except:
            self.setWindowTitle("Text Editor")
    
    def newFile(self):
        self.e = Editor()
        self.e.show()
    
    def saveFile(self):
        try:
            f = open(self.filename[0], "w", encoding="utf-8")
            f.write(self.txtEdit.toPlainText())
        except:
            try:
                self.filename = QtGui.QFileDialog.getSaveFileName(self, "Save File")
                self.setWindowTitle("Text Editor - %s" % self.filename[0])
                f = open(self.filename[0], "w", encoding="utf-8")
                f.write(self.txtEdit.toPlainText())
            except:
                self.setWindowTitle("Text Editor")
    
    def saveAsFile(self):
        try:
            self.filename = QtGui.QFileDialog.getSaveFileName(self, "Save As")
            self.setWindowTitle("Text Editor - %s" % self.filename[0])
            f = open(self.filename[0], "w", encoding="utf-8")
            f.write(self.txtEdit.toPlainText())
        except:
            self.setWindowTitle("Text Editor")
    
    def formatText(self):
        (font, ok) = QtGui.QFontDialog.getFont()
        if ok:
            self.txtEdit.setFont(font)
        else:
            pass

app = QtGui.QApplication(sys.argv)
e = Editor()
e.show()
sys.exit(app.exec_())
