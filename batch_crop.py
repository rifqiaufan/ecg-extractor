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
        # convert to hsv than apply mask to thershold ecg
        hsv = cv2.cvtColor(roi , cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))
        imask = mask>0
        green = np.zeros_like(roi, np.uint8)
        green[imask] = roi[imask]

        output_name = str.split(file,'.')
        cv2.imwrite(os.path.join(output_path,output_name[0]+".jpg") ,green)
        


# quick test
# batch_crop([50,800],[100,190],'./data','./output')