# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 13:05:23 2020
@author: DEEP.I Inc.
"""
import sys

from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from PyQt5 import uic

FROM_CLASS_MainWindow = uic.loadUiType("mainwindow.ui")[0]
FROM_CLASS_Loading = uic.loadUiType("load.ui")[0]

class MainWindow(QMainWindow,FROM_CLASS_MainWindow):    

    def __init__(self):
        super().__init__() 
        self.setupUi(self) 
        self.show()
        
        # 버튼 클릭 매서드
        self.button.clicked.connect(self.loading)
        
    def loading(self):
        # 로딩중일때 다시 클릭하는 경우
        try: 
            self.loading
            self.loading.deleteLater()
            
        # 처음 클릭하는 경우    
        except:
            self.loading = loading(self)
        

#%% Loading Img
class loading(QWidget,FROM_CLASS_Loading):
    
    def __init__(self,parent):
        super(loading,self).__init__(parent)    
        self.setupUi(self) 
        self.center()
        self.show()
        
        # 동적 이미지 추가
        self.movie = QMovie('loading.gif', QByteArray(), self)
        self.movie.setCacheMode(QMovie.CacheAll)
        # QLabel에 동적 이미지 삽입
        self.label.setMovie(self.movie)
        self.movie.start()
        # 윈도우 해더 숨기기
        self.setWindowFlags(Qt.FramelessWindowHint)
    
    # 위젯 정중앙 위치
    def center(self):
        size=self.size()
        ph = self.parent().geometry().height()
        pw = self.parent().geometry().width()
        self.move(int(pw/2 - size.width()/2), int(ph/2 - size.height()/2))

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ShowApp = MainWindow()
    sys.exit(app.exec_())   


    