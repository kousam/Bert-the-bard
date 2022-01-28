from PyQt5.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QStackedLayout

from gui.BertFrame import BertFrame
from gui.RootFrame import RootFrame
from gui.Topbar import Topbar


import traceback


class MainFrame(RootFrame):

    def __init__(self, parent):
        super().__init__(parent)
        
        self.setObjectName('main_frame')
        
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        
        self.topBar_frame = Topbar(self)

        self.content_frame = QFrame()
        self.content_layout = QStackedLayout()

        self.content_frame.setLayout(self.content_layout)
        
        self.layout.addWidget(self.topBar_frame)
        self.layout.addWidget(self.content_frame)

        self.bert_frame = BertFrame(self)

        self.content_layout.insertWidget(0, self.bert_frame)

        self.setLayout(self.layout)


