from PyQt5 import QtCore, QtGui, QtWidgets
from tqdm import tqdm
import time
import sys, os
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


links = [] # 파일 담는 리스트 (단일만 받게 link[0]만 쓰임)
length_df = 0 
class ListBoxWidget(QListWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(1280, 260)

    def dragEnterEvent(self, event): # 파일을 드래그 가능 영역으로 들어오는 순간을 제어하는 메소드
        if event.mimeData().hasUrls:
            event.accept()
            #print("Drag Enter Event Accepted")
        else:
            event.ignore()
            

    def dragMoveEvent(self, event): # 파일을 드래그 가능 영역안에서 움직이는 순간을 제어하는 메소드
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()           
            verticalLayout_2.replaceWidget(listbox_view1,progress)
        
                
            
        else:
            event.ignore()
            
        
            

    def dropEvent(self, event):
        
        global table
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            

           
            for url in event.mimeData().urls():
                
                if url.isLocalFile():
                    links.append(str(url.toLocalFile()))
                    #print(url.toLocalFile())
                else:
                    links.append(str(url.toString()))
            self.addItems(links)
            excel_file_dir =links[0]
            worksheet_name = '1. Prompt'
            #worksheet_name = '일반음식점_1'
            
            table = QTableWidget()    
            
            
                    
            start = time.time()
            self.loadExcelData(excel_file_dir,worksheet_name)
            
            end = time.time()
            print(f"{end - start:.5f}초에 Read Finished.")
            verticalLayout_2.replaceWidget(progress,table)
        else:
            event.ignore()
            
   
            
    
            
    def loadExcelData(self, excel_file_dir, worksheet_name):
        global table
        global length_df
        #df = pd.read_excel(excel_file_dir,worksheet_name)
        #df = pd.read_excel(excel_file_dir, worksheet_name,usecols='C,K,L,M,N',header=1)
        for i in tqdm(range(0,1), ncols = 100, desc ="Loading data.."): 
            #df= pd.read_excel(excel_file_dir,worksheet_name)
            df= pd.read_excel(excel_file_dir,worksheet_name,usecols='C,K,L,M,N',header=1)
            
                       
        print("------xlsx Reading is completed ------")  
        print(df.to_dict(orient='dict'))
        length_df = len(df)
        print(f'데이터 행 길이는 {len(df)}입니다.')    
                  
       
        
        if df.size == 0:
                return
            
            
        df.fillna('', inplace=True)
        table.setRowCount(df.shape[0])
        table.setColumnCount(df.shape[1])
        table.setHorizontalHeaderLabels(df.columns)    
                      
        for row in tqdm(df.iterrows(),mininterval=0.001,ncols=100,leave=True,total=length_df):
            
            values = row[1]
            
            진행률 = int(int(row[0])/length_df * 100)             
            progress.setValue(진행률)
            for col_index, value in enumerate(values):
                if isinstance(value, (float,int)):
                    value = '{0:0,.0f}'.format(value)
                tableItem = QTableWidgetItem(str(value))
                table.setItem(row[0],col_index, tableItem)
                
        table.setColumnWidth(2,300)
        print("데이터 생성 완료")
    
    def search(self,s):
        global table
        
        
        # table.setColumnWidth(None)
    
        if not s:
            return
        
        matching_items = table.findItems(s, Qt.MatchContains)
        if matching_items:
            item = matching_items[0]
            table.setCurrentItem(item) 


class Ui_Form(QMainWindow):
    def setupUi(self, Form):
        
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1286, 829)
        # self.gridLayout = QGridLayout(Form)21
        # self.gridLayout.setObjectName(u"gridLayout")
        
        
        global verticalLayoutWidget_2
        global verticalLayout_2 
        global listbox_view1        
        global verticalLayoutWidget
        global referenceLayout
        global textEdit_3
               
        
        
       
        self.topLayout = QtWidgets.QVBoxLayout(verticalLayoutWidget)
        self.topLayout.setContentsMargins(0, 0, 0, 0)
        self.topLayout.setObjectName("topLayout")
        self.top_horizontalLayout = QtWidgets.QHBoxLayout()
        self.top_horizontalLayout.setObjectName("top_horizontalLayout")
        self.languageInputLayout = QtWidgets.QGroupBox(verticalLayoutWidget)
        self.languageInputLayout.setTitle("")
        self.languageInputLayout.setObjectName("languageInputLayout")
        self.label = QtWidgets.QLabel(self.languageInputLayout)
        self.label.setGeometry(QtCore.QRect(10, 20, 141, 41))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.languageInputLayout)
        self.comboBox.setGeometry(QtCore.QRect(10, 70, 221, 21))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.languageInputLayout)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 110, 221, 73))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_2.addWidget(self.textEdit_2)
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(self.languageInputLayout)
        self.pushButton.setGeometry(QtCore.QRect(10, 190, 221, 41))
        self.pushButton.setObjectName("pushButton")
        self.top_horizontalLayout.addWidget(self.languageInputLayout)
        referenceLayout = QtWidgets.QGroupBox(verticalLayoutWidget)
        referenceLayout.setTitle("")
        referenceLayout.setObjectName("referenceLayout")
        self.label_2 = QtWidgets.QLabel(referenceLayout)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 56, 12))
        self.label_2.setObjectName("label_2")
        textEdit_3 = QtWidgets.QLineEdit(referenceLayout)
        textEdit_3.setGeometry(QtCore.QRect(13, 70, 221, 131))
        textEdit_3.setObjectName("textEdit_3")
        textEdit_3.setPlaceholderText("Search...")        
        textEdit_3.textChanged.connect(listbox_view1.search)
        self.top_horizontalLayout.addWidget(referenceLayout)
        self.draftLayout = QtWidgets.QGroupBox(verticalLayoutWidget)
        self.draftLayout.setTitle("")
        self.draftLayout.setObjectName("draftLayout")
        self.label_3 = QtWidgets.QLabel(self.draftLayout)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 56, 12))
        self.label_3.setObjectName("label_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.draftLayout)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 70, 221, 131))
        self.textEdit_4.setObjectName("textEdit_4")
        self.top_horizontalLayout.addWidget(self.draftLayout)
        self.validationLayout = QtWidgets.QGroupBox(verticalLayoutWidget)
        self.validationLayout.setTitle("")
        self.validationLayout.setObjectName("validationLayout")
        self.label_4 = QtWidgets.QLabel(self.validationLayout)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 56, 12))
        self.label_4.setObjectName("label_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.validationLayout)
        self.textEdit_5.setGeometry(QtCore.QRect(20, 70, 221, 131))
        self.textEdit_5.setObjectName("textEdit_5")
        self.top_horizontalLayout.addWidget(self.validationLayout)
        self.contentsInfoLayout = QtWidgets.QGroupBox(verticalLayoutWidget)
        self.contentsInfoLayout.setTitle("")
        self.contentsInfoLayout.setObjectName("contentsInfoLayout")
        self.label_5 = QtWidgets.QLabel(self.contentsInfoLayout)
        self.label_5.setGeometry(QtCore.QRect(60, 30, 171, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.contentsInfoLayout)
        self.label_6.setGeometry(QtCore.QRect(20, 60, 171, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.contentsInfoLayout)
        self.label_7.setGeometry(QtCore.QRect(70, 90, 171, 16))
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.contentsInfoLayout)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 150, 221, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.top_horizontalLayout.addWidget(self.contentsInfoLayout)
        self.topLayout.addLayout(self.top_horizontalLayout)
        # self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 290, 1271, 251))
        verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        #verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        
        verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        # self.listbox_view1 = ListBoxWidget(self)        
        verticalLayout_2.addWidget(listbox_view1)
        verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 560, 811, 241))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.listbox_view2 = ListBoxWidget(self)
        self.horizontalLayout_3.addWidget(self.listbox_view2)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(840, 560, 441, 241))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.statusbar = QProgressBar(self.centralWidget)
        self.statusbar.setObjectName('statusbar')
        self.statusbar.setValue(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        # self.topLayout.addLayout(self.top_horizontalLayout)
        # self.gridLayout.addLayout(self.topLayout, 0,0,1,2)
        # self.gridLayout.addLayout(verticalLayout_2, 1,0,1,2)
        # self.gridLayout.addLayout(self.horizontalLayout_3, 2,0,1,1)
        # self.gridLayout.addWidget(self.groupBox, 2,0,1,2)
        
        
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "번역 언어 선택"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.label_2.setText(_translate("Form", "Reference"))
        self.label_3.setText(_translate("Form", "Draft"))
        self.label_4.setText(_translate("Form", "Validation"))
        self.label_5.setText(_translate("Form", "String Type :"))
        self.label_6.setText(_translate("Form", "Manual line breaks :"))
        self.label_7.setText(_translate("Form", "Max lines :"))
        self.pushButton_2.setText(_translate("Form", "검수 완료(Enter)"))
        self.groupBox.setTitle(QCoreApplication.translate("Form",u"Preview",None))


if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    
    verticalLayoutWidget = QtWidgets.QWidget(Form)
    verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 1271, 251))
    verticalLayoutWidget.setObjectName("verticalLayoutWidget")
    referenceLayout = QtWidgets.QGroupBox(verticalLayoutWidget)
    referenceLayout.setTitle("")
    referenceLayout.setObjectName("referenceLayout")
    referenceLayout = QtWidgets.QGroupBox(verticalLayoutWidget)
    referenceLayout.setTitle("")
    referenceLayout.setObjectName("referenceLayout")
    textEdit_3 = QtWidgets.QTextEdit()    
    listbox_view1 = ListBoxWidget() 
    progress = QProgressBar() 
    
    verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
    verticalLayout_2 = QtWidgets.QVBoxLayout(verticalLayoutWidget_2)
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    
    sys.exit(app.exec_())
