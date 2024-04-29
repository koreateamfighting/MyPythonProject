import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Button Color Changer")
        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton("Change Color", self)
        self.button.setGeometry(100, 50, 100, 30)
        self.button.setStyleSheet("background-color: red")  # 초기 배경색 설정

        self.button.clicked.connect(self.change_color)

    def change_color(self):
        current_color = self.button.palette().button().color().name()
        new_color = "blue" if current_color == "red" else "red"
        self.button.setStyleSheet(f"background-color: {new_color}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())