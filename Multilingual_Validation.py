from PyQt5 import QtCore, QtGui, QtWidgets
from tqdm import tqdm
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from difflib import get_close_matches
from threading import Thread
import threading
import time
import sys, os
import pandas as pd

links = [] # 파일 담는 리스트 전역 변수 (단일만 받게 link[0]만 쓰임)
df = [] # 엑셀 to 데이터 프레임으로 구성 , 
df2 = []
length_df = 0 # 데이터 프레임 길이 
data_list = [] #데이터 프레임을 테이블뷰에 배치하기 위해 리스트 형식으로 변환한 리스트 전역 변수
data_list2 = []
minor_data_list = []
columns = [] #열 제목을 담은 리스트 전역 변수
columns2 = [] #열 제목을 담은 리스트 전역 변수
minor_columns = []
select_row = 0 #선택된 셀의 행 번호
filepath = ''
target = ''
languages = []
진행률 = 0


class ListBoxWidget(QListWidget): # 2개의 리스트 컨트롤러
    

    
    def __init__(self, parent=None):
        super().__init__(parent)        
        
        self.setAcceptDrops(True)
        self.resize(1280, 260)

    def dragEnterEvent(self, event):# 파일을 드래그 가능 영역으로 들어오는 순간을 제어하는 메소드
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):# 파일을 드래그 가능 영역안에서 움직이는 순간을 제어하는 메소드
        
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event): #파일 드랍 하눈 순간을 대한 제어하는 메소드
        global table1,filepath,target
                
        if event.mimeData().hasUrls():
            
            event.setDropAction(Qt.CopyAction)
            event.accept()         
           
            for url in event.mimeData().urls():
                
                if url.isLocalFile():
                    # links.append(str(url.toLocalFile()))
                    # print(links)
                    filepath = str(url.toLocalFile())
                    
                else:
                    # links.append(str(url.toString()))
                    filepath = str(url.toString())
            # self.addItems(links)
            
            target = self.fileVerify(filepath)
            
            #print(target)
            
        
            if target == 'Multilanguage':
                excel_file_dir =filepath                
                worksheet_name = 'Sheet0'
                      
                            
                start = time.time()
                readexcel1.loadExcelData(excel_file_dir,worksheet_name)
            
                end = time.time()
                print(f"{end - start:.5f}초에 Read Finished.")
                table1.show()
                midwidget.replaceWidget(lidTableView_groupbox,table1)
                lidTableView_groupbox.hide()
                
                
            elif target == 'Master_DB':
                
                time.sleep(2)
                excel_file_dir = filepath
                worksheet_name = 'Sheet1'
                start = time.time()
                task = Thread(target=readexcel2.loadExcelData(excel_file_dir,worksheet_name))
                task.run()
                
                # readexcel2.loadExcelData(excel_file_dir,worksheet_name)            
                
                
                end = time.time()
                print(f"{end - start:.5f}초에 Read Finished.")
                table2.show()
                leftinbottomlayout.replaceWidget(masterDB_groupbox,table2)
                masterDB_groupbox.hide()
            else:
                Ui_MainWindow.fileErrorAlert()
                event.ignore()
                
            
        else:
            event.ignore()
            
    def fileVerify(self,filepath):
        
        if (filepath.__contains__('Multilanguage')):
                target = 'Multilanguage'
        elif(filepath.__contains__('Master_DB')):
                target = 'Master_DB'
        else:
                target = 'Null'
        return target
    
    def setTableView1(self):
        
        global df
        
        global data_list 
        global minor_data_list
        global minor_columns
        global columns
        
          
        table1.hideColumn(0) 
        table1.setColumnWidth(2,300)
        print("데이터 생성 완료")
        filter_df = df.filter(items=columns)
        filter_minor_df = df.filter(items=minor_columns)
        data_list = filter_df.values.tolist()
        minor_data_list = filter_minor_df.values.tolist()
        #print(minor_data_list)
        
        hheader = table1.horizontalHeader()
        #hheader.sectionClicked.connect(readexcel1._horizontal_header_clicked) 
        hheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)       
        table1.setRowCount(len(data_list))
        table1.setColumnCount(5)        
        table1.setHorizontalHeaderLabels(columns)        
        table1.setColumnWidth(0,int(table1.width() * 0.15))        
        table1.setColumnWidth(1,int(table1.width() * 0.10))
        table1.setColumnWidth(2,int(table1.width() * 0.25))
        table1.setColumnWidth(3,int(table1.width() * 0.25))
        table1.setColumnWidth(4,int(table1.width() * 0.25))
             
        print(f'테이블의 길이 :{table1.width()}')
        print(f'테이블의 높이 :{table1.height()}')
        
        #print(df.filter(items=['Korean','Proposal EN-US']))
       
                      
        for row in tqdm(filter_df.iterrows(),mininterval=0.001,ncols=100,leave=True,total=length_df):
            
            values = row[1]
            
            진행률 = int(int(row[0])/length_df * 100)             
            statusbar.setValue(진행률)
            
            for col_index, value in enumerate(values):
                # if isinstance(value, (float,int)):
                #     value = '{0:0,.0f}'.format(value)
                #print(col_index , value)
                tableItem = QTableWidgetItem(str(value))
                table1.setItem(row[0],col_index, tableItem)
        table1.horizontalHeader().setStretchLastSection(True)
        # table1.horizontalHeader().setSectionResizeMode(
        # QHeaderView.Stretch)
        table1.cellClicked.connect(readexcel1._cellclicked)
       
        ref_textedt.textChanged.connect(readexcel1.filter)
        
        time.sleep(1)
        
        statusbar.hide()
        
    
        
        
    def setTableView2(self):
        global df2,data_list2,진행률
           
        
        table2.setColumnWidth(2,300)
        print("데이터 생성 완료")
        
        data_list2 = df2.values.tolist()
        table2.setRowCount(len(data_list2))      
        #table2.setColumnCount(len(columns2))
        table2.setColumnCount(5)
        table2.setHorizontalHeaderLabels(columns2)
        table2.setColumnWidth(0,int(table2.width() * 0.15))        
        table2.setColumnWidth(1,int(table2.width() * 0.10))
        table2.setColumnWidth(2,int(table2.width() * 0.25))
        table2.setColumnWidth(3,int(table2.width() * 0.25))
        table2.setColumnWidth(4,int(table2.width() * 0.25))       
        statusbar.show()
        
        
                 
        for row in tqdm(df2.iterrows(),mininterval=0.001,ncols=100,leave=True,total=length_df):
            
            values = row[1]
            
            진행률 = int(int(row[0])/length_df * 100)             
            statusbar.setValue(진행률)
            for col_index, value in enumerate(values):
                if isinstance(value, (float,int)):
                   value = '{0:0,.0f}'.format(value)
                tableItem = QTableWidgetItem(str(value))
                table2.setItem(row[0],col_index, tableItem)
                
        table2.horizontalHeader().setStretchLastSection(True)
        table2.horizontalHeader().setSectionResizeMode(
        QHeaderView.Stretch)
        # table2.cellClicked.connect(self._cellclicked)
        # hheader = table1.horizontalHeader()
        # hheader.sectionClicked.connect(self._horizontal_header_clicked)
        # ref_textedt.textChanged.connect(self.filter)
        
        time.sleep(1)
        
        
        statusbar.hide()
        
    
        
    
         
            
    def selectedComboItem(self,text):
        global columns,table1,hheader,minor_data_list,filter_df,filter_minor_df,data_list        
        
        if text.currentText() == languages[0]:
            
            columns.pop()
            columns.append(languages[0])            
            table1.setColumnWidth(2,300)
            print("데이터 생성 완료")
            filter_df = df.filter(items=columns)
            filter_minor_df = df.filter(items=minor_columns)
            data_list = filter_df.values.tolist()
            minor_data_list = filter_minor_df.values.tolist()
            
        
            hheader = table1.horizontalHeader()
            hheader.sectionClicked.connect(readexcel1._horizontal_header_clicked) 
            hheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)       
            table1.setRowCount(len(data_list))
            table1.setColumnCount(5)        
            table1.setHorizontalHeaderLabels(columns)        
            table1.setColumnWidth(0,int(table1.width() * 0.15))        
            table1.setColumnWidth(1,int(table1.width() * 0.10))
            table1.setColumnWidth(2,int(table1.width() * 0.25))
            table1.setColumnWidth(3,int(table1.width() * 0.25))
            table1.setColumnWidth(4,int(table1.width() * 0.25))

            
        elif text.currentText() == languages[1]:
            print(columns)
            columns.pop()
            columns.append(languages[1])
            
            table1.setColumnWidth(2,300)
            
            print("데이터 생성 완료")
            
            filter_df = df.filter(items=columns)
            
            filter_minor_df = df.filter(items=minor_columns)
            data_list = filter_df.values.tolist()
            minor_data_list = filter_minor_df.values.tolist()
            
        
            hheader = table1.horizontalHeader()
            hheader.sectionClicked.connect(readexcel1._horizontal_header_clicked) 
            hheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)       
            table1.setRowCount(len(data_list))
            table1.setColumnCount(5)        
            table1.setHorizontalHeaderLabels(columns)        
            table1.setColumnWidth(0,int(table1.width() * 0.15))        
            table1.setColumnWidth(1,int(table1.width() * 0.10))
            table1.setColumnWidth(2,int(table1.width() * 0.25))
            table1.setColumnWidth(3,int(table1.width() * 0.25))
            table1.setColumnWidth(4,int(table1.width() * 0.25))

          
        elif text.currentText() == languages[2]:
      
            columns.pop()
            columns.append(languages[2])
            
            table1.setColumnWidth(2,300)
            
            print("데이터 생성 완료")
            filter_df = df.filter(items=columns)
            
            filter_minor_df = df.filter(items=minor_columns)
            data_list = filter_df.values.tolist()
            minor_data_list = filter_minor_df.values.tolist()
            
        
            hheader = table1.horizontalHeader()
            hheader.sectionClicked.connect(readexcel1._horizontal_header_clicked) 
            hheader.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)       
            table1.setRowCount(len(data_list))
            table1.setColumnCount(5)        
            table1.setHorizontalHeaderLabels(columns)        
            table1.setColumnWidth(0,int(table1.width() * 0.15))        
            table1.setColumnWidth(1,int(table1.width() * 0.10))
            table1.setColumnWidth(2,int(table1.width() * 0.25))
            table1.setColumnWidth(3,int(table1.width() * 0.25))
            table1.setColumnWidth(4,int(table1.width() * 0.25))
        
        
        for row in tqdm(filter_df.iterrows(),mininterval=0.001,ncols=100,leave=True,total=length_df):
            
            values = row[1]
            
            진행률 = int(int(row[0])/length_df * 100)             
            statusbar.setValue(진행률)
            
            for col_index, value in enumerate(values):
                # if isinstance(value, (float,int)):
                #     value = '{0:0,.0f}'.format(value)
                #print(col_index , value)
                tableItem = QTableWidgetItem(str(value))
                table1.setItem(row[0],col_index, tableItem)
        table1.horizontalHeader().setStretchLastSection(True)   


