import cv2
import numpy as np
from cv2 import CAP_PROP_PVAPI_BINNINGX
from manual_crop import manual_crop
from batch_crop import batch_crop

mode = input("manual/batch? ") or "manual"

if str.lower(mode) == "manual":

    path = "./data/ecg_test.JPG"
    im = cv2.imread(path)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # coordinate start from top left (0,0)
    cropping = False
    x_start, y_start, x_end, y_end = 0, 0, 0, 0

    param = [im, cropping]

    # load and extract ecg data
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", manual_crop,param)

    # drawing rectangle
    i = im.copy()
    if not cropping:
        cv2.imshow("image", i)

    elif cropping:
        cv2.rectangle(i, (x_start, y_start), (x_end, y_end),(0,255,0),5)
        cv2.imshow("image",i)

    cv2.waitKey(0)
    print(i.shape)

elif str.lower(mode) == "batch":
    batch_crop([50,800],[100,190],'./data','./output')

else:
    print("Mode not recognized!")





