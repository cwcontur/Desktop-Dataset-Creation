
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
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5 import QtGui
# from matplotlib import image
from pydantic import root_validator
from qtwidgets import Toggle, AnimatedToggle

from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
from QSwitchControl import SwitchControl
# from PIL import Image
# global variables for the current image number [progress], and the number of images [images]

# class QHSeperationLine(QtWidgets.QFrame):
#   '''
#   a horizontal seperation line\n
#   '''
#   def __init__(self):
#     super().__init__()
#     self.setMinimumWidth(1)
#     self.setFixedHeight(20)
#     self.setFrameShape(QtWidgets.QFrame.HLine)
#     self.setFrameShadow(QtWidgets.QFrame.Sunken)
#     self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
#     return

# * ================================================
class ButtonGroup(QtCore.QObject):
    trigger = QtCore.pyqtSignal((),(bool,))
    
    def addButton(self, button):
        button.clicked.connect(self.trigger.emit)
        
    def removeButton(self, button):
        button.clicked.disconnect(self.trigger.emit)
# * ================================================
class MainWindow(QMainWindow):
    # Default path
    root_directory = os.path.dirname(os.path.abspath("__file__"))
    
    global images, progression, clickCounter
    images = 0
    progression = 0
    clickCounter = 0
    
    global iconPath
    iconPath = os.path.join(root_directory, "icons\\")

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
        pic = QPixmap(os.path.join(iconPath, "cookie_splash.png"))
        pix = pic.scaled(300, 300, QtCore.Qt.KeepAspectRatio) # Scales the splash screen down to 300px * 300px
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
        Rows = images
        inputResults = np.empty((Rows, 6))
        # * ----------------
        
        # Array of zeroes with a place for each image
        global mylist
        mylist = np.empty(images)
        
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

        windowIcon = os.path.join(iconPath, 'cookie.png')
        iconWin = QtGui.QIcon(windowIcon)
        self.setWindowIcon(iconWin)
        self.setWindowTitle("Dataset Label Creator")
        self.setFixedHeight(650)
        self.setFixedWidth(650)        
        
        # ? Creates QLabel for the images from the dataset which will be displayed
        self.imageDisp = QLabel(self)
        self.imageDisp.setFixedWidth(400)
        self.imageDisp.setFixedHeight(533)

        # ! Displays the first image when program is loaded
        currentImage = os.path.join(image_directory, self.image_files[progression])
        pixmap = QPixmap(currentImage)
        self.imageDisp.setPixmap(pixmap)
        self.imageDisp.setScaledContents(True)
        self.imageDisp.setMinimumSize(QSize(100, 300))
        self.imageDisp.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        # ! Creates button group to control the buttons!
        # ! ==========================
        self.group = QButtonGroup()
        self.group.setExclusive(False)
        # ! ==========================
        
        # ! -----------------------------------------------------------------------------
        # ! Creates all of the toggle buttons based on input [keyboard shortcuts included]
        # ? =============================================================================
        self.she = AnimatedToggle(checked_color="#e6382c", pulse_checked_color="#bfbfbf") # Red, Grey
        self.she.setFixedHeight(50)
        self.she.setChecked(False)
        self.she.setShortcut(QKeySequence("Left"))
        self.she.setStatusTip("Use 'Left Arrow' to toggle")
        self.group.addButton(self.she)
        self.she.toggled.connect(self.sheData)
        sheLabel = QLabel("She")
        sheLabel.setFont(QFont("SF", 12))
        sheLabel.setAlignment(Qt.AlignCenter)
        #   --------------------------------------
        self.her = AnimatedToggle(checked_color="#e6732c", pulse_checked_color="#bfbfbf") # Orange, Grey
        self.her.setChecked(False)
        self.her.setShortcut(QKeySequence("Shift+Left"))
        self.her.setStatusTip("Use 'Shift+Left Arrow' to toggle")
        self.group.addButton(self.her)
        self.her.toggled.connect(self.herData)
        herLabel = QLabel("Her")
        herLabel.setFont(QFont("SF", 12))
        herLabel.setAlignment(Qt.AlignCenter)
        # ? =============================================================================
        self.he = AnimatedToggle(checked_color="#ebd82f", pulse_checked_color="#bfbfbf") # Yellow, Grey
        self.he.setChecked(False)
        self.he.setShortcut(QKeySequence("Down"))
        self.he.setStatusTip("Use 'Down Arrow' to toggle")
        self.group.addButton(self.he)
        self.he.toggled.connect(self.heData)
        heLabel = QLabel("He")
        heLabel.setFont(QFont("SF", 12))
        heLabel.setAlignment(Qt.AlignCenter)
        #   --------------------------------------       
        self.him = AnimatedToggle(checked_color="#3ac25f", pulse_checked_color="#bfbfbf") # Green, Grey
        self.him.setChecked(False)
        self.him.setShortcut(QKeySequence("Shift+Down"))
        self.him.setStatusTip("Use 'Shift+Down Arrow' to toggle")
        self.group.addButton(self.him)
        self.him.toggled.connect(self.himData)
        himLabel = QLabel("Him")
        himLabel.setFont(QFont("SF", 12))
        himLabel.setAlignment(Qt.AlignCenter)
        # ? =============================================================================
        self.they = AnimatedToggle(checked_color="#2f5eeb", pulse_checked_color="#bfbfbf") # Blue, Grey
        self.they.setChecked(False) 
        self.they.setShortcut(QKeySequence("Right"))
        self.they.setStatusTip("Use 'Right Arrow' to toggle")
        self.group.addButton(self.they)
        self.they.toggled.connect(self.theyData)
        theyLabel = QLabel("They")
        theyLabel.setFont(QFont("SF", 12))
        theyLabel.setAlignment(Qt.AlignCenter)        
        #   --------------------------------------        
        self.them = AnimatedToggle(checked_color="#612feb", pulse_checked_color="#bfbfbf") # Purple, Grey
        self.them.setChecked(False) 
        self.them.setShortcut(QKeySequence("Shift+Right"))
        self.them.setStatusTip("Use 'Shift+Down Arrow' to toggle")
        self.group.addButton(self.them)
        self.them.toggled.connect(self.themData)
        themLabel = QLabel("Them")
        themLabel.setFont(QFont("SF", 12))
        themLabel.setAlignment(Qt.AlignCenter)         
        # ? =============================================================================               
        # ? Submits button states and moves onto the next image for labeling 
        self.next = QPushButton('Submit', self)
        self.next.setFixedWidth(200)
        self.next.setFixedHeight(35)
        self.next.setShortcut(QKeySequence("Space"))
        self.next.setStatusTip("Use 'Space' to submit label and go to next image")
        self.next.clicked.connect(self.ontoNext)
        
        # * Creates the progress bar and limits it for the number of images that will be processed;
        # * Additionally, it doesn't keep track via percentage, it displays the number of completed,
        # * labels compared to the total number of images that need labels
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(0, 0, 300, 25)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setFormat("%v/%m")
        self.progressBar.setMaximum(images) 
        self.progressBar.setValue(progression)
        
        # ! All layouts needed to be arranged for the GUI
        base_layout = QHBoxLayout()
        base_layout.setSpacing(0)
        image_layout = QVBoxLayout()
        image_layout.setSpacing(0)
        self.buttons_layout = QVBoxLayout()
        self.buttons_layout.setSpacing(0)
        self.buttons_layout.setContentsMargins(10, -20, 10, 0)        

       # ! Buttons added to the GUI layout to be displayed
       # ! ====================================
        image_layout.addWidget(self.imageDisp)
        
        self.buttons_layout.addWidget(sheLabel)
        self.buttons_layout.addWidget(self.she)
        self.separatorLines()

        self.buttons_layout.addWidget(herLabel)
        self.buttons_layout.addWidget(self.her)
        self.separatorLines()

        self.buttons_layout.addWidget(heLabel)
        self.buttons_layout.addWidget(self.he)
        self.separatorLines()

        self.buttons_layout.addWidget(himLabel)
        self.buttons_layout.addWidget(self.him)
        self.separatorLines()
        
        self.buttons_layout.addWidget(theyLabel)
        self.buttons_layout.addWidget(self.they)
        self.separatorLines()
        
        self.buttons_layout.addWidget(themLabel)
        self.buttons_layout.addWidget(self.them)
        
        self.buttons_layout.addWidget(self.next)
        self.buttons_layout.setAlignment(Qt.AlignCenter)
        # ? ============================================
        
        # * Adds status bar at bottom for tips
        self.statusbar = self.statusBar()
        self.statusbar.addPermanentWidget(self.progressBar)
        
        base_layout.addLayout(image_layout)
        base_layout.addLayout(self.buttons_layout)
        
        widget = QWidget()
        widget.setLayout(base_layout)
        self.setCentralWidget(widget)
        
        # * Adds tool bar at top
        toolbar = QToolBar("Cookie Bakery")
        toolbar.setIconSize(QSize(32, 32))
        self.addToolBar(toolbar)
        
        undoIcon = os.path.join(iconPath, 'arrow-curve-180-left.png')
        goBack = QAction(QIcon(undoIcon), "Go Back", self)
        goBack.setStatusTip("Go back and re-label last image")
        goBack.triggered.connect(self.goBackNow)
        toolbar.addAction(goBack)
        
        splash.finish(self) #Closes splash screen after successful launch
        self.show()

    # * Creates separator lines between toggle buttons
    def separatorLines(self):
        line = QFrame()
        line.setGeometry(QRect(60, 110, 751, 20))
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.buttons_layout.addWidget(line)

