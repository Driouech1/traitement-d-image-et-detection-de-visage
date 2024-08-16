import cv2 as cv 
import matplotlib.pyplot as plt
img=cv.imread('photos/1.jpeg')
cv.imshow('Gray',img)
plt.imshow(img)
plt.show()

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('Gray',hsv)

lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('Gray',lab)
 
BGR=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('Gray',BGR)
cv.waitKey(0)
cv.destroyAllWindows()