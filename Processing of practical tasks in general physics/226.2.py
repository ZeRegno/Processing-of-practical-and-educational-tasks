import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
Nakal=[2.1, 2.2, 2.3, 2.4, 2.6, 2.7]
Temp=[769, 803, 879, 934, 1035, 1047]
ErrTemp=[41, 65, 85, 60, 161, 211]
V=[155, 162, 170, 180, 195, 200]
sV=[2, 3 ,4, 3 ,5 ,2]
y=Temp
x=Nakal
yerr=ErrTemp
m=0.91*10**(-30)
K=1.38*10**(-23)
a=m/(2*K)
print("a=",a)
k=len(x)
T=np.zeros(k)
sT=np.zeros(k)
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
Sigma_A=(Sigma_A)**0.5
print("Sigma_A=", Sigma_A )
i=0
for i in range(k):
    T[i]=a*(V[i]**2*10**6)
    sT[i]=2*a*V[i]*sV[i]*1000000
     
plt.title("Зависимость температуры термоэлектронов от напряжения накала")
plt.xlabel("Напряжение Накала, В")
plt.ylabel("Температура, К")
plt.grid()

plt.errorbar(x, T,   fmt='o-', yerr=sT, c='green', ecolor='green')
plt.errorbar( x, y,  fmt='o-', yerr=yerr , c='r', ecolor='red')
plt.figure()
plt.show() 

