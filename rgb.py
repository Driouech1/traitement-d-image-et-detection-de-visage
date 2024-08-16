import cv2 as cv

img=cv.imread("photos/th (1).jpeg")
pix=img[100,200]
print(pix)
(B,G,R)=img[50,50]
print("B={},G={},B={}".format(R,G,B))
cv.imshow("r7",img)
cv.waitKey(0)

