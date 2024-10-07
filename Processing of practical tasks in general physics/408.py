import numpy as np
import matplotlib.pyplot as plt
def Dl(sL1,sL2, Amax):
    sL=(sL1+sL2)/2
    SsL=((sL1-sL)**2+(sL2-sL)**2)**0.5
    Dl=Amax/sL/10**(-4)/2
    sDl=Amax/(sL**2)*SsL*10**4
    return Dl, sDl
def PLT1 (x,y, yerr, X, Y): 
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
    
    print(Y, "от", X, "  ","A=",A)
    print(Y, "от", X, "  ","B=",B)
    y_Aproximated=np.zeros(k, dtype=float)
    for i in range(k):
     y_Aproximated[i]=x[i]*A+B
     Sigma_A= Sigma_A+(y[i]-y_Aproximated[i])**2
    print(Y, "от", X, "  ","Sigma_A=", Sigma_A )
    
    plt.errorbar(x, y_Aproximated,   fmt='--')
    plt.errorbar( x, y,  yerr=yerr, fmt='o')
    print(" ")
    return A
Dl1,sDl1=Dl(1.8, 2.16, 30*10000)
Dl2,sDl2=Dl(1.5, 1.8, 30*10000)
Dl3,sDl3=Dl(1.639, 1.86,30*10000)
L1=[4977, 5679, 6150]
Dlt=600*1200*1000
y=[Dl1,Dl2, Dl3]
y2=[Dlt,Dlt, Dlt]
x=L1
X="L, А"
Y="Dl, линейная дисперсия прибора от длины волны"
plt.xlabel(X)
plt.ylabel(Y)
plt.errorbar( x, y, yerr=[sDl1,sDl2,sDl3], fmt='o', c='r', ecolor='red')
plt.errorbar(x, y2, fmt='-', c='blue')
plt.grid()
plt.plot()
plt.show()
sl1=[0.70, 1.45, 1.92, 2, 3.75, 4.45, 0.41]
sl2=[0.66, 1.44, 1.98, 2.89, 2.57, 4.26, 0.39]
A=[30, 80, 120, 160, 200, 250, 16]
sL=np.zeros(len(A))
Ssl=np.zeros(len(A))
for i in range(len(sl2)):
    sl1[i]=abs(sl1[i])
    sl2[i]=abs(sl2[i])
    sL[i]=(sl1[i]+sl2[i])/2
    Ssl[i]=((sl1[i]-sL[i])**2+(sl2[i]-sL[i])**2)**0.5/len(sl2)
Ssl[5]=Ssl[5]*30
Ssl[4]=Ssl[4]*5
X="а, мкм"
Y="L, А, ширина линии в спектре"
plt.xlabel(X)
plt.ylabel(Y)
plt.errorbar( A, sL, fmt='o', c='r', ecolor='red')
plt.grid()
plt.plot()
plt.show()    
C=PLT1(A, sL, Ssl, "а, мкм","L, А, ширина линии в спектре")
plt.xlabel("а, мкм")
plt.ylabel("L, А, ширина линии в спектре от ширины щели")
plt.grid()
plt.plot()
plt.show()    
Dl2a=1/C
print(Dl2a)
L=5885
R=np.zeros(len(sl2))
Sr=np.zeros(len(sl2))
Y="Зависимость разрешающей способности"
for i in range(len(sl2)):
   R[i]=L*Dl2a/A[i]/3
   Sr[i]=R[0]*0.05+R[i]*0.05
plt.xlabel(X,fontsize=20)
plt.ylabel(Y,fontsize=20)
plt.errorbar( A, R, yerr=Sr, fmt='o', c='r', ecolor='red')
plt.grid()
plt.plot()
plt.show()

    