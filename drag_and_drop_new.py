import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, QMimeDatabase

#파일 끌어오는 부분
class FileLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setText('파일을 끌어오세요')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa;
                font-size: 15pt;
                font-family:'Malgun Gothic';
            }
        ''')

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.setAcceptDrops(True)

        layout = QVBoxLayout()

        self.filebox = FileLabel()
        layout.addWidget(self.filebox)

        self.setLayout(layout)
        self.setWindowTitle('파일 drap/drop')

    #파일 끌어오기
    def dragEnterEvent(self, event):
        if self.find_pdf(event.mimeData()):
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if self.find_pdf(event.mimeData()):
            event.accept()
        else:
            event.ignore()

    #파일 놓기
    def dropEvent(self, event):
        urls = self.find_pdf(event.mimeData())
        if urls:
            for url in urls:
                print(url.toLocalFile())
            event.accept()
        else:
            event.ignore()

    def find_pdf(self, mimedata):
        urls = list()
        db = QMimeDatabase()
        for url in mimedata.urls():
            mimetype = db.mimeTypeForUrl(url)
            if mimetype.name() == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                urls.append(url)
        return urls

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyApp()
    myWindow.show()
    app.exec_()