# A dataset creation tool.
#
#   ,-.       _,---._ __  / \
#  /  )    .-'       `./ /   \
# (  (   ,'            `/    /|
#  \  `-"             \'\   / |
#   `.              ,  \ \ /  |
#    /`.          ,'-`----Y   |
#   (            ;        |   '
#   |  ,-.    ,-'  Connor |  /
#   |  | (   |   Contursi | /
#   )  |  \  `.___________|/
#   `--'   `--'

# importing required libraries
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import *
from PyQt6.QtCore import *

import sys

class test(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap('noctua.jpg')
        
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        
        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        self.move(300, 200)
        self.setWindowTitle('Noctua')
        self.show()
        

def main():
    app = QApplication(sys.argv)
    testing = test()
    sys.exit(app.exec())
    
if __name__ == '__main__':
    main()