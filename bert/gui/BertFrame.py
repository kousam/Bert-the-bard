from PyQt5.QtWidgets import QFrame, QGridLayout, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QTextCursor, QColor


from gui.RootFrame import RootFrame
from gui.Logger import Logger

from essentials.fileMrg import FileMgr

import os

class BertFrame(RootFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.showing_token = False

        self.initUI()

        self.getGUI().setLogger(self.logger)


    def initUI(self):
        self.initLayout()
        self.initWidgets()

        

        self.startStop_layout.addWidget(self.start_button)
        self.startStop_layout.addWidget(self.stop_button)

        self.startStop_frame.setLayout(self.startStop_layout)    
            

        
        
        self.tokenButton_layout.addWidget(self.saveToken_button)
        self.tokenButton_layout.addWidget(self.loadToken_button)
        self.tokenButton_layout.addWidget(self.showToken_button)

        self.tokenButton_frame.setLayout(self.tokenButton_layout)

        self.token_layout.addWidget(self.token_input)
        self.token_layout.addWidget(self.tokenButton_frame)

        self.token_frame.setLayout(self.token_layout)


        self.left_layout.addWidget(self.token_frame)
        

        
        self.left_layout.addWidget(self.openModsFolder_button, alignment=Qt.AlignCenter)
        self.left_layout.addWidget(self.startStop_frame)
        


            
        self.left_frame.setLayout(self.left_layout)

        #self.left_frame.setObjectName('test')


        #self.right_layout.addWidget(self.log_label)
        self.right_layout.addWidget(self.logger)
            
        self.right_frame.setLayout(self.right_layout)


        #self.token_input.setText('NTAwOTczMTEwMzMwMzkyNTc2.DsY3Gw.9FBWyfLFYyRUC0x7sZT2OVDiqMU')


        

        self.right_frame.setFixedWidth(500)
            
            
        self.layout.addWidget(self.left_frame)
        self.layout.addWidget(self.right_frame)

        self.setLayout(self.layout)

           


    def initLayout(self):
        # build main layout
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setAlignment(Qt.AlignCenter|Qt.AlignRight)
        self.layout.setSpacing(0)
        
        self.left_layout = QVBoxLayout()
        self.left_layout.setContentsMargins(10,40,10,10)
        self.left_layout.setAlignment(Qt.AlignCenter|Qt.AlignTop)
        self.left_layout.setSpacing(20)

        self.right_layout = QVBoxLayout()
        self.right_layout.setContentsMargins(10,10,10,10)
        self.right_layout.setAlignment(Qt.AlignCenter)
        self.right_layout.setSpacing(10)

        self.token_layout = QVBoxLayout()
        self.token_layout.setContentsMargins(0,0,0,0)
        self.token_layout.setAlignment(Qt.AlignCenter|Qt.AlignTop)
        self.token_layout.setSpacing(0)

        self.tokenButton_layout = QHBoxLayout()
        self.tokenButton_layout.setContentsMargins(0,0,0,10)
        self.tokenButton_layout.setAlignment(Qt.AlignRight)
        self.tokenButton_layout.setSpacing(10)
        
        self.startStop_layout = QHBoxLayout()
        self.startStop_layout.setContentsMargins(0,10,0,10)
        self.startStop_layout.setAlignment(Qt.AlignCenter)
        self.startStop_layout.setSpacing(20)

        

    def initWidgets(self):
        self.left_frame = QFrame()
        self.right_frame = QFrame()
        self.startStop_frame = QFrame()

        self.token_frame = QFrame()
        self.tokenButton_frame = QFrame()


        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(2,2)
        shadow.setColor(QColor(10,10,10,255))
        
        

        font = QFont("Roboto", 12)
        
        self.token_input = QLineEdit()
        self.token_input.setEchoMode(QLineEdit.Password)
        self.token_input.setFixedWidth(660)
        self.token_input.setPlaceholderText("Enter Token") 
        self.token_input.setFixedHeight(38)
        self.token_input.setFont(font)
        self.token_input.setAlignment(Qt.AlignCenter)
        self.token_input.setObjectName('default_lineEdit')

        self.token_input.setGraphicsEffect(shadow)


        self.logger = Logger(self)


        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(2,2)
        shadow.setColor(QColor(10,10,10,255))


        self.openModsFolder_button = QPushButton('Open mods folder')
        self.openModsFolder_button.setFixedWidth(160)
        self.openModsFolder_button.setFixedHeight(50)
        self.openModsFolder_button.setFont(font)
        self.openModsFolder_button.setObjectName('default_button')
        self.openModsFolder_button.setGraphicsEffect(shadow)

        self.openModsFolder_button.clicked.connect(self.openModsFolder)


        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(2,2)
        shadow.setColor(QColor(10,10,10,255))


        self.start_button = QPushButton('Start')
        self.start_button.setFixedWidth(160)
        self.start_button.setFixedHeight(50)
        self.start_button.setFont(font)
        self.start_button.setObjectName('default_button')
        self.start_button.setGraphicsEffect(shadow)
    

        self.start_button.clicked.connect(self.run)


        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(2,2)
        shadow.setColor(QColor(10,10,10,255))

        self.stop_button = QPushButton('Stop')
        self.stop_button.setFixedWidth(160)
        self.stop_button.setFixedHeight(50)
        self.stop_button.setFont(font)
        self.stop_button.setObjectName('default_button')
        self.stop_button.setGraphicsEffect(shadow)

        self.stop_button.clicked.connect(self.killBert)


        self.log_label = QLabel('Log output')


        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(2,2)
        shadow.setColor(QColor(10,10,10,255))

        self.saveToken_button = QPushButton('Save')
        self.saveToken_button.setFixedWidth(80)
        self.saveToken_button.setFixedHeight(38)
        self.saveToken_button.setFont(font)
        self.saveToken_button.setObjectName('default_button')
        self.saveToken_button.setGraphicsEffect(shadow)

        self.saveToken_button.clicked.connect(self.saveToken)


        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(2,2)
        shadow.setColor(QColor(10,10,10,255))

        self.loadToken_button = QPushButton('Load')
        self.loadToken_button.setFixedWidth(80)
        self.loadToken_button.setFixedHeight(38)
        self.loadToken_button.setFont(font)
        self.loadToken_button.setObjectName('default_button')
        self.loadToken_button.setGraphicsEffect(shadow)

        self.loadToken_button.clicked.connect(self.loadToken)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(2,2)
        shadow.setColor(QColor(10,10,10,255))

        self.showToken_button = QPushButton('Show')
        self.showToken_button.setFixedWidth(80)
        self.showToken_button.setFixedHeight(38)
        self.showToken_button.setFont(font)
        self.showToken_button.setObjectName('default_button')
        self.showToken_button.setGraphicsEffect(shadow)

        self.showToken_button.clicked.connect(self.showToken)




    def run(self):
        token = self.token_input.text()

        self.getGUI().runBert(token)

    def openModsFolder(self):
        self.getGUI().getApp().openModsFolder()


    def killBert(self):
        self.getGUI().killBert()


    def saveToken(self):
        try:
            token = self.token_input.text()
            FileMgr.saveToken(token)
        except Exception as e:
            print(e)

    def loadToken(self):
        # temp location
        
        token = FileMgr.getToken()
        self.token_input.setText(token)
        
    def showToken(self):
        if self.showing_token:
            self.token_input.setEchoMode(QLineEdit.Password)
        else:
            self.token_input.setEchoMode(QLineEdit.Normal)

        self.showing_token = self.showing_token == False
        

        