# ! 1 is toggled, 0 is not toggled 
# ? =============================
# ! She/Her             
    def sheData(self, s):
        global clickCounter
        if(s):
            inputResults[progression][0] = 1
            clickCounter += 1
#   -----------------------------            
    def herData(self, s):
        global clickCounter
        if(s):
            clickCounter += 1
            inputResults[progression][1] = 1
# ? =============================     
# ! He/Him            
    def heData(self, s):
        global clickCounter
        if(s):
            clickCounter += 1
            inputResults[progression][2] = 1
#   -----------------------------            
    def himData(self, s):
        global clickCounter
        if(s):
            clickCounter += 1
            inputResults[progression][3] = 1
# ? =============================      
# ! They/Them            
    def theyData(self, s):
        global clickCounter
        if(s):
            clickCounter += 1
            inputResults[progression][4] = 1
#   -----------------------------            
    def themData(self, s):
        global clickCounter
        if(s):
            clickCounter += 1
            inputResults[progression][5] = 1
# ? =============================   
        
# * -----------------------------
# * Updates the image displayed + increments the progress bar
# * -----------------------------    
    def updateData(self):
        # Resets button state tracking
        global clickCounter
        clickCounter = 0
        
        global progression
        # Displays + updates image to be labeled
        currentImage = os.path.join(image_directory, self.image_files[progression + 1])
        pixmap = QPixmap(currentImage)
        self.imageDisp.setPixmap(pixmap)
        self.imageDisp.setScaledContents(True)
        self.imageDisp.setMinimumSize(QSize(100, 300))
        self.imageDisp.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        
        # Increments progress bar         
        progression += 1
        if progression <= images:
            self.progressBar.setValue(progression)
