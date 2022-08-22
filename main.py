import argparse
from genericpath import isfile
import cv2
import os
import numpy as np
from cv2 import CAP_PROP_PVAPI_BINNINGX
from batch_crop import batch_crop
from manual_crop import manual_crop
# from batch_crop import batch_crop
from digitize_ecg import digitize_ecg
import argparse

parser = argparse.ArgumentParser(description='Extract ECG data from image/screenshot')
parser.add_argument('path', help='path to image/folder')
parser.add_argument('--batch', default=False, action='store_true', help='running in batch')
args = parser.parse_args()

print("""
ECG EXTRACTOR \n
Manual/batch processing supported \n
- batch processing only work for consistent image size and layout
- more features to come ...

""")


if args.batch != True:
    im_path = args.path
    if os.path.isfile(im_path):
        im = cv2.imread(im_path)
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

        digitize_ecg('./output/ecg_test.jpg','./output_digitize')
    else:
        print('Please select the correct file path')

elif args.batch == True:
    if ~os.path.isfile(args.path):
        try:
            batch_crop([50,800],[100,190],args.path,'./output')
            working_output = os.listdir('./output')
            working_output = [file for file in working_output if not file.startswith('.')]
            for i in range(len(working_output)):
                digitize_ecg(os.path.join('./output',working_output[i]),'./output_digitize')
        except:
            print("Something goes wrong")
    else:
        print("Please select the correct working folder")

print("Extraction completed!")

    



# while True:
#     mode = input("manual/batch? ") or "manual"

#     if str.lower(mode) == "manual":
#         path = args.path
#         im = cv2.imread(path)
#         im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#         # coordinate start from top left (0,0)
#         cropping = False
#         x_start, y_start, x_end, y_end = 0, 0, 0, 0

#         param = [im, cropping]

#         # load and extract ecg data
#         cv2.namedWindow("image")
#         cv2.setMouseCallback("image", manual_crop,param)

#         # drawing rectangle
#         i = im.copy()
#         if not cropping:
#             cv2.imshow("image", i)

#         elif cropping:
#             cv2.rectangle(i, (x_start, y_start), (x_end, y_end),(0,255,0),5)
#             cv2.imshow("image",i)

#         cv2.waitKey(0)
#         print(i.shape)
#         break

#     elif str.lower(mode) == "batch":
#         batch_crop([50,800],[100,190],'./data','./output')
#         digitize_ecg('./output/ecg_test.jpg','./output_digitize')
#         break

#     elif str.lower(mode) == "q":
#         print("Quit")
#         break
#     else:
#         print("Mode not recognized!\n")







