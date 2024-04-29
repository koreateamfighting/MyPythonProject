import sys 
from PyQt5.QtCore import Qt, QMimeData 
from PyQt5.QtGui import QDrag 
from PyQt5.QtWidgets import *
from openpyxl import load_workbook
import pandas as pd


allData = {}
first_column = []
second_column = []
third_column = []
column_idx_lookup = {'LID': 0, '한국어': 1, '영어': 2}
class DragDropWidget(QWidget): 
    
    
    def __init__(self): 
        super().__init__() 
 
        # Create a label to display the file path
        mainlayout = QVBoxLayout()
        mainlayout.setSpacing(20)     
        mainlayout.addLayout(self.dragAnddropBox())
        #mainlayout.addLayout(self.textfield())                
        self.setLayout(mainlayout)
        # Set the widget to accept drops 
        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(290, 290)
        self.tableWidget.setRowCount(len(allData.values()))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        mainlayout.addWidget(self.tableWidget)

        self.setTableWidgetData()
        
    def dragAnddropBox(self):
        self.label = QLabel(self) 
        self.label.setText("Drop a file here") 
        self.label.resize(1000,200)
        sub1layout = QVBoxLayout()
        sub1layout.addWidget(self.label)
        self.setAcceptDrops(True) 
               
        return sub1layout
    def setTableWidgetData(self):
        column_headers = ['LID', '한국어', '영어']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        for k, v in allData.items():
            col = column_idx_lookup[k]
            for row, val in enumerate(v):
                item = QTableWidgetItem(val)
                if col == 2:
                    item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)

                self.tableWidget.setItem(row, col, item)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
    
    # def textfield(self):
    #     global textEdit1
    #     sub2layout = QVBoxLayout()
    #     sub2layout.addWidget(textEdit1)
        
    #     return sub2layout
 
    def dragEnterEvent(self, event): 
        # Check if the dragged data is a file 
        if event.mimeData().hasUrls(): 
            # Accept the drop if the file is a valid type 
            event.accept() 
        else: 
            # Reject the drop if the file is not a valid type 
            event.ignore() 
 
    def dropEvent(self, event): 
        # Get the file path from the dropped data         
        
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            print(f)
 
        # Update the label to display the file path 
        self.label.setText(f)
        self.readExcel(f)
        
    
    def readExcel(self,f):
        # wb = load_workbook(filename= f,read_only = True)
        # ws = wb['1. Prompt']
        # whole_list = []
        
        # for row in ws.rows:
        #     for cell in row:        
        #         whole_list.append(cell.value)     
        
        
        # for list in whole_list:
        #     textEdit1.append(f'{list}\n')
        # wb.close()
        dataset = pd.read_excel(io = f,sheet_name='1. Prompt',skiprows = 2, usecols='C,K,L',names=['LID','영어','한국어'])
        # print(dataset['한국어'])
        
        for i in dataset['한국어']:
             # textEdit1.append(f'{i}\n') 
             first_column.append(f'{i}\n')               
             
        for j in dataset['영어'] :
            # textEdit1.append(f'{j}\n')
            second_column.append(f'{j}\n')               
            
        for k in dataset['LID']:
            # textEdit1.append(f'{k}\n')
            third_column.append(f'{k}\n')        
            
            
        allData['LID'] = third_column
        allData['한국어'] = first_column
        allData['영어'] = second_column
    
    
    # print(allData)       
            
        
            
                 
           

 
if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    #textEdit1 = QTextEdit()
    tableWidget = QTableWidget()
    widget = DragDropWidget() 
    widget.show() 
    sys.exit(app.exec_())
    