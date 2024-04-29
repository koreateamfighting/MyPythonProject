from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,QPushButton,QHeaderView
from PyQt5.QtCore import Qt
import sys
import pandas as pd

class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.setWindowTitle("Load Excel data to QTableWidget")
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.table = QTableWidget()
        layout.addWidget(self.table)
        
        self.button = QPushButton('&Load Data')
        self.button.clicked.connect(lambda _, xl_path= excel_file_path, sheet_name = worksheet_name: self.loadExcelData(xl_path,sheet_name))
        layout.addWidget(self.button)
        
        
    def loadExcelData(self, excel_file_dir, worksheet_name):
        df = pd.read_excel(excel_file_dir, worksheet_name)
        if df.size == 0:
                return
            
            
        df.fillna('', inplace=True)
        self.table.setRowCount(df.shape[0])
        self.table.setColumnCount(df.shape[1])
        self.table.setHorizontalHeaderLabels(df.columns)
        
        
        
        
        for row in df.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                if isinstance(value, (float,int)):
                    value = '{0:0,.0f}'.format(value)
                tableItem = QTableWidgetItem(str(value))
                self.table.setItem(row[0],col_index, tableItem)
                
        self.table.setColumnWidth(2,300)
        
        
        
        
        
    
    
if __name__ == '__main__':
    
    excel_file_path = 'C:/Users/MEDIAZEN/Desktop/data.xlsx'
    worksheet_name = 'country'
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 17px;
        }
        ''')
    window = Main()
    window.showMaximized()
    app.exec_()