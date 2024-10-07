import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
P=[215, 175, 153, 125, 97, 64, 38]
T=[-10.8, -11.2, -11.8, -12.7, -13.8, -15.3, -17.4]
sT=0.05
y=T
x=P
k=len(x)
sY=list(range(k))
for i in range(k):
    y[i]=4.67+y[i]
    y[i]=-1/y[i]
    sY[i]=sT*y[i]**2
    print("p=", P[i], " 1/T=", y[i], "+-", sY[i])
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
 
print("A=", A )
print("B=", B )

y_Aproximated=np.zeros(k, dtype=float)
for i in range(k):
     y_Aproximated[i]=x[i]*A+B
     Sigma_A= Sigma_A+(y[i]-y_Aproximated[i])**2
     sY[i]=sY[i]*3
Sigma_A=(Sigma_A)**0.5
print("Sigma_A=", Sigma_A )

     
plt.title("1/dT от dp")
plt.xlabel("dp")
plt.ylabel("1/dT")
plt.grid()

plt.errorbar(x, y_Aproximated,   fmt='-', c='blue', ecolor='green')
plt.errorbar( x, y,  fmt='o', yerr=sY, c='r', ecolor='red')
plt.figure()
plt.show() 

W=3.74
p=742*133
T0=295
R=8.31
b=1.51*10**(-6)
Cp=A*W*T0/(b*p)*R
print("Cp=",Cp)
Cv=Cp-R
print("Cv=",Cv)
I=Cv/R*2
print("I=",I, "+-", 2*1.23/R)
