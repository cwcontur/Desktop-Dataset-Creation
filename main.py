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
from pathlib import Path
from PyQt6 import QtWidgets
import sys


# from PyQt5 import QtCore, QtGui, QtWidgets


# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(800, 600)
#         MainWindow.setMouseTracking(True)
#         icon = QtGui.QIcon.fromTheme("Label")
#         MainWindow.setWindowIcon(icon)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
#         self.graphicsView.setGeometry(QtCore.QRect(130, 10, 541, 351))
#         self.graphicsView.setAutoFillBackground(True)
#         self.graphicsView.setViewportUpdateMode(QtWidgets.QGraphicsView.SmartViewportUpdate)
#         self.graphicsView.setObjectName("graphicsView")
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(350, 430, 75, 23))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(430, 430, 75, 23))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_3.setGeometry(QtCore.QRect(270, 430, 75, 23))
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
#         self.radioButton.setGeometry(QtCore.QRect(300, 410, 82, 17))
#         self.radioButton.setFocusPolicy(QtCore.Qt.StrongFocus)
#         self.radioButton.setText("")
#         self.radioButton.setChecked(True)
#         self.radioButton.setObjectName("radioButton")
#         self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
#         self.radioButton_2.setGeometry(QtCore.QRect(380, 410, 82, 20))
#         self.radioButton_2.setText("")
#         self.radioButton_2.setObjectName("radioButton_2")
#         self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
#         self.radioButton_3.setGeometry(QtCore.QRect(460, 410, 82, 17))
#         self.radioButton_3.setText("")
#         self.radioButton_3.setObjectName("radioButton_3")
#         self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
#         self.progressBar.setGeometry(QtCore.QRect(230, 520, 351, 23))
#         self.progressBar.setProperty("value", 24)
#         self.progressBar.setObjectName("progressBar")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(266, 460, 61, 20))
#         self.label.setObjectName("label")
#         self.label_2 = QtWidgets.QLabel(self.centralwidget)
#         self.label_2.setGeometry(QtCore.QRect(360, 460, 61, 20))
#         self.label_2.setObjectName("label_2")
#         self.label_3 = QtWidgets.QLabel(self.centralwidget)
#         self.label_3.setGeometry(QtCore.QRect(440, 460, 61, 20))
#         self.label_3.setObjectName("label_3")
#         self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_4.setGeometry(QtCore.QRect(570, 430, 75, 23))
#         self.pushButton_4.setObjectName("pushButton_4")
#         self.label_4 = QtWidgets.QLabel(self.centralwidget)
#         self.label_4.setGeometry(QtCore.QRect(590, 460, 47, 13))
#         self.label_4.setObjectName("label_4")
#         self.keySequenceEdit = QtWidgets.QKeySequenceEdit(self.centralwidget)
#         self.keySequenceEdit.setGeometry(QtCore.QRect(80, 470, 113, 20))
#         self.keySequenceEdit.setObjectName("keySequenceEdit")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
#         self.menubar.setObjectName("menubar")
#         self.menuFile = QtWidgets.QMenu(self.menubar)
#         self.menuFile.setObjectName("menuFile")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#         self.actionOpen_Folder = QtWidgets.QAction(MainWindow)
#         self.actionOpen_Folder.setObjectName("actionOpen_Folder")
#         self.actionconfirm = QtWidgets.QAction(MainWindow)
#         self.actionconfirm.setObjectName("actionconfirm")
#         self.actionQuit = QtWidgets.QAction(MainWindow)
#         self.actionQuit.setObjectName("actionQuit")
#         self.menuFile.addAction(self.actionOpen_Folder)
#         self.menuFile.addSeparator()
#         self.menuFile.addAction(self.actionQuit)
#         self.menubar.addAction(self.menuFile.menuAction())

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         MainWindow.setToolTip(_translate("MainWindow", "A program that lets you label data."))
#         self.graphicsView.setToolTip(_translate("MainWindow", "<html><head/><body><p>Picture currently receiving label for dataset.</p></body></html>"))
#         self.pushButton.setText(_translate("MainWindow", "She/Her"))
#         self.pushButton_2.setText(_translate("MainWindow", "They/Them"))
#         self.pushButton_3.setText(_translate("MainWindow", "He/Him"))
#         self.label.setText(_translate("MainWindow", "Left Arrow"))
#         self.label_2.setText(_translate("MainWindow", "Down Arrow"))
#         self.label_3.setText(_translate("MainWindow", "Right Arrow"))
#         self.pushButton_4.setText(_translate("MainWindow", "Label"))
#         self.label_4.setText(_translate("MainWindow", "Up Arrow"))
#         self.keySequenceEdit.setWhatsThis(_translate("MainWindow", "This is a test shortcut"))
#         self.keySequenceEdit.setKeySequence(_translate("MainWindow", "Ctrl+E"))
#         self.menuFile.setTitle(_translate("MainWindow", "File"))
#         self.actionOpen_Folder.setText(_translate("MainWindow", "Open Folder"))
#         self.actionconfirm.setText(_translate("MainWindow", "confirm"))
#         self.actionQuit.setText(_translate("MainWindow", "Quit"))


