import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img=cv.imread('photos/d.jpeg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('dog',gray)

hist=cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title('Grayscall histogram')
plt.xlabel('hist')
plt.ylabel('# of pixels')
plt.plot(hist)
plt.xlim([0,256])
plt.show()
  #color histogramm
plt.figure()
plt.title('Golors histogram')
plt.xlabel('hist')
plt.ylabel('# of pixels')
color=('b','g','r')
for i ,col in enumerate(color):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()    
