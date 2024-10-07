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
    plt.errorbar( x, y, fmt='o' ,c=c)
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
PLT1((-2, -1, 0, 1, 2), (-139, -80, 0, 58, 117), "blue")
PLT1((-2, -1, 0, 1, 2), (-142, -72, 0, 77, 151), "green")
PLT1((-2, -1, 0, 1, 2), (-192, -141, 0, 96, 196), "red")
plt.title("зависимость Хм от м")
plt.xlabel("m")
plt.ylabel("Хм, 10 мкм")
plt.grid()