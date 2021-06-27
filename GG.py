# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 16:46:40 2019

@author: MSI
"""
# สำหรับนักศึกษาที่ต้องการ Hint 
import random
import numpy as np
import matplotlib.pyplot as plt

np.seed = 1234

# กำหนดจำนวนของการทดลอง (ผู้เล่น) ในเเต่ละสมมติฐาน 
DisAI=np.array([175,176,188,173,178,182,175,176,180,175])
timeDis = np.array([2.26,2.41,3.16,2.20,2.45,3.00,2.24,2.40,2.58,2.24])
meanTime=np.mean(timeDis)
stdTime = np.std(timeDis)
meanDis = np.mean(DisAI)
stdDis = np.std(DisAI)
timeStd = np.std(timeDis)
print("Random uniform distribution mean : ",meanDis)
print("Random uniform distribution std : ",stdDis)
print("Random uniform distribution meanTime : ",meanTime)
print("Random uniform distribution stdTime : ",stdTime)

ClumAI=np.array([46,53,50,47,56,50,52,48,52,55])
timeClum=np.array([0.26,0.24])
meanClum=np.mean(ClumAI)
stdClum = np.std(ClumAI)
print("Random Clumsy mean : ",meanClum)
print("Random uClumsy std : ",stdClum)

Ntrails = 1000
Clumsy=[]
Uniform=[]
s = np.random.randint(meanDis-2*stdDis,meanDis+2*stdDis,100)
t=np.random.uniform(meanTime-2*stdTime,meanTime+2*stdTime,100)

print("Result of 1000 running ai uniform distribution : ",s)
print("Size of s : {}".format(s.__len__()))

s2=np.random.randint(meanClum-2*stdClum,meanClum+2*stdClum,1000)
print("Result of 1000 running ai Clumsy distribution : ",s2)
print("Size of s2 : {}".format(s2.__len__()))
plt.hist(labels="Apple",s)

