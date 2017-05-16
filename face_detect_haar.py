#-*-coding:utf8-*-#
"""
Created on Wed Feb 04 21:53:05 2015
@author: http://2hwp.com/
"""


import os
import cv2
from PIL import Image,ImageDraw

#detectFaces()返回图像中所有人脸的矩形坐标（矩形左上、右下顶点）
#使用haar特征的级联分类器haarcascade_frontalface_default.xml，在haarcascades目录下还有其他的训练好的xml文件可供选择。
#注：haarcascades目录下训练好的分类器必须以灰度图作为输入。
def detectFaces(image_name):
    img1 = cv2.imread(image_name)
    img = cv2.resize(img1,(240,319))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



    face_cascade = cv2.CascadeClassifier("/Users/chiyexiao/Documents/Nao/naorobot/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_alt2.xml")

#    face_cascade = cv2.CascadeClassifier("/Users/chiyexiao/Documents/Nao/naorobot/opencv-3.2.0/data/haarcascades/haarcascade_profileface.xml")


#    if img.ndim == 3:
#    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#    else:
#        gray = img #if语句：如果img维度为3，说明不是灰度图，先转化为灰度图gray，如果不为3，也就是2，原图就是灰度图

    faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = 0
    )

#    face_cascade.detectMultiScale( frame_gray, faces, 1.1, 2, 0|CV_HAAR_SCALE_IMAGE, Size(30, 30) );


    result = []
    print faces
    for (x,y,width,height) in faces:
        result.append((x,int(y - 0.117*height),x+width,int((y+1.1*height))))
#    print result
    return result


#保存人脸图
def saveFaces(image_name,id):
    faces = detectFaces(image_name)
    if faces:
        #将人脸保存在save_dir目录下。
        #Image模块：Image.open获取图像句柄，crop剪切图像(剪切的区域就是detectFaces返回的坐标)，save保存。
#        save_dir = image_name.split('.')[0]+"_faces"
#        os.mkdir(save_dir)
        count = 0
        for (x1,y1,x2,y2) in faces:
            file_name = os.path.join(image_name.split('.')[0]+"_"+str(count)+".jpg")
            filename1 =os.path.join("s42/"+str(id)+".pgm")
            Image.open(image_name).resize(((240,319)),Image.ANTIALIAS).crop((x1,y1,x2,y2)).save(file_name)
            count+=1
            img = cv2.imread( file_name,0) #0 黑白图片；1 原色图片
            img = cv2.resize(img,(92,112))
            cv2.imwrite(filename1, img)
    print faces




if __name__ == '__main__':
    files = os.listdir('pics')
    id = 0
    for filename in files:
#        print filename
        saveFaces('pics/'+filename,id)
        id=id+1

