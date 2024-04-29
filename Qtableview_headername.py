import sys
import requests

import PyQt5
from PyQt5.QtWidgets import QTableView, QWidget, QApplication, QGridLayout, QHeaderView
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QColor, QIcon, QPixmap

from datetime import datetime


class MagicIcon():
    def __init__(self, link):
        self.link = link
        self.icon = QIcon()
        try:
            response = requests.get(self.link)
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            self.icon = QIcon(pixmap)
        except:
            pass


class TableModel(QAbstractTableModel):

    def headerData(self, section: int, orientation: PyQt5.QtCore.Qt.Orientation, role: int = ...):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            # return f"Column {section + 1}"
            return self.columns[section]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return f"{section + 1}"

    def __init__(self, _data):
        self.columns = ["Account", "Investment", "KYC", "Investment Date"]
        # super().__init__(self)
        super(TableModel, self).__init__()
        self._data = _data
        self.calendarLink = "https://img.icons8.com/fluency/48/000000/windows-calendar.png"
        self.dollarLink = "https://img.icons8.com/external-vitaliy-gorbachev-lineal-color-vitaly-gorbachev/40/000000/external-dollar-currency-vitaliy-gorbachev-lineal-color-vitaly-gorbachev-1.png"
        self.analysis = "https://img.icons8.com/external-flatarticons-blue-flatarticons/65/000000/external-analysis-digital-marketing-flatarticons-blue-flatarticons-1.png"
        self.bug = "https://img.icons8.com/offices/30/000000/bug.png"
        self.account = "https://img.icons8.com/plumpy/24/000000/edit-administrator.png"
        self.approvedLink = "https://img.icons8.com/external-bearicons-flat-bearicons/40/000000/external-approved-approved-and-rejected-bearicons-flat-bearicons-9.png"
        self.rejectedLink = "https://img.icons8.com/external-bearicons-flat-bearicons/40/000000/external-rejected-approved-and-rejected-bearicons-flat-bearicons-11.png"
        self.naLink = "https://img.icons8.com/color/48/000000/not-applicable.png"

        self.calendarIcon = MagicIcon(self.calendarLink).icon
        self.accountIcon = MagicIcon(self.account).icon
        self.dollarIcon = MagicIcon(self.dollarLink).icon
        self.approvedIcon = MagicIcon(self.approvedLink).icon
        self.rejectedIcon = MagicIcon(self.rejectedLink).icon
        self.naIcon = MagicIcon(self.naLink).icon

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, datetime):
                return value.strftime("%Y-%m-%d")
            if isinstance(value, float):
                return f"{value:.2f}"
            return value
        if role == Qt.TextAlignmentRole:
            return Qt.AlignHCenter + Qt.AlignVCenter

        if role == Qt.BackgroundRole:
            return QColor("#adcdff") if index.row() % 2 == 0 else QColor("#d8ffc2")

        if role == Qt.DecorationRole:
            value = self._data[index.row()][index.column()]
            
            if value is None:
                return self.naIcon
            if isinstance(value, datetime):
                return self.calendarIcon
            if index.column() == 0:
                return self.accountIcon
            if index.column() == 1:
                return self.dollarIcon
            if index.column() == 2:
                if value == True:
                    return self.approvedIcon
                elif value == False:
                    return self.rejectedIcon
                return self.naIcon

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class MainWindow(QWidget):
    def __init__(self):
        # super().__init__()
        super(MainWindow, self).__init__()
        self.resizeEvent = self.onResize
        self.table = QTableView()
        
        self.setWindowIcon(MagicIcon(
            "https://img.icons8.com/external-flatarticons-blue-flatarticons/65/000000/external-analysis-digital-marketing-flatarticons-blue-flatarticons-1.png"
        ).icon)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.table.setSizeAdjustPolicy(QHeaderView.AdjustIgnored)
        # self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        data = [
            ["Andrew Mike", 15.255, True, datetime(2022, 1, 5)],
            ["Eliza Petterson", 353.555, False, datetime(2020, 1, 5)],
            ["Joseph Samuel", 123, None, datetime(2020, 1, 15)],
            ["Nita Singh", 266, True, datetime(2022, 2, 7)],
            ["Rahul Chakrabarti", 102, True, datetime(2019, 10, 15)],
        ]
        self.model = TableModel(data)
        self.table.setModel(self.model)
        self.header = self.table.horizontalHeader()
        # self.header.setSectionResizeMode(0, QHeaderView.Stretch)
        # self.header.setSectionResizeMode(1, QHeaderView.)
        # self.header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.layout = QGridLayout()
        self.layout.addWidget(self.table, 0, 0)
        self.setLayout(self.layout)

    def onResize(self, event):
        # print('old', event.oldSize(), 'new', event.size())
        # super(MainWindow, self).resizeEvent(event)
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wid = MainWindow()
    wid.show()
    sys.exit(app.exec())