# Imports
import os
#import cv2
import time

from anyio import current_default_worker_thread_limiter
import main # Code frontend
import random
import numpy as np
import pandas as pd

# Defines the size of the dataset to be created
dataset_size = 1000
current_dataset_size = 0

# Base directory path
base_directory = os.path.dirname(os.path.abspath("__file__"))
os.chdir(base_directory)

# Directory paths for images
images_path = "./images"

# Makes sure that the images are available to use
images = False
if os.path.exists(images):
    images = True

m_or_f = 0 # man images = 1, woman images = 2; 0 is default and must be set before traversing directory paths
man_images = "/man/"
man_image_position = 0 # Counts file position in directory
woman_images = "/woman/"
woman_image_position = 0 # Counts file position in directory

man_file_names = pd.DataFrame()
woman_file_names = pd.DataFrame()

man_path = images_path + man_images
woman_path = images_path + woman_images

# DataFrame for collecting input results for image classification
dataset = pd.DataFrame(columns = ['image', 'gender', 'classification'])

# Does a coin flip to determine if a male or female image will appear next
# Additionally, this then changes the directory path to match the outcome of the coin flip
def directory_path():
    
    # Does the coin flip and creates new path string based on outcome
    def cointoss():
        global outcome
        outcome = random.randint(0,1)
        print(outcome)
        if outcome == 0:
            # self.current_location = os.path.join(images, man_images)
            current_location = images_path + man_images
            m_or_f = 1
        elif outcome == 1:
            # self.current_location = os.path.join(images, woman_images)
            current_location = images_path + woman_images
            m_or_f = 2
        # else:
            # ! Not yet implemented in frontend
            # main.errorEvent()
            # self.current_location = images #placeholder
        return current_location
        
    # Changes file directory based on coin flip outcome
    def filepath(directory_location):
        global new_location
        new_location = directory_location
        os.chdir(new_location) # changes active directory
        return new_location

    # Does coin toss and changes directory path to reflect coin toss outcome
    random_directory_change = filepath(cointoss())
    
def file_traversal():
    
    def change_path():
        directory_path()
        
    def image_names():
        is_image = ".jpg"

        global count
        count = 0
        # print(man_path)
        for subdir, dirs, files in os.walk(man_path):
            for file in files:
                if is_image in file.lower():
                    dataset.loc[count, 'image'] = file
                    dataset.loc[count, 'gender'] = "male"
                    count += 1

        for subdir, dirs, files in os.walk(woman_path):
            for file in files:
                if is_image in file.lower():
                    dataset.loc[count, 'image'] = file
                    dataset.loc[count, 'gender'] = "female"
                    count += 1

        test = image_names()
        print(dataset)
        
file_traversal()

            



