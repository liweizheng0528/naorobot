# -*- coding: utf-8 -*-

from numpy import *
import sys,os
from pca import *

reload(sys)
sys.setdefaultencoding('utf-8')

ef = Eigenfaces()
ef.dist_metric=ef.distEclud
ef.loadimgs("orl_faces/")
ef.compute()
# 创建测试集
# testImg = ef.X[10]
# print testImg
X = []

im = Image.open("12.pgm")
im = im.convert("L") #数据转换为long类型
X.append(np.asarray(im, dtype=np.uint8))
y = 3
# print X[0]
print "实际值 =", ef.y[10], "->", "预测值 =",ef.predict(X[0])

