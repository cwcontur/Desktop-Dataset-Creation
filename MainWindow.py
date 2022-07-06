from copyreg import pickle
from logging import root
import sys
from tkinter import image_names
import os
import pandas as pd
import numpy as np
# import PyQt5
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5 import QtGui
from matplotlib import image
from pydantic import root_validator
from qtwidgets import Toggle, AnimatedToggle

# global variables for the current image number [progress], and the number of images [images]

class MainWindow(QMainWindow):
    root_directory = os.path.dirname(os.path.abspath("__file__"))
    image_directory = os.path.join(root_directory, "images/")
    mylist = os.listdir(image_directory)
    
    images = 1000
    progress = 0
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # pagelayout = QVBoxLayout()
        # self.stackedWindow = QStackedLayout()
        
        # splashImage = QLabel("Splush")
        # splashImage.setPixmap(QPixmap("cookie_jar.png"))
        # pagelayout.addWidget(splashImage)
        # pagelayout.addLayout(self.stackedWindow)
        # splunk = QWidget()
        # splunk.setLayout(pagelayout)
        # self.setCentralWidget(splunk)        
        # pagelayout.addLayout(self.stackedWindow)
        # splash = QIcon("cookie_jar.png")
        # pagelayout.addWidget(splash)
        # pagelayout.setCentralWidget(splash)
        # self.setLayout(pagelayout)
        pic = QPixmap("cookies_jar.png")
        pix = pic.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        splash = QSplashScreen(pix)
        splash.show()        
        
        
        
        global root_directory
        global image_directory
        root_directory = os.path.dirname(os.path.abspath("__file__"))
        print(root_directory)
        
        image_directory = os.path.join(root_directory, "image_data\\")
        print(image_directory)
        
        global images
        global progression
        images = len(os.listdir(image_directory)) # Counts the number of files in the image directory
        progression = 0
        
        # Array of zeroes with a place for each image
        global mylist
        mylist = np.zeros(shape=(images))
        
        # ? Creates an array of the image file names
        for subdir, dirs, files in os.walk(image_directory):
            for file in files:
                os.chdir(subdir)
                  
                if "female" in subdir:
                    if((images) % 2 != 0):
                        temp = file
                        mylist.insert((images), temp)
                # *-------------------------------- #
                elif "male" in subdir:
                    if((images) % 2 == 0):
                        temp = file
                        mylist.insert((images), temp)

                images += 1  # ! Count of the pictures found

        mylist = os.listdir(image_directory)
        
        self.image_files = mylist
        


        self.setWindowTitle("Dataset Label Creator")
        self.setMinimumSize(QSize(800, 535))
        self.setMaximumSize(QSize(1500, 1000))
        
        self.setWindowIcon(QIcon("cookie--pencil.png"))
        
        self.image = QLabel("Data")
        # self.image.setPixmap(QPixmap(self.image_files[progress]))
        # self.image.setScaledContents(True)
        self.ontoNext()
        
        # image = QPixmap(self.image_files[progress])
        # self.label.setPixmap(image)
        
        # ! -----------------------------------------------------------------------------
        #Creates all of the toggle buttons based on input
        self.she = AnimatedToggle(checked_color="#e6382c", pulse_checked_color="#bfbfbf")
        self.she.setChecked(True)
        self.her = AnimatedToggle(checked_color="#e6572c", pulse_checked_color="#bfbfbf")
        self.her.setChecked(True)
        
        self.he = AnimatedToggle(checked_color="#ebd82f", pulse_checked_color="#bfbfbf")
        self.he.setChecked(True)
        self.him = AnimatedToggle(checked_color="#a9eb2f", pulse_checked_color="#bfbfbf")
        self.him.setChecked(True)
        
        self.they = AnimatedToggle(checked_color="#2f5eeb", pulse_checked_color="#bfbfbf")
        self.they.setChecked(True) 
        self.them = AnimatedToggle(checked_color="#612feb", pulse_checked_color="#bfbfbf")
        self.them.setChecked(True) 
        # ! -----------------------------------------------------------------------------
        
        # Submits button states and moves onto the next image for labeling 
        self.next = QPushButton('Submit', self)
        self.next.clicked.connect(self.ontoNext)
        
        # Creates the progress bar and limits it for the number of images that will be processed

        self.progress_Bar = QProgressBar(self)
        self.progress_Bar.setGeometry(0, 0, 300, 25)
        self.progress_Bar.setMaximum(images) 

        # All layouts needed to be arranged for the GUI
        base_layout = QHBoxLayout()
        image_layout = QVBoxLayout()
        buttons_layout = QVBoxLayout()
        submit_layout = QVBoxLayout()
        
        buttons_layout.addWidget(self.image)
        buttons_layout.addWidget(self.progress_Bar)
        buttons_layout.addWidget(self.she)
        buttons_layout.addWidget(self.he)
        buttons_layout.addWidget(self.they)
        buttons_layout.addWidget(self.next)
        
        
        
        base_layout.addLayout(buttons_layout)
        widget = QWidget()
        widget.setLayout(base_layout)
        self.setCentralWidget(widget)
        splash.finish(self)
        self.show()
        
