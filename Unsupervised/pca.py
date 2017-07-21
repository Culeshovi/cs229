import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import pandas as pd
import numpy as np
import math
import random

a1=[]
a2=[]
for i in range(100):
    a1.append(random.randint(5,60))
    a1.append(random.randint(-56,-1))
    a2.append(random.randint(0,40))
    a2.append(random.randint(-37,-3))
plt.scatter(a1,a2,color='c')
plt.show()

#Applying PCA
a1=np.array(a1)
a2=np.array(a2)
m1=np.mean(a1)
m2=np.mean(a2)
a1=a1-m1
a2=a2-m2
k=[]
for i in range(200):
    k.append([a1[i],a2[i]])
k=np.array(k)
s =np.matmul(k.T,k)
s=s/200


t1=[]
t2=[]
for i in k:
    t1.append(np.dot(s[0],i))
    t2.append(0)
print (t1)
plt.scatter(t1,t2,color='r')
plt.show()
    


    








    


                

