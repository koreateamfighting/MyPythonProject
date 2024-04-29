import sys 
from PyQt5.QtCore import Qt, QMimeData 
from PyQt5.QtGui import QDrag 
from PyQt5.QtWidgets import *
from openpyxl import load_workbook
import pandas as pd


class DragDropWidget(QWidget): 
    
    
    def __init__(self): 
        super().__init__() 
 
        # Create a label to display the file path       
             
                       
        mainlayout = QVBoxLayout()
        mainlayout.setSpacing(20)     
        
                
        mainlayout.addLayout(self.dragAnddropBox())
        mainlayout.addLayout(self.textfield())
               
                
        self.setLayout(mainlayout)
        
        # Set the widget to accept drops 
        
    def dragAnddropBox(self):
        self.label = QLabel(self) 
        self.label.setText("Drop a file here") 
        self.label.resize(1000,200)
        sub1layout = QVBoxLayout()
        sub1layout.addWidget(self.label)
        self.setAcceptDrops(True) 
        
        
        return sub1layout
    
    def textfield(self):
        global textEdit1
        sub2layout = QVBoxLayout()
        sub2layout.addWidget(textEdit1)
        
        return sub2layout
 
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
        dataset = pd.read_excel(io = f,sheet_name='1. Prompt',skiprows = 2, usecols='K,L',names=['영어','한국어'])
        # print(dataset['한국어'])
        
        for i in dataset['한국어']:
             textEdit1.append(f'{i}\n')
            
        


        
        
        
 
if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    textEdit1 = QTextEdit()
    widget = DragDropWidget() 
    widget.show() 
    sys.exit(app.exec_())
    