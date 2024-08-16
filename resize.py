import cv2 as cv

img=cv.imread('photos/catt.jpg')
cv.imshow('catt',img)

width=500
height=500

new_img=cv.resize(img,(width,height))

cv.imshow('Ressed image',new_img)
cv.waitKey(0)
cv.destroyAllWindows()
