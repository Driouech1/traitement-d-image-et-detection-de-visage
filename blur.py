import cv2 as cv 

img=cv.imread('photos/1.jpeg')
cv.imshow("image",img)
blur=cv.GaussianBlur(img,(7,7),sigmaX=8,sigmaY=4, borderType=cv.BORDER_DEFAULT)
cv.imshow("blur",blur)
cv.waitKey(0)
