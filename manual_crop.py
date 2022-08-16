import cv2
import numpy as np

def manual_crop(event,x,y,flags,param):
    global x_start, y_start, x_end, y_end, cropping

    im = param[0]
    cropping = param[1]

    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x,y,x,y
        cropping = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        x_end,y_end = x,y
        cropping = False

        refPoint = [(x_start,y_start),(x_end,y_end)]

        if len(refPoint) == 2:
            roi = im[refPoint[0][1]:refPoint[1][1],refPoint[0][0]:refPoint[1][0]]
            cv2.imshow("Cropped",roi)
            cv2.imwrite("./data/test.jpg",roi)


    