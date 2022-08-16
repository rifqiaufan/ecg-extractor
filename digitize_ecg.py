from unicodedata import digit
import numpy as np
import cv2


def digitize_ecg(input_path,output_path='./'):
    im = cv2.imread(input_path)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    

    row,col = np.shape(im)
    threshold_im = np.array([255 if px>200 else 0 for px in im.reshape(1,-1)[0]])
    threshold_im = threshold_im.reshape(row,col)
    threshold_im = threshold_im.astype(np.uint8)

    print(threshold_im)
   
    print("input size: "+str(np.shape(im)))
    print("output size: "+str(np.shape(threshold_im)))

    # cv2.imshow("Threshold",threshold_im)
    # cv2.waitKey(0)


    return

digitize_ecg('./output/ecg_test.jpg')