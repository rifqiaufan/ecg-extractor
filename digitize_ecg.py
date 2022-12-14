from unicodedata import digit
import numpy as np
import cv2
from skimage.morphology import skeletonize
import pandas as pd
import os


def digitize_ecg(input_path,output_path='./'):
    im = cv2.imread(input_path)
    
    im_gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    bw = cv2.threshold(im_gray, 127, 255, cv2.THRESH_BINARY)
    bw = bw[1].astype(bool)
    skeleton = skeletonize(bw)

    value1 = []
    value2 = []
    for pos in range(len(skeleton[0,:])):
        if np.sum(skeleton[:,pos] == True)>1:
            value1.append(np.min(np.where(skeleton[:,pos] == True)[0]))
            value2.append(np.max(np.where(skeleton[:,pos] == True)[0]))
        elif np.sum(skeleton[:,pos] == True) == 0:
            continue
        else:
            value1.append(np.where(skeleton[:,pos] == True)[0][0])
            value2.append(np.where(skeleton[:,pos] == True)[0][0])

    value1 = np.array(value1)*-1
    value2 = np.array(value2)*-1
    ecg_digitize = pd.DataFrame({
        'x':np.arange(0,len(value1)),
        'y':value1
    })
    ecg_digitize2 = pd.DataFrame({
        'x':np.arange(0,len(value2)),
        'y':value2
    })

    boundary_up = np.mean(ecg_digitize2['y']) + 2*np.std(ecg_digitize2['y'])
    boundary_down = np.mean(ecg_digitize2['y']) - 2*np.std(ecg_digitize2['y'])
    update_ecg_digitize2 = ecg_digitize2.loc[ecg_digitize2['y'] > boundary_down,:]

    file_name = input_path.split('/')[-1]
    file_name = file_name.split('.')[0] + '.csv'
 
    update_ecg_digitize2.to_csv(os.path.join(output_path,file_name),index=False)

    return

# digitize_ecg('./output/ecg_test.jpg','./output_digitize')