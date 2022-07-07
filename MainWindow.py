
#? A dataset creation tool.
#?
#?   ,-.       _,---._ __  / \
#?  /  )    .-'       `./ /   \
#? (  (   ,'            `/    /|
#?  \  `-"             \'\   / |
#?   `.              ,  \ \ /  |
#?    /`.          ,'-`----Y   |
#?   (            ;        |   '
#?   |  ,-.    ,-'  Connor |  /
#?   |  | (   |   Contursi | /
#?   )  |  \  `.___________|/
#?   `--'   `--'

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

from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys

from PIL import Image
# global variables for the current image number [progress], and the number of images [images]
# * ================================================
class ButtonGroup(QtCore.QObject):
    trigger = QtCore.pyqtSignal((),(bool,))
    
    def addButton(self, button):
        button.clicked.connect(self.trigger.emit)
        
    def removeButton(self, button):
        button.clicked.disconnect(self.trigger.emit)
# * ================================================

class MainWindow(QMainWindow):
    # root_directory = os.path.dirname(os.path.abspath("__file__"))
    # image_directory = os.path.join(root_directory, "images/")
    # mylist = os.listdir(image_directory)
    global images, progression, W, H, inputResults
    images = 1000
    progression = 0
    W = 6
    H = images - 1
    # ! 1 is toggled, 0 is not toggled
    inputResults = [[0 for x in range(W)] for y in range(H)]
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        global root_directory
        global image_directory
        # Source path for application
        root_directory = os.path.dirname(os.path.abspath("__file__"))
        # Source path for image files
        image_directory = os.path.join(root_directory, "image_data\\")
        # Source path for GUI icons
        iconPath = os.path.join(root_directory, "icons\\")
        
        # ? Loads splash screen that stays persistent till the program is finished starting up
        pic = QPixmap(os.path.join(iconPath, "cookies_jar.png"))
        pix = pic.scaled(400, 400, QtCore.Qt.KeepAspectRatio) # Scales the splash screen down to 300px * 300px
        splash = QSplashScreen(pix)
        splash.show()                
        
        # Creates global variables that get the number of images and keep track of which file in the directory is being accessed
        global images
        global progression
        images = len(os.listdir(image_directory)) # Counts the number of files in the image directory
        progression = 0
        
        # * ----------------
        # * collects inputs for each image [globally] and stores them in a 2D array
        # ! 1 is toggled, 0 is not toggled
        global inputResults
        inputResults = [[0 for x in range(W)] for y in range(H)]
        # * ----------------
        
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
        self.image_files = os.listdir(image_directory)
        print(self.image_files)
        windowIcon = os.path.join(iconPath, 'cookie.png')
        iconWin = QtGui.QIcon(windowIcon)
        self.setWindowIcon(iconWin)
        self.setWindowTitle("Dataset Label Creator")
        self.setMinimumSize(QSize(800, 535))
        self.setMaximumSize(QSize(1500, 1000))
        
        # ? Creates QLabel for the images from the dataset which will be displayed
        
        self.image = QLabel("Data")
        # self.updateData()
        # self.ontoNext()
        
        # ! Creates button group to control the buttons!
        # ! ==========================
        self.group = QButtonGroup()
        self.group.setExclusive(False)
        # ! ==========================
        
        # ! -----------------------------------------------------------------------------
        # ! Creates all of the toggle buttons based on input [keyboard shortcuts included]
        # ? =============================================================================
        self.she = AnimatedToggle(checked_color="#e6382c", pulse_checked_color="#bfbfbf") # Red, Grey
        self.she.setChecked(False)
        self.she.setShortcut(QKeySequence("Left"))
        self.she.setStatusTip("Use 'Left Arrow' to toggle")
        self.group.addButton(self.she)
        self.she.toggled.connect(self.sheData)
        #   --------------------------------------
        self.her = AnimatedToggle(checked_color="#e6732c", pulse_checked_color="#bfbfbf") # Orange, Grey
        self.her.setChecked(False)
        self.her.setShortcut(QKeySequence("Shift+Left"))
        self.her.setStatusTip("Use 'Shift+Left Arrow' to toggle")
        self.group.addButton(self.her)
        self.her.toggled.connect(self.herData)
        # ? =============================================================================
        self.he = AnimatedToggle(checked_color="#ebd82f", pulse_checked_color="#bfbfbf") # Yellow, Grey
        self.he.setChecked(False)
        self.he.setShortcut(QKeySequence("Down"))
        self.he.setStatusTip("Use 'Down Arrow' to toggle")
        self.group.addButton(self.he)
        self.he.toggled.connect(self.heData)
        #   --------------------------------------       
        self.him = AnimatedToggle(checked_color="#3ac25f", pulse_checked_color="#bfbfbf") # Green, Grey
        self.him.setChecked(False)
        self.him.setShortcut(QKeySequence("Shift+Down"))
        self.him.setStatusTip("Use 'Shift+Down Arrow' to toggle")
        self.group.addButton(self.him)
        self.him.toggled.connect(self.himData)
        # ? =============================================================================
        self.they = AnimatedToggle(checked_color="#2f5eeb", pulse_checked_color="#bfbfbf") # Blue, Grey
        self.they.setChecked(False) 
        self.they.setShortcut(QKeySequence("Right"))
        self.they.setStatusTip("Use 'Right Arrow' to toggle")
        self.group.addButton(self.they)
        self.they.toggled.connect(self.theyData)
        #   --------------------------------------        
        self.them = AnimatedToggle(checked_color="#612feb", pulse_checked_color="#bfbfbf") # Purple, Grey
        self.them.setChecked(False) 
        self.them.setShortcut(QKeySequence("Shift+Right"))
        self.them.setStatusTip("Use 'Shift+Down Arrow' to toggle")
        self.group.addButton(self.them)
        self.them.toggled.connect(self.themData)
        # ? =============================================================================       
        # ! -----------------------------------------------------------------------------
        
        # ? Submits button states and moves onto the next image for labeling 
        self.next = QPushButton('Submit', self)
        self.next.setShortcut(QKeySequence("Space"))
        self.next.setStatusTip("Use 'Enter' to submit label and go to next image")
        self.group.addButton(self.next)
        self.next.clicked.connect(self.ontoNext)
        
        # * Creates the progress bar and limits it for the number of images that will be processed;
        # * Additionally, it doesn't keep track via percentage, it displays the number of completed,
        # * labels compared to the total number of images that need labels
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(0, 0, 300, 25)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setFormat("%v/%m")
        self.progressBar.setMaximum(images) 
        
        # ! All layouts needed to be arranged for the GUI
        base_layout = QHBoxLayout()
        image_layout = QVBoxLayout()
        buttons_layout = QVBoxLayout()
        submit_layout = QVBoxLayout()
        
        # ? Buttons added to the GUI layout to be displayed
        buttons_layout.addWidget(self.image)
        buttons_layout.addWidget(self.she)
        buttons_layout.addWidget(self.her)
        buttons_layout.addWidget(self.he)
        buttons_layout.addWidget(self.him)
        buttons_layout.addWidget(self.they)
        buttons_layout.addWidget(self.them)
        buttons_layout.addWidget(self.next)
              
        # * Adds status bar at bottom for tips
        self.setStatusBar(QStatusBar(self))
        
        base_layout.addLayout(buttons_layout)
        widget = QWidget()
        widget.setLayout(base_layout)
        self.setCentralWidget(widget)
        
        # * Adds tool bar at top
        toolbar = QToolBar("Cookie Bakery")
        self.addToolBar(toolbar)
        
        splash.finish(self) #Closes splash screen after successful launch
        self.show()

