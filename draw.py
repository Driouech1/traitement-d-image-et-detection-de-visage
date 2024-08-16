import cv2 as cv
import numpy as np 

image=np.zeros((500, 500,3),dtype='uint8')
cv.imshow('blank',image)
img=cv.imread('photos/th (4).jpeg')
cv.imshow('catt',img)

#paint
image[200:300 ,400:504] =191,206,253
cv.imshow("image",image)

#paint rectangle
cv.rectangle(image,(50,100),(200,200),(0,255,0),thickness=7,lineType= cv.LSD_REFINE_ADV)
cv.imshow("rectangle",image)

#draw a cercle
cv.circle(image,center=(250,250),radius=100,color=(0,0,250),thickness=-1)
#cv.imshow("circle",image)

#draw a line
cv.line(image,(50,100),(200,200),(255,255,0),thickness=3,lineType= cv.LSD_REFINE_ADV)
cv.imshow("line",image)
#write a text
cv.putText(image,text='Hy I\'m Aymane',org=(10,30),thickness=1,fontFace=cv.FAST_FEATURE_DETECTOR_TYPE_7_12,color=( 200,0,255),lineType=cv.ACCESS_MASK,fontScale=2)
cv.imshow("text",image)
cv.waitKey(0)

