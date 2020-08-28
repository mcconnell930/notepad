import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pathlib import Path

class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
	def initUI(self):
		self.textEditor = QTextEdit()
		self.setCentralWidget(self.textEditor)
		
		exit = QAction(QIcon("new.png"), "Edit", self)
		exit.setShortcut("Ctrl+Q")
		exit.triggered.connect(self.textEditor.clear)
		
		Cut = QAction(QIcon("cut.png"), "Cut", self)
		Cut.setShortcut("Ctrl+X")
		Cut.triggered.connect(self.textEditor.cut)
		
		Copy = QAction(QIcon("copy.png"), "Copy", self)
		Copy.setShortcut("Ctrl+C")
		Copy.triggered.connect(self.textEditor.copy)
		New = QAction(QIcon("new.png"), "New",self)
		New.setShortcut("Ctrl+N")
		New.triggered.connect(self.textEditor.clear)
		Open = QAction(QIcon("open.png"), "Open", self)
		Open.setShortcut("Ctrl+O")
		Open.triggered.connect(self.openn)
		
		Save = QAction(QIcon("save.png"), "Save", self)
		Save.setShortcut("Ctrl+S")
		Save.triggered.connect(self.saveFile)
		
		Paste = QAction(QIcon("paste.png"), "Paste", self)
		Paste.setShortcut("Ctrl+V")
		Paste.triggered.connect(self.textEditor.paste)
	
		
		
		
	
	
	
	
		
	
		
		self.statusbar = self.statusBar()
		self.statusbar.showMessage("running")
		
		menubar = self.menuBar()
		filemenu = menubar.addMenu("file")
		menubar.setNativeMenuBar(False)
		new = QMenu("New", self)
		newF = QAction("New file", self)
		newFF = QAction("New Tab", self)
		newF.triggered.connect(self.textEditor.clear)
		newFF.triggered.connect(self.textEditor.clear)
		new.addAction(newF)
		new.addAction(newFF)
		
		open = QAction("open", self)
		open.setShortcut("Ctrl+O")
		open.setStatusTip("open")
		open.triggered.connect(self.openn)
		
		
		save = QAction("save", self)
		save.setShortcut("Ctrl+S")
		save.setStatusTip("save file")
		save.triggered.connect(self.saveFile)
		
		saveAs = QAction("save As", self)
		saveAs.triggered.connect(self.saveFile)
		
		quit = QAction("Exit", self)
		quit.setShortcut("Ctrl+Q")
		quit.setStatusTip("exit program")
		quit.triggered.connect(self.close)
		
		view = QAction("view statusbar",self, checkable=True)
		view.setStatusTip("view statusbar")
		view.setChecked(True)
		view.triggered.connect(self.toggleMenu)
		self.toolbar = self.addToolBar('Exit')
		self.toolbar.addAction(exit)
		self.toolbar = self.addToolBar('Cut')
		self.toolbar.addAction(Cut)
		self.toolbar = self.addToolBar('Copy')
		self.toolbar.addAction(Copy)
		self.toolbar = self.addToolBar('Save')
		self.toolbar.addAction(Save)
		self.toolbar = self.addToolBar('Open')
		self.toolbar.addAction(Open)
		self.toolbar = self.addToolBar('Paste')
		self.toolbar.addAction(Paste)
		
		filemenu.addMenu(new)
		filemenu.addAction(open)
		filemenu.addAction(view)
		filemenu.addAction(save)
		filemenu.addAction(saveAs)
		filemenu.addAction(quit)
		
		editmenu = menubar.addMenu("Edit")
		copy = QAction("copy", self)
		copy.setShortcut("Ctrl+C")
		copy.triggered.connect(self.textEditor.copy)
		
		cut = QAction("cut", self)
		cut.setShortcut("Ctrl+X")
		cut.triggered.connect(self.textEditor.cut)
		
		paste = QAction("paste", self)
		paste.setShortcut("Ctrl+V")
		paste.triggered.connect(self.textEditor.paste)
		
		
		undo = QAction("Undo", self)
		undo.setShortcut("Ctrl+Z")
		undo.triggered.connect(self.textEditor.undo)
		
		
		redo = QAction("redo", self)
		redo.setShortcut("Ctrl+Y")
		redo.triggered.connect(self.textEditor.redo)
		
		
		selectAll = QAction("select all", self)
		selectAll.setShortcut("Ctrl+A")
		selectAll.triggered.connect(self.textEditor.selectAll)
		
		editmenu.addAction(copy)
		editmenu.addAction(cut)
		editmenu.addAction(paste)
		editmenu.addAction(undo)
		editmenu.addAction(redo)
		editmenu.addAction(selectAll)
		
		formatMenu = menubar.addMenu("format")
		changeBg =  QAction("change background", self)
		changeBg.triggered.connect(self.changeBg)
		
		
		changeFont = QAction("Change Font",self)
		changeFont.triggered.connect(self.changeFont)
		
		formatMenu.addAction(changeBg)
		formatMenu.addAction(changeFont)
		
		helpmenu = menubar.addMenu("help")
		
		about = QAction("About", self)
		about.triggered.connect(self.about)
		
		
		help = QAction("help", self)
		help.triggered.connect(self.help)
		
		suggest = QAction("suggest", self)
		suggest.triggered.connect(self.suggest)
		
		helpmenu.addAction(help)
		
		helpmenu.addAction(about)
		
		helpmenu.addAction(suggest)
		
		
		
		
		
		self.setGeometry(300, 300,250,150)
		self.setWindowTitle("notepad")
		self.show()
		
	def toggleMenu(self, state):
		if state:
			self.statusbar.show()
		else:
			self.statusbar.hide()
			
	def openn(self):
			home_dir = str(Path.home())
			fname = QFileDialog.getOpenFileName(self, "open file", home_dir)
			if fname[0]:
				f = open(fname[0], "r")
			with f:
				data = f.read()
				self.textEditor.setText(data)
				
	def closeEvent(self, event):
		reply = QMessageBox.question(self, "message","do u really want to quit",QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
	def changeFont(self):
		font, ok = QFontDialog.getFont()
		if ok:
			self.textEditor.setFont(font)
	def changeBg(self):
		font, ok = QColorDialog.getColor()
		if ok:
			self.textEditor.setColor(font)
			
	def help(self):
		msg = QMessageBox()
		msg.setWindowTitle("help")
		msg.setText("To start, Download, click start button, search notroad v2,double click and open it up")
		msg.setIcon(QMessageBox.Information)
		msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
		msg.exec()
	def about(self):
		msg = QMessageBox()
		msg.setWindowTitle("About")
		msg.setIcon(QMessageBox.Information)
		msg.setText("Notepad V2 is a word processing program, the latest version of the Spark Notepad app which allows changing of text in a computer file. Notepad V2 was created by the Spark Company, idea gotten from microsoft co-operation in other to teach learners how to build theirs. It is a text editor, a very simple word processor. It has been a part of Microsoft Windows since 1985.")
		msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
		msg.exec()
		
	def suggest(self):
		test, ok = QInputDialog.getText(self,"have any questions or any Suggestions","enter text: ")
		if ok:
			msg = QMessageBox()
			msg.setText("thanks for your feed back")
			msg.exec()

	
		
	def saveFile(self):
	      
          S__File = QFileDialog.getSaveFileName(None,'SaveTextFile','/', "Text Files (*.txt)\nPython file (*.py)\nAll files (*.*)")
          Text = self.textEditor.toPlainText()
          
          if S__File[0]:
          	  
          	  with open(S__File[0], 'w') as file:
          	  	file.write(Text)
 
            
            
def main():
		app = QApplication(sys.argv)
		es = Example()
		sys.exit(app.exec_())
		
if __name__ == "__main__":
		
		main()
		
		
		
		
		
		
