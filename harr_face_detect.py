# -*- coding: utf-8 -*-

from numpy import *
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('/Users/chiyexiao/Documents/Nao/naorobot/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_alt.xml')

img = cv2.imread('lawrence.jpg')
gray = cv2.imread('lawrence.jpg',0)



faces = face_cascade.detectMultiScale(gray, 1.2, 3)
print faces
for (x,y,w,h) in faces:
    img2 = cv2.rectangle(img,(x,int(y - 0.117*h)),(x+w,int((y+1.1*h))),(255,255,255),4)
#	roi_gray = gray[y:y+h, x:x+w]
#	roi_color = img[y:y+h, x:x+w]

cv2.imwrite("IMG$(##.lawrence.jpg", img) # ±£¥ÊÕº∆¨


#y-(1/3)*h y+(4/3)
