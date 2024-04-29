
# Lets make the main window class
# Subscribe to PyShine Youtube channel for more detail! 
# WEBSITE: www.pyshine.com
from result2 import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtWidgets
import platform

op_sys = platform.system()



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		"""
		This function initializes our main window from the main.py, set its title 
		and also allow the drops on it.
		"""
		super().__init__()
		self.setupUi(self)
		self.setWindowTitle('PyShine drag drop plot')
		self.setAcceptDrops(True)
	def dragEnterEvent(self, e):
		"""
		This function will detect the drag enter event from the mouse on the main window
		"""
		if e.mimeData().hasUrls:
			e.accept()
		else:
			e.ignore()
	def dragMoveEvent(self,e):
		"""
		This function will detect the drag move event on the main window
		"""
		if e.mimeData().hasUrls:
			e.accept()
		else:
			e.ignore()
	def dropEvent(self,e):
		"""
		This function will enable the drop file directly on to the 
		main window. The file location will be stored in the self.filename
		"""
		if e.mimeData().hasUrls:
			e.setDropAction(QtCore.Qt.CopyAction)
			e.accept()
			for url in e.mimeData().urls():
				#if op_sys == 'Darwin':
				#	fname = str(NSURL.URLWithString_(str(url.toString())).filePathURL().path())
				#else:
				#	fname = str(url.toLocalFile())
				fname = str(url.toLocalFile())
			self.filename = fname
			print("GOT ADDRESS:",self.filename)
			self.readData()
		else:
			e.ignore() # just like above functions	
# Subscribe to PyShine Youtube channel for more detail! 
# WEBSITE: www.pyshine.com		
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
	
