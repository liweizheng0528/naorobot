# -*- coding: utf-8 -*-

from numpy import *
import cv2
from matplotlib import pyplot as plt

# 读取图片
img = cv2.imread( 'lawrence.mono.pgm' , 1) #黑白图片
plt.imshow(img, cmap = 'gray' , interpolation = 'bicubic' )
plt.xticks([]), plt. yticks([]) # 隐藏 X Y 坐标
plt.show()
