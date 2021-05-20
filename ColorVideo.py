import cv2
import skimage.io
import numpy as np
import sys
import os
from os.path import isfile, join

count = 1
epath = "FinalFramesDir"
imgdir = os.listdir('ContentFramesDir')
while count <= len(imgdir):
    img = skimage.io.imread("ContentFramesDir"+str(count)+".jpg")
    img2 = skimage.io.imread("StyleFramesDir"+str(count)+".jpg")
    yuv = cv2.cvtColor(np.float32(img), cv2.COLOR_RGB2YUV)
    y, u, v = cv2.split(yuv)
    yuv2 = cv2.cvtColor(np.float32(img2), cv2.COLOR_RGB2YUV)
    h, j, k = cv2.split(yuv2)
    img3 = np.dstack((h,u,v))
    img3 = cv2.cvtColor(np.float32(img3), cv2.COLOR_YUV2BGR)
    cv2.imwrite( os.path.join(epath , "final"+str(count)+".jpg"), img3);
    del y
    del u
    del v
    del h
    del j
    del k
    count = count + 1
