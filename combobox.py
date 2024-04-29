# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import os
import sys

seoul_list = ['강남구','강동구', '강북구' , '강서구' ,'관악구','광진구' , '구로구', '금천구' , '노원구', '도봉구', '동대문구', '동작구', '마포구' , '서대문구' , '서초구', '성동구', '성북구', '송파구' , '양천구' , '영등포구' , '용산구' , '은평구' , '종로구' , '중구' , '중랑구']

gyeongki_list = ['가평군' ,'고양시 덕양구' ,'고양시 일산동구','고양시 일산서구' ,'과천시' ,'광명시' ,'광주시' ,'구리시' ,'군포시' ,'김포시' ,'남양주시' ,'동두천시' ,'부천시' ,'성남시 분당구' ,'성남시 수정구' ,'성남시 중원구' ,'수원시 권선구' ,'수원시 영통구' ,'수원시 장안구', '수원시 팔달구' ,'시흥시' ,'안산시 단원구' ,'안산시 상록구' ,'안성시', '안양시 동안구' ,'안양시 만안구' ,'양주시' ,'양평군' ,'여주시', '연천군' ,'오산시',' 용인시 기흥구' ,'용인시 수지구', '용인시 처인구' ,'의왕시', '의정부시' ,'이천시' ,'파주시' ,'평택시' ,'포천시', '하남시' ,'화성시']


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType(os.path.abspath("untitled.ui"))[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.comboBox.addItem('경기')
        self.comboBox.addItem('서울')
        self.comboBox.addItem('인천')
        # 선택되면 두번째 콤보박스의 내용이 바뀜
        self.comboBox.activated[str].connect(lambda :self.selectedComboItem(self.comboBox))
        
        self.comboBox_2.addItem('이전구역을 먼저 선택해주세요')
 
        self.show()

        

    ### 콤보박스 관련 함수
    def selectedComboItem(self,text):
    
        print(text.currentText())
        if text.currentText() == '서울':
            print("1")

            self.comboBox_2.clear()
            self.comboBox_2.addItems(seoul_list)

        if text.currentText() == '경기':
            print("1")

            self.comboBox_2.clear()
            self.comboBox_2.addItems(gyeongki_list)




if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
    
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
