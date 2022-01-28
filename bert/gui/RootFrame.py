from PyQt5.QtWidgets import QFrame



class RootFrame(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def getGUI(self):
        return self.parent.getGUI()

    def getParent(self):
        return self.parent
        
    def highlight(self):
        self.setStyleSheet("background-color: rgb(200, 100, 100)")
        
