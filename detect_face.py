import cv2 as cv
face_cascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_cascade=cv.CascadeClassifier('haarcascade_eye.xml')

img=cv.imread('photos/g.jpeg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,1.1,1)
eyes=eyes_cascade.detectMultiScale(gray,1.2,2)
for(x,y,w,h,)  in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,250),2)
    for (ex,ey,ew,eh) in eyes:
         cv.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,34,250),2)
         
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
    
