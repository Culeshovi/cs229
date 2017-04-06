import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import pandas as pd
import numpy as np

def grad_runner(x,y,a,b,m,iterate):
    new_m=m
    new_b=b
    for i in range(iterate):
        [new_b,new_m]=gradient_descent_algorithm(x,y,a,new_b,new_m)
    return [new_b,new_m]
    
def gradient_descent_algorithm(x,y,a,b,m):
    new_m=0
    new_b=0
    n=float(len(x))
    for i in range(len(x)):
        h=x[i] 
        new_m+=(1/n)*h*(y[i]-(m*h+b))
        new_b+=(1/n)*(y[i]-(m*h+b))
    m1=m+(a*new_m)
    b1=b+(a*new_b)
    return [b1,m1]
            

def predict(x,b,m):#Predicter Function
    y=[]
    for i in range(len(x)):
        k=float(x[i])*m+b
        y.append(float(k))
    return y
        

def run():
    a=0.0001#learning_rate
    initial_b = 0 # initial y-intercept guess
    initial_m = 0 # initial slope guess
    linear_train = pd.read_excel("cricket chirps vs temperature.xls")
    x=np.array(linear_train['X'],)
    y=np.array(linear_train['Y'],)
    x_test=np.array(linear_train['X'],)
    iteration=1000
    [b,m]=grad_runner(x,y,a,initial_b,initial_m,iteration)
    k=predict(x_test,b,m)
    plt.xlabel('chirps/sec for the striped ground cricket')
    plt.ylabel('temperature in degrees Fahrenheit')
    plt.title(' Cricket Chirps Vs. Temperature')
    plt.scatter(x,y,label='Points')
    plt.plot(x_test,k,label='Hypothesis')
    plt.legend()
    plt.show()
    #Data set used from http://college.cengage.com/mathematics/brase/understandable_statistics/7e/students/datasets/slr/frames/frame.html
    
 








    
if __name__ == '__main__':
    run()
