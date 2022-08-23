from genericpath import isfile
from ntpath import join
import cv2
import numpy as np
import os

def batch_crop(x,y,input_path,output_path):
    refPoint = [(x[0],y[0]),(x[1],y[1])]
    path = input_path
    working_files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path,file))]
    working_files = [file for file in working_files if not file.startswith('.')] 

    for file in working_files:
        im = cv2.imread(os.path.join(path,file))
        
        roi = im[refPoint[0][1]:refPoint[1][1],refPoint[0][0]:refPoint[1][0]]

        output_name = str.split(file,'.')
        cv2.imwrite(os.path.join(output_path,output_name[0]+".jpg") ,roi)
        


# quick test
# batch_crop([50,800],[100,190],'./data','./output')