import cv2 as cv 
img=cv.imread('photos/th.jpeg')
cv.imshow("CANY",img)
canny=cv.Canny(img,125,175)
cv.imshow("CANY",canny)
dilated=cv.dilate(canny,(3,3),iterations=4)
cv.imshow("CANY",dilated)

cv.waitKey(0)