import cv2
import numpy as np
img=cv2.imread('photos/cat.jpg')
blank=np.zeros(img.shape[:2],dtype='uint8')
mask=cv2.circle(blank,(img.shape[1]//2+45,img.shape[0]//2),100,255,-1)
masked=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('mask',masked)
cv2.waitKey(0)
cv2.destroyAllWindows()