# * -----------------------------
# * Goes onto the next image for labeling 
# * -----------------------------         
    def ontoNext(self, s):
        global progression
        global images

        # Unchecks all radio buttons for fresh state when next image is shown
        for button in self.group.buttons():
            if button is not s:
                button.setChecked(False)

        # Displays an error if no buttons are toggled
        if clickCounter == 0: 
            self.userError()   
        else:
            self.updateData()
# * -----------------------------
# * Lets the user go back and redo the label for the last image
# * -----------------------------           
    def goBackNow(self):
        global progression
        # Displays and undoes label for last image to be labeled
        if progression > 0:
            currentImage = os.path.join(image_directory, self.image_files[progression-1])
            pixmap = QPixmap(currentImage)
            self.imageDisp.setPixmap(pixmap)
            self.imageDisp.setScaledContents(True)
            self.imageDisp.setMinimumSize(QSize(100, 300))
            self.imageDisp.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
            
            # Decrements progress counter and bar
            progression -= 1
            self.progressBar.setValue(progression)
# * ----------------------------- 
# * Opens dialogue box when no options have been selected, but the 'submit' button was used
# * ----------------------------- 
    def userError(self):
        global iconPath
        errorWindow = QMessageBox(self)
        errorWindow.setWindowTitle("Whoa there!")
        errorWindow.setText("You have to make at least one selection!")
        errorWindow.setStandardButtons(QMessageBox.Ok)
        errorIcon = os.path.join(iconPath, 'brain--exclamation.png')
        errorWindow.setIcon(QMessageBox.Warning)
        button = errorWindow.exec_()
        
        if button == QMessageBox.Ok:
            errorWindow.close()
# * ============================
# ! ============================
def main():
    
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()


if __name__ == '__main__':
    main()
# ! ============================
# ! ~ Original starter code for the GUI ~
# ! app = QApplication(sys.argv)
# ! window = MainWindow()
# ! window.show()
# ! app.exec_()