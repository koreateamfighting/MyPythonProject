import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('PyQt5 GUI')
        self.resize(400,300)
        self.add_widgets()
    
    def add_widgets(self):
        self.statusBar().showMessage('Text in statusbar')
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        
        new_action = QAction('New',self)
        file_menu.addAction(new_action)
        new_action.setStatusTip('New File')
    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    
    gui.show()
    sys.exit(app.exec_())
        
        
        
        