import cv2
import skimage.io
import numpy as np
import sys
import os
from os.path import isfile, join

count = 1
index = 0
carr = [] #content image name array
sarr = [] #style image name array
epath = "" #Output frames dir
imgdir = os.listdir('') #content frames dir

for img in os.listdir(""): #content frames dir
    carr.append(img)
    print(carr)

for img in os.listdir(""): #style frames dir
    sarr.append(img)
    print(sarr)

while count <= len(imgdir):
    img = skimage.io.imread("" + str(carr[index])) #content frames dir
    img2 = skimage.io.imread("" + str(sarr[index])) #style frames dir
    yuv = cv2.cvtColor(np.float32(img), cv2.COLOR_RGB2YUV)
    y, u, v = cv2.split(yuv)
    yuv2 = cv2.cvtColor(np.float32(img2), cv2.COLOR_RGB2YUV)
    h, j, k = cv2.split(yuv2)
    img3 = np.dstack((h, u, v))
    img3 = cv2.cvtColor(np.float32(img3), cv2.COLOR_YUV2BGR)
    cv2.imwrite(os.path.join(epath, str(count) + ".png"), img3);
    del y
    del u
    del v
    del h
    del j
    del k
    count = count + 1
    index = index + 1
