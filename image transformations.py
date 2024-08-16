import cv2 as cv
import numpy as np

img=cv.imread('photos/th.jpeg')
cv.imshow("photo",img)
h, w=img.shape[:2] 
center=(w//2,h//2)
ct=cv.getRotationMatrix2D(center,-65,0.5)
rotated=cv.warpAffine(img,ct,(w,h))
cv.imshow("photo rpotted",rotated)
flip=cv.flip(img,-1)
cv.imshow("photo rpotted",flip)
cv.waitKey(0)