class MultiLanguageReadExcel(): # Read Excel Model(1)
    
   
    def loadExcelData(self, excel_file_dir, worksheet_name): # (핵심) 엑셀 데이터 가공 하는 제어 메소드
        global table1,length_df,df,columns,data_list,minor_data_list,minor_columns,languages   
        
        statusbar.show()
        
        # 이 부분에서 제대로 된 엑셀 파일인지  검증###############################
                
        for i in tqdm(range(0,1), ncols = 100, desc ="Loading data.."):            
            df= pd.read_excel(excel_file_dir,worksheet_name,usecols='B,E,AA,AF,AG,AJ,AV,R,S,U')
            #df= pd.read_excel(excel_file_dir,worksheet_name)
        
        print("------xlsx Reading is completed ------")  
        
        length_df = len(df)
        print(f'데이터 행 길이는 {len(df)}입니다.')
        
        #columns = df.columns.tolist()
        
        languages = ['Spanish (Mexico)','French (Canada)','German.1']
        columns = ['Standard LID','Component','Korean','Proposal EN-US','Spanish (Mexico)']
        minor_columns = ['String Type','Manual Line breaks','Max Lines']      
        
              
        # print(columns)
        
        
        for language in languages:
            combobox.addItem(language)
        
        
        
        if df.size == 0:
                return 
        
        listbox_view1.setTableView1()         
    
    def _horizontal_header_clicked(self, idx):
        """
        컬럼 헤더 click 시에만, 정렬하고, 다시 정렬기능 off 시킴
        -- 정렬기능 on 시켜놓으면, 값 바뀌면 바로 자동으로 data 순서 정렬되어 바뀌어 헷갈린다..
        :param idx -->  horizontalheader index; 0, 1, 2,...
        :return:
        """
        # print("hedder2.. ", idx)
        table1.setSortingEnabled(True)  # 정렬기능 on
        # time.sleep(0.2)
        table1.setSortingEnabled(False)  # 정렬기능 off
    
    def _cellclicked(self, row, col):
        global select_row           
        #print(f"_cellclicked : {data_list[int(row)][int(col)]} ") # 실행하지 않는게 좋음
        select_row = row
        draft_txtedt.setText(str(data_list[select_row][3]))
        val_txtedt.setText(str(data_list[select_row][4]))
        strtype_label.setText(f"String type : {str(minor_data_list[select_row][0])}")
        linebreaks_label.setText(f"Manulal line breaks : {str(minor_data_list[select_row][1])}")
        maxlines_label.setText(f"Max lines : {str(minor_data_list[select_row][2])}")
        uidinfo_txtedt.setText(str(data_list[select_row][0]))
        componentinfo_txtedt.setText(str(data_list[select_row][1]))
    
    def fun_reset(self): # 초기화 메뉴 함수
        global links, df ,df2, excel_file_dir,filepath
                      
        print("초기화 버튼을 눌렀습니다.")
        excel_file_dir = ''
        # links = []
        filepath = ''
        df = []
        df2 = [] 
        
        
        table1.hide()
        table2.hide()
        midwidget.replaceWidget(table1,lidTableView_groupbox)
        leftinbottomlayout.replaceWidget(table2,masterDB_groupbox)
        
        listbox_view1.clear()
        listbox_view2.clear()
        lidTableView_groupbox.show()
        masterDB_groupbox.show()
        
    
    def filter(self, filter_text):
        
        for i in range(table1.rowCount()):
            for j in range(table1.columnCount()):
                
                item = table1.item(i, j)                
                match = filter_text.lower() not in item.text().lower()
                
                
                table1.setRowHidden(i, match)
                if not match:
                    break
        
        readexcel2.filter(filter_text)
                
