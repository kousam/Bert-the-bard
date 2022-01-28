from PyQt5.QtWidgets import QFrame, QHBoxLayout, QGraphicsDropShadowEffect, QLabel, QPushButton
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QColor, QFont

from gui.RootFrame import RootFrame



class Topbar(RootFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.h = 32

        self.setFixedHeight(self.h)
        self.setObjectName('top_bar')
        
        shadow = QGraphicsDropShadowEffect()
  
        shadow.setBlurRadius(20)
        shadow.setOffset(0,2)
        shadow.setColor(QColor(0,0,0))
        #self.setGraphicsEffect(shadow)
        
        self.maximized = False
        


        self.initUI()
        
        
        

    def initUI(self):
        self.initLayout()
        self.initWidgets()
        
        self.layout.addWidget(self.title_label, alignment=Qt.AlignLeft)
        self.layout.addStretch()
        self.layout.addWidget(self.minimize_button, alignment=Qt.AlignRight)
        self.layout.addWidget(self.maximize_button, alignment=Qt.AlignRight)
        self.layout.addWidget(self.exit_button, alignment=Qt.AlignRight)
        
        self.setLayout(self.layout)

    def initLayout(self):
        # build main layout
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(10,0,0,0)
        self.layout.setAlignment(Qt.AlignRight)
        self.layout.setSpacing(0)

    def initWidgets(self):
        font = QFont("Roboto", 12)
        self.title_label = QLabel('Bert the bard')
        self.title_label.setFixedHeight(self.h)
        #self.title_label.setAlignment(Qt.Align)
        self.title_label.setFixedWidth(300)
        self.title_label.setFont(font)
        #self.title_label.setStyleSheet('background-color: #dddddd')
        
    
        self.exit_button = QPushButton('X')
        self.exit_button.setFixedSize(self.h * 2, self.h)
        self.exit_button.setObjectName('exit_button')
        self.exit_button.clicked.connect(self.exitButtonAction)
        
        
        self.maximize_button = QPushButton('[ ]')
        self.maximize_button.setFixedSize(self.h*2, self.h)
        self.maximize_button.setObjectName('topbar_button')
        self.maximize_button.clicked.connect(self.maximizeButtonAction)
        
        
        self.minimize_button = QPushButton('_')
        self.minimize_button.setFixedSize(self.h*2, self.h)
        self.minimize_button.setObjectName('topbar_button')
        self.minimize_button.clicked.connect(self.minimizeButtonAction)
        


    def mousePressEvent(self, event):
        
        self.oldPos = event.globalPos()
        
   

    def mouseMoveEvent(self, event):
        
        gui = self.getGUI()
        
        if not gui.maxim:
        
            delta = QPoint(event.globalPos() - self.oldPos)
            
            gui.move(gui.x() + delta.x(), gui.y() + delta.y())
            
            self.oldPos = event.globalPos()
    
    def exitButtonAction(self):
        
        self.getGUI()._quit()
        
    def maximizeButtonAction(self):
        self.getGUI()._maximize()
        
    def minimizeButtonAction(self):
        self.getGUI()._minimize()







