import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
def PLT1 (x,y, yerr, c): 
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
    plt.errorbar( x, y, fmt='o', yerr= yerr ,c=c)
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
Kr=[92, 99, 103, 108, 120]
Zel=[92, 102, 109, 116, 131]
Sin=[94, 103, 110, 120, 138]
yerr1=np.zeros(len(Kr))
yerr2=np.zeros(len(Kr))
yerr3=np.zeros(len(Kr))
Kr1=Kr[0]
Zel1=Zel[0]
Sin1=Sin[0]
for i in range(len(Kr)):
    Kr[i]=Kr[i]-Kr1
    Zel[i]=Zel[i]-Zel1
    Sin[i]=Sin[i]-Sin1
    print(Kr[i])
    print(Zel[i])
    print(Sin[i])
    print(" ")
    yerr1[i]=Kr[i]/max(Kr)
    yerr2[i]=Zel[i]/max(Zel)
    yerr3[i]=Sin[i]/max(Sin)
C=[0, 0.061, 0.0985, 0.142, 0.2394]
Akr=PLT1(C, Kr, yerr1, 'red')
Azel=PLT1(C, Zel, yerr2,'green')
Asin=PLT1(C, Sin, yerr3, 'blue')
plt.legend(["Красный", " ", "Зеленый", "", "Синий", " "])
plt.grid()
plt.title("Зависимость угла вращения плоскости поляризации от концентрации раствора", size=10)
plt.show()
d=1.9
akr=Akr/d
azel=Azel/d
asin=Asin/d
print("akr=",akr)
print("azel=",azel)
print("asin=",asin)
Kr=[105, 110, 117, 126]
Zel=[112, 120, 127, 137]
Sin=[114, 122, 130, 143]
yerr1=np.zeros(len(Kr))
yerr2=np.zeros(len(Kr))
yerr3=np.zeros(len(Kr))
for i in range(len(Kr)):
    Kr[i]=Kr[i]-Kr1
    Zel[i]=Zel[i]-Zel1
    Sin[i]=Sin[i]-Sin1
    print(Kr[i])
    print(Zel[i])
    print(Sin[i])
    print(" ")
    yerr1[i]=Kr[i]/max(Kr)
    yerr2[i]=Zel[i]/max(Zel)
    yerr3[i]=Sin[i]/max(Sin)
C=[0.7, 0.9, 1.2, 1.6]
Akr=PLT1(C, Kr, yerr1, 'red')
Azel=PLT1(C, Zel, yerr2,'green')
Asin=PLT1(C, Sin, yerr3, 'blue')
plt.legend(["Красный", " ", "Зеленый", "", "Синий", " "])
plt.grid()
plt.title("Зависимость угла вращения плоскости поляризации от толщины пластинки", size=10)
plt.show()
Akv=[Akr, Azel, Asin]
Asah=[akr, azel, asin]
L=[0.632, 0.515, 0.464]
L1=np.zeros(len(L))
yerr=np.zeros(len(L))
for i in range(len(L)):
    L1[i]=L[i]**(-2)
    print("L1=",L1[i])
PLT1(L1, Asah, yerr, "orange")
PLT1(L1, Akv, yerr, "grey")
plt.title("графики зависимости удельного вращения плоскости поляризации от 1/L^2", size=10)
plt.xlabel("1/L^2, 1/мкм^2",fontsize=20)
plt.ylabel("удельное вращение плоскости поляризации",fontsize=10)
plt.legend(["Раствор сахара", "град*см^3/(дм*г) ", "Кварц", "град/мм"])
plt.grid()
plt.show()