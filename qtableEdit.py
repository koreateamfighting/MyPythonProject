#-*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, \
    QTableWidgetItem, QAbstractItemView, QTextEdit, QPushButton
from PyQt5.Qt import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 윈도우 설정
        self.setGeometry(200, 100, 400, 400)  # x, y, w, h
        self.setWindowTitle('QTableWidget Sample Window')

        # QTableWidget
        self.tablewidget = QTableWidget(self)
        self.tablewidget.resize(400, 200)
        self.tablewidget.setRowCount(3) # 행 개수
        self.tablewidget.setColumnCount(3) # 열 개수
        self.tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.edit = QTextEdit(self)
        self.edit.move(10, 210)

        self.btn = QPushButton(self)
        self.btn.setText('0, 0 셀 입력')
        self.btn.move(120, 210)

        # QTableWidget 에 데이터 추가하기
        self.insert_data()

        # 수정 가능한 필드
        self.tablewidget.setEditTriggers(QAbstractItemView.AllEditTriggers)

        # 데이터 조회
        rowcount = self.tablewidget.rowCount()
        colcount = self.tablewidget.columnCount()

        for i in range(0, rowcount):
            for j in range(0, colcount):
                data = self.tablewidget.item(i, j)
                if data is not None:
                    print(data.text())
                else:
                    print('blank')

        # self.tablewidget.item(0, 0).setText('1111')

        # 테이블 이벤트 지정
        self.tablewidget.cellChanged.connect(self.cellchanged_event)
        self.tablewidget.currentCellChanged.connect(self.currentcellchanged_event)
        self.tablewidget.cellClicked.connect(self.cellclicked_event)
        self.tablewidget.cellDoubleClicked.connect(self.celldoubleclicked_event)

    # 셀 더블클릭 때 발생하는 이벤트
    def celldoubleclicked_event(self, row, col):
        data = self.tablewidget.item(row, col)
        print("셀 더블클릭 셀 값 : ", data.text())

    # 셀 선택할 때 발생하는 이벤트
    def cellclicked_event(self, row, col):
        data = self.tablewidget.item(row, col)
        print("셀 클릭 셀 값 : ", data.text())

    # 선택한 셀이 바뀌면 발생하는 이벤트
    def currentcellchanged_event(self, row, col, pre_row, pre_col):
        current_data = self.tablewidget.item(row, col) # 현재 선택 셀 값
        pre_data = self.tablewidget.item(pre_row, pre_col) # 이전 선택 셀 값
        if pre_data is not None:
            print("이전 선택 셀 값 : ", pre_data.text())
        else:
            print("이전 선택 셀 값 : 없음")

        print("현재 선택 셀 값 : ", current_data.text())

    # 셀의 내용이 바뀌었을 때 이벤트
    def cellchanged_event(self, row, col):
        data = self.tablewidget.item(row, col)
        print("cellchanged_event 발생 : ", data.text())

    def insert_data(self):
        self.tablewidget.setItem(0, 0, QTableWidgetItem("1행 1열"))
        self.tablewidget.setItem(0, 1, QTableWidgetItem("1행 2열"))
        self.tablewidget.setItem(1, 0, QTableWidgetItem("2행 1열"))
        self.tablewidget.setItem(1, 1, QTableWidgetItem("2행 2열"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