class MasterDBReadExcel(): # Read Excel Model(2)        
    
    
    def startThread():
        thread = threading.Thread()
        thread.daemon = True
        thread.start()
                                      
    def loadExcelData(self, excel_file_dir, worksheet_name): # (핵심) 엑셀 데이터 가공 하는 제어 메소드
        
        global table2,length_df,df2,columns2,data_list2
       
              
                
        for i in tqdm(range(0,1), ncols = 100, desc ="Loading data.."):            
            df2= pd.read_excel(excel_file_dir,worksheet_name,usecols='B,D,E,F,G,H,N')
        
        print("------xlsx Reading is completed ------")  
        #print(df.to_dict(orient='dict'))
        length_df = len(df2)
        print(f'데이터 행 길이는 {len(df2)}입니다.')
        # print(columns)
        
        # for language in languages:
        #     combobox.addItem(language)
        
        #time.sleep(1)
        statusbar.show()  
        columns2 = df2.columns.tolist()
        print(columns2)
        
        
        if df2.size == 0:
                return       
            
        listbox_view2.setTableView2()   
            
    def filter(self, filter_text):
        
        for i in range(table2.rowCount()):
            for j in range(table2.columnCount()):
                
                item = table2.item(i, j)
                
                
                match = filter_text.lower() not in item.text().lower()
                
                table2.setRowHidden(i, match)
                if not match:
                    break
                

