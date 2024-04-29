from PyQt5.QtWidgets import QTableWidget, QLineEdit, QPushButton, QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidgetItem,QAction,qApp
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

import random, string, sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)


        self.query = QLineEdit()
        self.query.setPlaceholderText("Search...")
        self.query.textChanged.connect(self.search)

        n_rows = 50
        n_cols = 4

        self.table = QTableWidget()
        self.table.setRowCount(n_rows)
        self.table.setColumnCount(n_cols)

        for c in range(0, n_cols):
            for r in range(0, n_rows):
                s = ''.join(random.choice(string.ascii_lowercase) for n in range(10))
                i = QTableWidgetItem(s)
                self.table.setItem(c, r, i)

        layout = QVBoxLayout()

        layout.addWidget(self.query)
        layout.addWidget(self.table)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)
       

    def search(self, s):
        # Clear current selection.
        self.table.setCurrentItem(None)
        print("뭐니2")
        print(s)

        if not s:
            # Empty string, don't search.
            return

        matching_items = self.table.findItems(s, Qt.MatchContains)
        if matching_items:
            # We have found something.
            item = matching_items[0]  # Take the first.
            self.table.setCurrentItem(item)


app = QApplication(sys.argv)
w = MainWindow()
w.show()

app.exec_()