# * -----------------------------    
    def updateData(self):
        # print("dumb")
        file = self.image_files[self.progress]
        # Increments progress bar
        

    
# * -----------------------------        
    def ontoNext(self):
        global progression
        progression += 1
        global images
        # if progression <= images:
        #     self.progress_Bar.setValue(progression)
        # self.updateData()
        
# * ----------------------------- 
# * Opens dialogue box when no options have been selected, but the 'submit' button was used
    def userError(self):
        errorWindow = QMessageBox(self)
        errorWindow.setWindowTitle("Whoa there!")
        errorWindow.setText("You have to make at least one selection!")
        errorWindow.setStandardButtons(QMessageBox.Ok)
        errorWindow.setIcon("brain--exclamation.png")
        button = errorWindow.exec_()
        
        if button == QMessageBox.Ok:
            errorWindow.close()
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
        
#         self.setWindowTitle("Stupid Bitch")
#         self.setMinimumSize(QSize(800, 535))
#         self.setMaximumSize(QSize(1500, 1000))
        
#         layout = QHBoxLayout()
        
#         layout.addWidget(Color("red"))
#         layout.addWidget(Color("green"))
#         layout.addWidget(Color("yellow"))
#         layout.addWidget(Color("blue"))
#         widget = QWidget()
#         widget.setLayout(layout)
        
#         self.setCentralWidget(widget)
        
#         toolbar = QToolBar("My Main Toolbar")
#         toolbar.setIconSize(QSize(16,16)) # ? Sets icon size
#         self.addToolBar(toolbar)
        
#         button_action = QAction(QIcon("cookie.png"), "Your Button", self) # * sets the button to an icon pic
        
#         button_action.setStatusTip("This is your cookie")
#         button_action.triggered.connect(self.onMyToolBarButtonClick)
#         button_action.setCheckable(True) # ! Makes the button toggleable
#         toolbar.addAction(button_action) 
        
#         button_action.setShortcut(QKeySequence("Ctrl+p")) # ! keyboard shortcut
#         toolbar.addAction(button_action)                     
        
#         toolbar.addSeparator() # ? Adds line in the menu to separate components
        
#         button_action2 = QPushButton("shit")
        
#         button_action2.setStatusTip("Who Took a Bite???????")
#         # button_action2.triggered.connect(self.onMyToolBarButtonClick)
#         button_action2.clicked.connect(self.onMyToolBarButtonClick) # ! Button action after click
#         # toolbar.addAction(button_action2)
        
#         self.setStatusBar(QStatusBar(self))
        
#         menu = self.menuBar()
        
#         file_menu = menu.addMenu("&Cunt")
#         file_menu.addAction(button_action)
#         file_menu.addAction(button_action2)  
    
#     def onMyToolBarButtonClick(self, s):
#         print("monch", s)
        
def main():
    
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()


if __name__ == '__main__':
    main()

# ! app = QApplication(sys.argv)

# ! window = MainWindow()
# ! window.show()

# ! app.exec_()