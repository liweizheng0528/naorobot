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
testImg = ef.X[69]
print "实际值 =", ef.y[69], "->", "预测值 =",ef.predict(testImg)