# * Tool tip basic layout        
# QToolTip.setFont(QFont('SansSerif', 10))

# self.setToolTip('This is a <b>QWidget</b> widget')

# btn = QPushButton('Button', self)
# btn.setToolTip('This is a <b>QPushButton</b> widget')
# * ------------------------

import random
import sys

from PyQt6.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QFrame, QApplication
from PyQt6.QtWidgets import *

class Ui_MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        
        # self.statusbar = self.statusBar()

        self.tabs()
        
        self.center()
        self.setWindowTitle("Dataset Label Creator")
        self.setMinimumSize(QSize(800, 500))
        self.setMaximumSize(QSize(1920, 1080))
        
        self.show()
    
    def center(self):

        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def tabs(self):
        tabs = QTabWidget()
        tabs.setTabPosition(self, topLeft)
        tabs.setMovable(True)
        
        tabs.addTab(Folder("Folder"), "Folder")
        # tabs.addTab(Save("Save"), "Save")
        tabs.addTab(Quit("Quit"), "Quit")
        self.setCentralWidget(tabs)

        
    
class Folder(QWidget):
    
    def __init__(self, folder):
        super(Folder, self).__init__()
        self.initButton()
        
    def initButton(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        
    def showDialog(self):
    
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if fname[0]:

            f = open(fname[0], 'r')

            with f:

                data = f.read()
                self.textEdit.setText(data)
                
                
                
# class Save(QWidget):
    
#     def __init__(self, save):
#         super(Save, self).__init__()
#         self.initButton()

#     def initButton(self):
        
class Quit(QWidget):
    
    def __init__(self, quit):
        super(Quit, self).__init__()
        self.initButton()

    def initButton(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:

            event.accept()
        else:

            event.ignore()

        
        
        
    # def __init__(self, parent = None):
    #     super().__init__()
    #     super(Ui_MainWindow, self).__init__(parent)
		
    #     layout = QVBoxLayout()
    #     self.btn = QPushButton("QFileDialog static method")
    #     self.btn.clicked.connect(self.getfile)
            
    #     layout.addWidget(self.btn)
    #     self.le = QLabel("Hello")
            
    #     layout.addWidget(self.le)
    #     self.btn1 = QPushButton("QFileDialog object")
    #     self.btn1.clicked.connect(self.getfiles)
    #     layout.addWidget(self.btn1)
            
    #     self.contents = QTextEdit()
    #     layout.addWidget(self.contents)
    #     self.setLayout(layout)
    #     self.setWindowTitle("File Dialog demo")
        # self.initUI()

    # def initUI(self):
        # ----------------------------------------------------------------
        # hbox = QHBoxLayout(self)
        # # pixmap = QPixmap('noctua.jpg')

        # lbl = QLabel(self)
        # lbl.setPixmap(pixmap)
        # # ----------------------------------------------------------------
        # self.textEdit = QTextEdit()
        # self.statusBar()

        # openFile = QAction(QIcon('open.png'), 'Open', self)
        # openFile.setShortcut('Crtl+o')
        # openFile.setStatusTip('Open new File')
        # openFile.triggered.connect(self.showDialog)

        # menubar = self.menubar()
        # fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(openFile)

        # hbox.addWidget(lbl)
        # self.setLayout(hbox)

        # self.move(300, 200)
        # self.setWindowTitle('Label')
        # self.show()

        # Shows dialog for opening a file
        # def showDialog(self):
        #     home_dir = str(Path.home())
        #     fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        #     if fname[0]:

        #         f = open(fname[0], 'r')

        #         with f:

        #             data = f.read()
        #             self.textEdit.setText(data)
                    
    # def getfile(self):
    #     fname = QFileDialog.getOpenFileName(self, 'Open file', 
    #     'c:\\',"Image files (*.jpg *.gif)")
    #     self.le.setPixmap(QPixmap(fname))
    
    # def getfiles(self):
    #     dlg = QFileDialog()
    #     dlg.setFileMode(QFileDialog.AnyFile)
    #     dlg.setFilter("Text files (*.txt)")
    #     filenames = QStringList()
            
    #     if dlg.exec_():
    #         filenames = dlg.selectedFiles()
    #         f = open(filenames[0], 'r')
                
    #         with f:
    #             data = f.read()
    #             self.contents.setText(data)
    # # Creates a confirm box for quitting the program            
    # def closeEvent(self, event):

    #     reply = QMessageBox.question(self, 'Message',
    #                 "Are you sure to quit?", QMessageBox.StandardButton.Yes |
    #                 QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

    #     if reply == QMessageBox.StandardButton.Yes:

    #         event.accept()
    #     else:

    #         event.ignore()
            
    # Centers the window on the desktop


# ! This remains unchanged; will be used


def main():
    
    app = QApplication([])
    mainwindow = Ui_MainWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
