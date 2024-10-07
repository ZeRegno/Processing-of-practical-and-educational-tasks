import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
def PLT1 (x,y, c): 
    y=y
    x=x
    k=len(y)
    Sum_xy=0
    Sum_x=0
    Sum_y=0
    Sum_x2=0
    for i in range(k):
       Sum_xy=Sum_xy+x[i]*y[i]
       Sum_x=Sum_x+x[i]
       Sum_y=Sum_y+y[i] 
       Sum_x2=Sum_x2+x[i]**2
    A=(k*Sum_xy-Sum_x*Sum_y)/(k*Sum_x2-Sum_x**2)
    B=(Sum_y-A*Sum_x)/k
    Sigma_A=0
    y_Aproximated=np.zeros(k, dtype=float)
    
    y_Aproximated=np.zeros(k, dtype=float)
    for i in range(k):
     y_Aproximated[i]=x[i]*A+B
     Sigma_A= Sigma_A+(y[i]-y_Aproximated[i])**2
    plt.errorbar(x, y_Aproximated,   fmt='--' ,c=c)
    plt.errorbar( x, y, fmt='o' ,c="red")

    
    print(c,"A=", A, "B=", B)
    
    print("коэфицент кореляции=",corl(x,y))
    print("")
    return  A
def corl(x,y):
    xsr=0
    ysr=0
    y2sr=0
    x2sr=0
    xysr=0
    for i in range(len(x)):
        xsr=x[i]+xsr
        ysr=ysr+y[i]
        xysr=xysr+y[i]*x[i]
        x2sr=x[i]**2+x2sr
        y2sr=y[i]**2+y2sr
    xsr=xsr/len(x)
    ysr=ysr/len(x)
    xysr=xysr/len(x)
    x2sr=x2sr/len(x)
    y2sr=y2sr/len(x)
    r=(xysr-xsr*ysr)/((x2sr-xsr**2)**0.5*(y2sr-ysr**2)**0.5)
    return r
def sq (x): 
    x=x
    k=len(x)
    x_A=np.zeros(k, dtype=float)
    for i in range(k):
     x_A[i]=x[i]**2
    return x_A
X=(29, 37, 50, 67, 85, 103, 115, 54)
PLT1(sq(X), (1014, 1795, 3595, 6488, 10486, 15614, 19888, 4109), "blue")
plt.title("зависимость интенсивности от ширины щели")
plt.xlabel("ширина щели в ^2, мкм^2")
plt.ylabel("Интенсивность")
plt.grid()
plt.show()
X=(1, 2, 3, 4)
PLT1(sq(X), (1372, 5494, 13150, 17462), "blue")
plt.title("зависимость интенсивности от количества щелей")
plt.xlabel("количество щелей ^2")
plt.ylabel("Интенсивность")
plt.grid()
plt.show()


PLT1((1, 2, 3, 4 ,5, 6, 7), (0.0045, 0.0066, 0.0089, 0.0116, 0.014, 0.017, 0.019), "blue")
plt.xlabel("Номер Экстремума")
plt.ylabel("1/bi, 1/mm")
plt.grid()
plt.show()