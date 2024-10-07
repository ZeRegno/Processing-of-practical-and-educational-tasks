import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

N1=800
r=14 
R1=50
Pi=3.1415
C= 4.7/10**6
R3=28*1000
N2=400
S = 3*3 
M0=1.257*10**(-8)
OA=[49, 49, 47, 45, 45, 42, 40, 38, 35, 30]
OB=[1912, 1760, 1607, 1431, 1243, 1056, 774, 598, 387, 223]
OC=[34, 33, 42, 40, 38, 38, 36, 36, 36, 35]
OD=[69, 70, 70, 70, 67, 67, 66, 65, 59, 54]
OA1=[-54, -55, -51, -50, -49, -49, -46, -45, -41, -40]
OB1=[-1982, -1830, -1677, -1490, -1314, -1103, -833, -692,-457,-282]
OC1=[-33, -32, -32, -23, -22, -21, -21, -20, -20, -20]
OD1=[-60, -60, -59,- 57, -56, -55, -53, -52, -50, -42]

x=OA
k=len(OA)
print(k)
k=len(OA1)
print(k)
k=len(OB)
print(k)
k=len(OB1)
print(k)
k=len(OC)
print(k)
k=len(OC1)
print(k)
k=len(OD)
print(k)
k=len(OD1)
print(k)
Hc=list(range(k))
Hs=list(range(k))
Boct=list(range(k))
Bs=list(range(k))
M=list(range(k))
for i in range(k):
 Hc[i]=(N1/(2*Pi*r))*0.5*(OA[i]-OA1[i])/50
 Boct[i]=R3*C*0.5*(OC[i]-OC1[i])/(N2*S) 
 Hs[i]=(N1/(2*Pi*r))*0.5*(OB[i]-OB1[i])/50 
 Bs[i]=R3*C*0.5*(OD[i]-OD1[i])/(N2*S)
 M[i]=Bs[i]/(M0*Hs[i])

print(Hc) 
print(Boct)
print(Bs)
print(Hs)
print(M)
 
plt.title("ВS(HS)")
plt.xlabel("ВS")
plt.ylabel("HS")
plt.grid()
plt.errorbar( Hs, Bs,  fmt='o' , c='r', ecolor='red')
plt.figure()
plt.show()

plt.title("M(HS)")
plt.xlabel("M")
plt.ylabel("HS")
plt.grid()
plt.errorbar( Hs,M,  fmt='o' , c='r', ecolor='red')
plt.figure()
plt.show()
"""
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
     
plt.title("Зависимость температуры термоэлектронов от напряжения накала")
plt.xlabel("Напряжение Накала, В")
plt.ylabel("Температура, К")
plt.grid()
plt.errorbar(x, y_Aproximated,   fmt='-', c='blue', ecolor='c')
plt.errorbar( x, y,  fmt='o', yerr=yerr , c='r', ecolor='red')
plt.figure()
plt.show()"""