class Ui_MainWindow(QMainWindow): # Main View
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(QSize(1255, 676))
        
        global readexcel1,readexcel2,statusbar,centralwidget,listbox_view1,listbox_view2,\
            midwidget,leftinbottomlayout,lidTableView_groupbox,second_groupbox,third_groupbox,\
            fourth_groupbox,ref_textedt,draft_txtedt,val_txtedt,masterDB_groupbox,strtype_label,linebreaks_label,\
            maxlines_label,uidinfo_txtedt,componentinfo_txtedt,combobox
        
        centralwidget = QtWidgets.QWidget(MainWindow)
        centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mainlayout = QtWidgets.QVBoxLayout()
        self.mainlayout.setObjectName("mainlayout")
        self.topwidget = QtWidgets.QHBoxLayout()
        self.topwidget.setObjectName("topwidget")
        self.first_groupbox = QtWidgets.QGroupBox(centralwidget)
        self.first_groupbox.setTitle("")
        self.first_groupbox.setObjectName("first_groupbox")        
        self.selectlanguage_label = QtWidgets.QLabel(self.first_groupbox)
        self.selectlanguage_label.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.selectlanguage_label.setObjectName("selectlanguage_label")
        combobox = QtWidgets.QComboBox(self.first_groupbox)
        combobox.setGeometry(QtCore.QRect(10, 30, 201, 22))
        combobox.setObjectName("combobox")
        combobox.activated[str].connect(lambda : listbox_view1.selectedComboItem(combobox))
        uidinfo_txtedt = QtWidgets.QLineEdit(self.first_groupbox)
        uidinfo_txtedt.setGeometry(QtCore.QRect(10, 70, 91, 20))
        uidinfo_txtedt.setObjectName("uidinfo_txtedt")
        componentinfo_txtedt = QtWidgets.QLineEdit(self.first_groupbox)
        componentinfo_txtedt.setGeometry(QtCore.QRect(120, 70, 91, 20))
        componentinfo_txtedt.setObjectName("componentinfo_txtedt")
        self.scenario_view_btn = QtWidgets.QPushButton(self.first_groupbox)
        self.scenario_view_btn.setGeometry(QtCore.QRect(10, 110, 201, 41))
        self.scenario_view_btn.setObjectName("scenario_view_btn")
        self.topwidget.addWidget(self.first_groupbox)
        second_groupbox = QtWidgets.QGroupBox(centralwidget)
        second_groupbox.setObjectName("second_groupbox")
        ref_textedt = QtWidgets.QLineEdit(second_groupbox)
        ref_textedt.setGeometry(QtCore.QRect(10, 20, 201, 141))
        ref_textedt.setObjectName("ref_textedt")
        ref_textedt.setPlaceholderText("Search...")                
        self.topwidget.addWidget(second_groupbox)
        third_groupbox = QtWidgets.QGroupBox(centralwidget)
        third_groupbox.setObjectName("third_groupbox")
        draft_txtedt = QtWidgets.QLineEdit(third_groupbox)
        draft_txtedt.setGeometry(QtCore.QRect(10, 20, 201, 141))
        draft_txtedt.setObjectName("draft_txtedt")
        self.topwidget.addWidget(third_groupbox)      
        fourth_groupbox = QtWidgets.QGroupBox(centralwidget)  
        fourth_groupbox.setObjectName("fourth_groupbox")
        val_txtedt = QtWidgets.QLineEdit(fourth_groupbox)
        val_txtedt.setGeometry(QtCore.QRect(10, 20, 201, 141))
        val_txtedt.setObjectName("val_txtedt")
        self.topwidget.addWidget(fourth_groupbox)
        self.fifth_groupBox = QtWidgets.QGroupBox(centralwidget)
        self.fifth_groupBox.setTitle("")
        self.fifth_groupBox.setObjectName("fifth_groupBox")
        strtype_label = QtWidgets.QLabel(self.fifth_groupBox)
        strtype_label.setGeometry(QRect(10, 30, 221, 20))
        strtype_label.setAlignment(Qt.AlignCenter)                
        strtype_label.setObjectName("strtype_label")
        linebreaks_label = QtWidgets.QLabel(self.fifth_groupBox)
        linebreaks_label.setGeometry(QRect(30, 50, 200, 20))
        linebreaks_label.setAlignment(Qt.AlignCenter) 
        linebreaks_label.setObjectName("linebreaks_label")
        maxlines_label = QtWidgets.QLabel(self.fifth_groupBox)
        maxlines_label.setGeometry(QtCore.QRect(70, 70, 100, 20))
        maxlines_label.setAlignment(Qt.AlignCenter) 
        maxlines_label.setObjectName("maxlines_label")
        self.enter_btn = QtWidgets.QPushButton(self.fifth_groupBox)
        self.enter_btn.setGeometry(QtCore.QRect(20, 110, 191, 41))
        self.enter_btn.setObjectName("enter_btn")
        self.topwidget.addWidget(self.fifth_groupBox)
        self.mainlayout.addLayout(self.topwidget)
        #midwidget = QtWidgets.QVBoxLayout()
        midwidget.setObjectName("midwidget")
        lidTableView_groupbox = QtWidgets.QGroupBox(centralwidget)
        lidTableView_groupbox.setTitle("")
        lidTableView_groupbox.setObjectName("lidTableView_groupbox")      
        # self.listWidget = QtWidgets.QListWidget(self.lidTableView_groupbox)
        # self.listWidget.setGeometry(QtCore.QRect(10, 20, 1361, 192))
        # self.listWidget.setObjectName("listWidget")
        listbox_view1 = ListBoxWidget(lidTableView_groupbox)              
        midwidget.addWidget(lidTableView_groupbox)        
        self.mainlayout.addLayout(midwidget)
        self.midwidget_title = QtWidgets.QLabel(lidTableView_groupbox)
        self.midwidget_title.setGeometry(QtCore.QRect(490, 20, 221, 16))
        self.midwidget_title.setAlignment(QtCore.Qt.AlignHCenter)
        self.midwidget_title.setObjectName("midwidget_title_2")
        self.guide_label1 = QtWidgets.QLabel(lidTableView_groupbox)
        self.guide_label1.setGeometry(QtCore.QRect(470, 80, 421, 21))      
        self.guide_label1.setAlignment(QtCore.Qt.AlignVCenter)
        self.guide_label1.setObjectName("guidelabel")
        self.bottomwidget = QtWidgets.QHBoxLayout()
        self.bottomwidget.setObjectName("bottomwidget")
        leftinbottomlayout = QtWidgets.QVBoxLayout()
        leftinbottomlayout.setObjectName("leftinbottomlayout")        
        masterDB_groupbox = QtWidgets.QGroupBox(centralwidget)
        masterDB_groupbox.setTitle("")
        masterDB_groupbox.setObjectName("masterDB_groupbox")              
        listbox_view2 = ListBoxWidget(masterDB_groupbox)
        leftinbottomlayout.addWidget(masterDB_groupbox)
        self.masterdb_title = QtWidgets.QLabel(masterDB_groupbox)
        self.masterdb_title.setGeometry(QtCore.QRect(200, 10, 201, 16))
        self.masterdb_title.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.masterdb_title.setObjectName("masterdb_title")     
        self.guide_label2 = QtWidgets.QLabel(masterDB_groupbox)
        self.guide_label2.setGeometry(QtCore.QRect(110, 80, 421, 21))              
        self.guide_label2.setObjectName("guidelabel")
        self.guide_label2.setAlignment(QtCore.Qt.AlignVCenter)
        self.bottomwidget.addLayout(leftinbottomlayout)
        self.rightinbottomlayout = QtWidgets.QHBoxLayout()
        self.rightinbottomlayout.setObjectName("rightinbottomlayout")
        self.preview_groupbox = QtWidgets.QGroupBox(centralwidget)
        self.preview_groupbox.setTitle("")
        self.preview_groupbox.setObjectName("preview_groupbox")
        self.preview_title = QtWidgets.QLabel(self.preview_groupbox)
        self.preview_title.setGeometry(QtCore.QRect(240, 10, 101, 20))
        self.preview_title.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.preview_title.setObjectName("preview_title")
        self.rightinbottomlayout.addWidget(self.preview_groupbox)
        self.bottomwidget.addLayout(self.rightinbottomlayout)
        self.mainlayout.addLayout(self.bottomwidget)
        self.gridLayout.addLayout(self.mainlayout, 0, 0, 1, 1)
        
        statusbar = QtWidgets.QProgressBar(centralwidget)
        statusbar.setProperty("value", 0)
        statusbar.setObjectName("statusbar")
        self.gridLayout.addWidget(statusbar, 1, 0, 1, 1)
        MainWindow.setCentralWidget(centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1255, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.reset_action = QAction("초기화")
        self.quit_action = QAction("종료")
        self.reset_action.triggered.connect(readexcel1.fun_reset)        
        self.quit_action.triggered.connect(qApp.quit)             
        
        
        file_menu = self.menubar.addMenu("메뉴")
        file_menu.addAction(self.reset_action)
        file_menu.addAction(self.quit_action)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    
       

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectlanguage_label.setText(_translate("MainWindow", "번역 언어 선택"))
        self.scenario_view_btn.setText(_translate("MainWindow", "UX 시나리오 보기"))
        second_groupbox.setTitle(_translate("MainWindow", "Reference"))
        third_groupbox.setTitle(_translate("MainWindow", "Draft"))
        fourth_groupbox.setTitle(_translate("MainWindow", "Validation"))
        self.guide_label1.setText(_translate("MainWindow", "1. 검수할 엑셀 파일을 여기에 드래그 앤 드롭 하세요."))
        self.guide_label2.setText(_translate("MainWindow", "2. Multilanguage Master DB 파일을 여기에 드래그 앤 드롭 하세요."))
        strtype_label.setText(_translate("MainWindow", "String Type:"))
        linebreaks_label.setText(_translate("MainWindow", "Manual line breaks:"))
        maxlines_label.setText(_translate("MainWindow", "Max lines:"))
        self.enter_btn.setText(_translate("MainWindow", "검수 완료(Enter)"))
        self.midwidget_title.setText(_translate("MainWindow", "Validation Request"))
        self.masterdb_title.setText(_translate("MainWindow", "유사 단어/문장 in Master DB"))
        self.preview_title.setText(_translate("MainWindow", "Preview"))
        self.menu.setTitle(_translate("MainWindow", "메뉴"))       
        
    def fileErrorAlert():     
       # click 함수가 실행 될때, QMessageBox()가 생성된다. 
        fileError_Alert = QMessageBox()
        fileError_Alert.setText("잘못된 파일입니다.")
        fileError_Alert.exec() 
        
if __name__ == "__main__":    
    app = QtWidgets.QApplication(sys.argv)    
    MainWindow = QtWidgets.QMainWindow()
    readexcel1 = MultiLanguageReadExcel()
    readexcel2 = MasterDBReadExcel()
    listbox_view1 = ListBoxWidget()
    listbox_view2 = ListBoxWidget()    
    centralwidget = QtWidgets.QWidget()
    combobox = QtWidgets.QComboBox()
    uidinfo_txtedt = QtWidgets.QLineEdit()
    componentinfo_txtedt = QtWidgets.QLineEdit()
    lidTableView_groupbox = QtWidgets.QGroupBox(centralwidget)
    strtype_label = QtWidgets.QLabel()
    linebreaks_label = QtWidgets.QLabel()
    maxlines_label = QtWidgets.QLabel()
    midwidget =  QtWidgets.QVBoxLayout()    
    second_groupbox = QtWidgets.QGroupBox(centralwidget)
    third_groupbox = QtWidgets.QGroupBox(centralwidget)
    fourth_groupbox = QtWidgets.QGroupBox(centralwidget)
    ref_textedt = QtWidgets.QLineEdit(second_groupbox) 
    draft_txtedt = QtWidgets.QLineEdit(third_groupbox)   
    val_txtedt = QtWidgets.QLineEdit(fourth_groupbox)
    leftinbottomlayout = QtWidgets.QVBoxLayout()    
    masterDB_groupbox = QtWidgets.QGroupBox(centralwidget)
    masterDB_groupbox.setMinimumSize(800,200)  #?      
    statusbar = QtWidgets.QProgressBar()    
    table1 = QTableWidget()     
    table1.setMaximumSize(1280,260) #핵심 사이즈 조절 메소드    
    table2 = QTableWidget()     
    table2.setMaximumSize(800,200) #핵심 사이즈 조절 메소드       
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())