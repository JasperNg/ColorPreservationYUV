import cv2
import skimage.io
import numpy as np
import sys

img = skimage.io.imread('ContentImage')
img2 = skimage.io.imread('StylizedImage')
yuv = cv2.cvtColor(np.float32(img), cv2.COLOR_RGB2YUV)
y, u, v = cv2.split(yuv)
yuv2 = cv2.cvtColor(np.float32(img2), cv2.COLOR_RGB2YUV)
h, j, k = cv2.split(yuv2)
img2 = np.dstack((h,u,v))
img2 = cv2.cvtColor(np.float32(img2), cv2.COLOR_YUV2BGR)
cv2.imwrite( "final.jpg", img2);
