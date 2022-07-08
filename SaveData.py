import numpy as np
import pandas as pd
# ---------------------------------------------- #
# Image_Manipulation
# ---------------------------------------------- #
import os
# ---------------------------------------------- #

class saveDataLabels(data, files):

    def saveData(data, files):
        # Creates new csv and deletes previous version if it's still in existence
        if os.path.exists("./SaveData.csv"):  # File path in current directory
            os.remove("SaveData.csv")  # Deletes files [if exists]

        data.to_csv("SaveData.csv")  # Saves data to .csv

        # Checks file size just to make sure that it's not empty
        file_size = os.path.getsize("SaveData.csv")
        kb = round(file_size / 1024, 1)  # Kilobytes
        print("File size:", kb, "kb")
        
    def loadData(data, files):
        