# ! 1 is toggled, 0 is not toggled 
# ? =============================
# ! She/Her             
    def sheData(self, s):
        global inputResults
        if(s):
            inputResults[0][progression] = 1
            # print("True")
#   -----------------------------            
    def herData(self, s):
        if(s):
            inputResults[1][progression] = 1
            # print("True")
# ? =============================     
# ! He/Him            
    def heData(self, s):
        if(s):
            inputResults[2][progression] = 1
            # print("True")
#   -----------------------------            
    def himData(self, s):
        if(s):
            inputResults[3][progression] = 1
            # print("True")
# ? =============================      
# ! They/Them            
    def theyData(self, s):
        if(s):
            inputResults[4][progression] = 1
            # print("True")
#   -----------------------------            
    def themData(self, s):
        if(s):
            inputResults[5][progression] = 1
            # print("True")
# ? =============================   
        
# * -----------------------------    
    def updateData(self):
        # print("dumb")
        global progression
        # file = self.image_files[progression]
        da = os.path.join(image_directory, self.image_files[progression])
        tab = Image.open(str(da))
        image.setPixmap(QPixmap("C:\\Users\\indie\\Desktop-Dataset-Creation\\image_data\\00000001.jpg"
))
        image.setScaledContents(True)
        # Increments progress bar         

# * -----------------------------        
    def ontoNext(self, s):
        global progression
        global images
        
        for button in self.group.buttons():
            if button is not s:
                button.setChecked(False)
        
        # if progression <= images:
        #     self.progressBar.setValue(progression)
        
        self.updateData()
        progression += 1

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
    
# ! ~ Original starter code for the GUI ~
# ! app = QApplication(sys.argv)
# ! window = MainWindow()
# ! window.show()
# ! app.exec_()