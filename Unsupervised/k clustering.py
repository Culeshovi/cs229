import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import pandas as pd
import numpy as np
import random
z1=[]
z2=[]
k1=[55,15]
k2=[15,35]
for i in range(100):
    z1.append(random.randint(40,70))
    z1.append(random.randint(0,30))
    z2.append(random.randint(25,45))
    z2.append(random.randint(0,20))

#plt.scatter(y1,y2,color='c')
plt.scatter(z1,z2,color='g')
plt.scatter(k1[0],k1[1],color='r',marker='x')
plt.scatter(k2[0],k2[1],color='c',marker='x')
plt.show()
def kmeanscluster(z1,z2,k1,k2,iterate):
    new_k1=k1
    new_k2=k2
    for i in range(iterate):
        [ new_k1, new_k2]=clusteralgo(z1,z2,new_k1,new_k2)
    return (new_k1,new_k2)

def clusteralgo(z1,z2,new_k1,new_k2):
    x1=[]
    x2=[]
    y1=[]
    y2=[]
    for j in range(len(z1)):
        if np.linalg.norm(np.array([z1[j],z2[j]])-np.array(new_k1)) < np.linalg.norm(np.array([z1[j],z2[j]])-np.array(new_k2)):
            x1.append(z1[j])
            x2.append(z2[j])
        else:
            y1.append(z1[j])
            y2.append(z2[j])
    plt.scatter(new_k1[0],new_k1[1],color='r',marker='x')
    plt.scatter(new_k2[0],new_k2[1],color='c',marker='x')
    new_k1[0]=sum(x1)/len(x1)
    new_k1[1]=sum(x2)/len(x2)
    new_k2[0]=sum(y1)/len(y1)
    new_k2[1]=sum(y2)/len(y2)
    plt.scatter(x1,x2,color='r')
    plt.scatter(y1,y2,color='c')
    plt.show()
    return [new_k1,new_k2]

        
[b,m]=kmeanscluster(z1,z2,k1,k2,10)
print (b,m)        
                

