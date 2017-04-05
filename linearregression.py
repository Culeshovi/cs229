import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


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
    x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
    y=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
    x_test=[7.0,8.0,9.0,10.0]
    iteration=1000
    [b,m]=grad_runner(x,y,a,initial_b,initial_m,iteration)
    k=predict(x_test,b,m)
    plt.scatter(x_test,k,s=50)
    plt.plot(x_test,k)
    plt.show()
    
 








    
if __name__ == '__main__':
    run()
