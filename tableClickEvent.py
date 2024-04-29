import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 800, 300)       

        self.ta1 = QTableWidget(self)
        self.ta1.resize(400, 500)
        self.ta1.setColumnCount(3)
     
        table_column=["첫번째 열" , "두번째 열" , "Third 열"]
        self.ta1.setHorizontalHeaderLabels(table_column)

        self.ta1.cellClicked.connect(self.fun_cellClicked)

        #행 2개 추가
        self.ta1.setRowCount(2)
        
        #추가된 행에 데이터 채워넣음
        self.ta1.setItem(0, 0, QTableWidgetItem("(0,0)"))
        self.ta1.setItem(0, 1, QTableWidgetItem("(0,1)"))
        self.ta1.setItem(1, 0, QTableWidgetItem("(1,0)"))
        self.ta1.setItem(1, 1, QTableWidgetItem("(1,1)"))
        self.ta1.setItem(0, 2, QTableWidgetItem("(0,2)"))
        self.ta1.setItem(1, 2, QTableWidgetItem("(1,2)"))
        

    def fun_cellClicked(self,row,col):
        print("cell clicked row : %d , col : %d"  %(row,col))    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()