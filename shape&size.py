import cv2 as cv

img=cv.imread("photos/th (1).jpeg",0)
print("shape:",img.shape)
print("size:",img.size)
print("type:",img.dtype)
cv.imshow("img",img)

cv.waitKey(0)