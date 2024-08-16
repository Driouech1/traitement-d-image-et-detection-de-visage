import cv2 as cv
face_cascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_cascade=cv.CascadeClassifier('haarcascade_eye.xml')
cap=cv.VideoCapture(0)
while True:
    _,img=cap.read()

    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,2)
    eyes=eyes_cascade.detectMultiScale(gray,1.2,2)
    for(x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        for (ex,ey,ew,eh) in eyes:
         cv.rectangle(img,(ex,ey),(ex+ew,ey+eh),(100,34,250),2)
         
    cv.imshow('image',img)
    k=cv.waitKey(30)& 0xff
    if k==27:
        break
cv.destroyAllWindows()
cap.release()