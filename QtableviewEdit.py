from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QPushButton, QVBoxLayout, QWidget
import sys
 
 
class MyTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
 
    def rowCount(self, parent):
        return len(self._data)
 
    def columnCount(self, parent):
        return len(self._data[0])
 
    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            
            return str(self._data[index.row()][index.column()])
        return None
 
    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            print("이전값:")
            print(self._data[index.row()][index.column()])
            self._data[index.row()][index.column()] = value
            
            self.dataChanged.emit(index, index)
            print("바꾼값")
            print(value)
            print(value=='')
            return True
        return False
 
    def flags(self, index):
        return super().flags(index) | Qt.ItemFlag.ItemIsEditable
 
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.model = MyTableModel(self.data)
 
        self.table_view = QTableView()
        self.table_view.setModel(self.model)
 
        self.edit_button = QPushButton('Edit Data')
        self.edit_button.clicked.connect(self.editData)
 
        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        layout.addWidget(self.edit_button)
 
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
 
    def editData(self):
        # Activate edit mode on the selected cell
        index = self.table_view.currentIndex()
        if index.isValid():
            self.table_view.edit(index)
 
    def closeEvent(self, event):
        # Print the final data when closing the window
        print('Final Data:', self.data)
        event.accept()
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
 
    window = MainWindow()
    window.show()
 
    sys.exit(app.exec())