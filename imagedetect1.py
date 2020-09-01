import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('Files/haarcascade_frontalface_default.xml')
eye_cascade =cv2. CascadeClassifier('Files/frontalEyes35x16.xml')
img = cv2.imread('shirley_pic1.jpeg')
#convert it to grayscale image
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)

print(faces)
for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    eye_gray = gray_img[y:y+h,x:x+w]
    eye_color= img[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(eye_gray,scaleFactor=1.05,minNeighbors=5)
    for ex,ey,ew,eh in eyes:
        cv2.rectangle(eye_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),3)
        cv2.imshow("image",img)
#cv2.imshow('Gray Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
