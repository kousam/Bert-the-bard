


import asyncio
from asyncqt import QEventLoop

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

import sys
import os
import subprocess


from GUI import GUI



class App():
    def __init__(self):
        pass

    def createLoop(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def runLoop(self):
        try:
            self.loop.run_forever()

        except Exception as e:
            print(e)

        finally:
            self.loop.close()

    def openModsFolder(self):
        try:
            path = os.path.dirname(os.path.realpath(__file__))
            mods_path = os.path.abspath(os.path.join(path, 'mods'))
        except Exception as e:
            print(e)
            
        
        subprocess.Popen('explorer "{}"'.format(mods_path))

    def getLoop(self):
        return self.loop


    def run(self):
        os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        self.qApp = QApplication(sys.argv)
        self.loop = QEventLoop(self.qApp)
        asyncio.set_event_loop(self.loop)
        
        self.gui = GUI(self)
        self.gui.show()

        self.loop.run_forever()

        sys.exit(self.qApp.exec_())

    def quit(self):
        sys.exit(self.qApp.exec_())













