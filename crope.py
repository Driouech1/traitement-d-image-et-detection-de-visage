import cv2 as cv

img=cv.imread('photos/th (3).jpeg')
cv.imshow('th (3)',img)
crope=img[70:200, 70:400]
cv.imshow('cr7',crope)
cv.waitKey(0)


