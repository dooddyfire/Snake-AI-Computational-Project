#!/usr/bin/env python
# coding: utf-8

# In[27]:


import random
import numpy as np
import matplotlib.pyplot as plt

np.seed = 1234

# กำหนดจำนวนของการทดลอง (ผู้เล่น) ในเเต่ละสมมติฐาน 
DisAI=np.array([175,176,188,173,178,182,175,176,180,175])   #Result getting from running AI on Random Unifrom Distribution Food pattern
timeDis = np.array([2.26,2.41,3.16,2.20,2.45,3.00,2.24,2.40,2.58,2.24])
meanTime=np.mean(timeDis) #mean Time

meanDis = np.mean(DisAI) #Mean Score Random Uniform
stdDis = np.std(DisAI)  #SD Score  Random Uniform
timeStd = np.std(timeDis)  #SD Time Random Uniform
print("Random uniform distribution mean : ",meanDis)
print("Random uniform distribution std : ",stdDis)
print("Random uniform distribution meanTime : ",meanTime)
print("Random uniform distribution stdTime : ",stdTime)

ClumAI=np.array([46,53,27,25,27,56,30,48,36,65]) #Result getting from running AI on Clumsy Food pattern
timeClum=np.array([0.26,0.24,0.15,0.10,0.08,0.18,0.12,0.20,0.14,0.18]) #Time Clumsy
meanClum=np.mean(ClumAI) #Mean Clumsy food
stdClum = np.std(ClumAI) # SD Time Clumsy Food
print("Random Clumsy mean : ",meanClum) 
print("Random Clumsy std : ",stdClum)

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
plt.hist(s, alpha = 0.5, color = 'b' , label = 'Random Food Score')
plt.legend()


# In[30]:


plt.hist(s2, alpha = 0.5, color = 'r' , label = 'Clumsy Food Score')
plt.legend()


# In[25]:


ScoreDis = DisAI/timeDis
plt.hist(ScoreDis, alpha = 0.5, color = 'r' , label = 'Score/Time Uniform')
plt.legend()


# In[28]:



plt.hist(ClumAI/timeClum, alpha = 0.5, color = 'r' , label = 'Score/Time Clumsy')
plt.legend()


# In[ ]:




