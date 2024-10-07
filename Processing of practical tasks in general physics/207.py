import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
from numpy import trapz
P=[1114.3, 1095.5, 1078.7, 1073.1, 1052.9, 1041.6, 1028.4, 1021.0, 1011.2, 998.3]
V=[35, 35.5, 36, 36.5, 37, 37.5, 38, 38.5, 39, 39.5]
s=0.05
y=P
x=V
k=len(x)
sY=list(range(k))
for i in range(k):
    sY[i]=s*y[i]/10
    
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
y_Aproximated=y
for i in range(k):
     y_Aproximated[i]=x[i]*A+B
     Sigma_A= Sigma_A+(y[i]-y_Aproximated[i])**2
Sigma_A=(Sigma_A)**0.5
print("Sigma_A=", Sigma_A )

"""area1 = trapz(y, dx=0.001)
print("area =", area1)

area2 = simps(y, dx=0.001)
print("area =", area2)"""
     
plt.title("P(V)")
plt.xlabel("V")
plt.ylabel("P")
plt.grid()

plt.errorbar(x, y_Aproximated,   fmt='-', c='blue', ecolor='green')
plt.errorbar( x, y,  fmt='o', c='r', ecolor='red')
plt.figure()
plt.show() 
R=8.31
T=298.83
n=1110.9*35.5/(R*297.07)/1000
dSt=R*n*np.log(39.5/35.0)
dS=list(range(k))
dSt=list(range(k))
i=0
d=1
while i<=k-1:
    dSt[i]=R*n*np.log(V[i]/V[0])
    dy=list(range(d))
    j=0
    while j <= d-1:
        dy[j]=y[j]
        j=j+1
    d=d+1
    area1 = trapz(dy, dx=0.001)
    dS[i]=area1/T/2
    print("T=const, dS=",dS[i]," , dSt=",dSt[i])
    print()
    i=i+1


pV=[39000.4, 38891.1, 38832.5, 39167, 38955.9, 39061.4, 39078.1, 39309.4, 39437.8, 39431.5]
V=[35, 35.5, 36, 36.5, 37, 37.5, 38, 38.5, 39, 39.5]
P=[1114.3, 1095.5, 1078.7, 1073.1, 1052.9, 1041.6, 1028.4, 1021.0 1011.2, 998.3]
plt.title("pV(V)")
plt.xlabel("pV")
plt.ylabel("V")
plt.grid()

plt.errorbar(V, pV,   fmt='o', c='blue', ecolor='green')
plt.figure()
plt.show() 

Vc=42.5/1000
P=[989.5, 990.3, 993.4, 995.8, 999.5, 1001.6, 1002.8, 1004,8]
T=[313.44, 313.24, 315.23, 316.16, 317.25, 318.21, 318.48, 319.17]
k=len(T)
dS=list(range(k))
x=list(range(k))
i=0
d=1
Cv=5/2*R
Cp=R+Cv
while i<=k-1:
    dS[i]=n*(-R*np.log(P[i]/P[0])+Cp*np.log(T[i]/T[0]))
    print("V=const, dS", dS[i])
    x[i]=np.log(T[i]/T[0])
    i=i+1
y=dS
   
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
y_Aproximated=y
for i in range(k):
     y_Aproximated[i]=x[i]*A+B
     Sigma_A= Sigma_A+(y[i]-y_Aproximated[i])**2
Sigma_A=(Sigma_A)**0.5
plt.title("dS(ln(Ti/T0))")
plt.xlabel("ln(Ti/T0)")
plt.ylabel("dS")
plt.grid()

plt.errorbar(y_Aproximated, x,   fmt='-', c='blue', ecolor='green')
plt.errorbar( y, x,  fmt='o', c='r', ecolor='red')
plt.figure()
plt.show() 
Cv=A/n
print("Cv=", Cv )
pt=[3.16, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15, 3.15]
P=[989.5, 990.3, 993.4, 995.8, 999.5, 1001.6, 1002.8, 1004,8]
plt.title("p/T(p)")
plt.xlabel("p, hpа")
plt.ylabel("p/T, hpa/K")
plt.grid()


plt.errorbar( P, pt,  fmt='o', c='r', ecolor='red')
plt.figure()
plt.show()

P=[1019.5, 1015.7, 1014.2, 998.7, 998.3, 998.0]
T=[305.79, 306.28, 306.88, 307.08, 310.29, 313.44]
v=np.linspace(39.5, 42, 6)
k=len(P)
i=0
Cv=5/2*R
dS=list(range(k))
x=list(range(k))
while i<=k-1:
    dS[i]=n*(-R*np.log(V[i]/V[0])+Cv*np.log(T[i]/T[0]))
    print("P=const, dS=", dS[i])
    x[i]=np.log(T[i]/T[0])
    i=i+1
y=dS
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
y_Aproximated=y
for i in range(k):
     y_Aproximated[i]=x[i]*A+B
     Sigma_A= Sigma_A+(y[i]-y_Aproximated[i])**2
Sigma_A=(Sigma_A)**0.5
print("Sigma_A=", Sigma_A )
plt.title("dS(ln(Ti/T0))")
plt.xlabel("ln(Ti/T0)")
plt.ylabel("dS")
plt.grid()
plt.errorbar(x, y_Aproximated,   fmt='-', c='blue', ecolor='green')
plt.errorbar( x, dS,  fmt='o', c='r', ecolor='red')
plt.figure()
plt.show()
VT=[0.13, 0.13, 0.13, 0.13, 0.13, 0.13]
v=np.linspace(39.5, 42, 6)
plt.title("V/T(V)")
plt.xlabel("V, ml")
plt.ylabel("V/T, ml/K")
plt.grid()
plt.errorbar( v, VT,  fmt='o', c='r', ecolor='red')
plt.figure()
plt.show()
Cp=A/n*3
print("Cp=", Cp )
P=[1019.5, 1015.7, 1014.2, 998.7, 998.3, 998.0]
V=np.linspace(42.5, 39, 7)

y=P
x=V
k=len(x)
sY=list(range(k))
for i in range(k):
    sY[i]=s*y[i]/10
    
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
y_Aproximated=y
for i in range(k):
     y_Aproximated[i]=x[i]*A+B
     Sigma_A= Sigma_A+(y[i]-y_Aproximated[i])**2
Sigma_A=(Sigma_A)**0.5
print("Sigma_A=", Sigma_A )

"""area1 = trapz(y, dx=0.001)
print("area =", area1)

area2 = simps(y, dx=0.001)
print("area =", area2)"""
     
plt.title("P(V)")
plt.xlabel("V")
plt.ylabel("P")
plt.grid()

plt.errorbar(x, y_Aproximated,   fmt='-', c='blue', ecolor='green')
plt.errorbar( x, y,  fmt='o', c='r', ecolor='red')
plt.figure()
plt.show() 
R=8.31
T=297.07
n=1110.9*35.5/(R*297.07)/1000
dSt=R*n*np.log(39.5/35.0)
dS=list(range(k))
dSt=list(range(k))
i=0
d=1
while i<=k-1:
    dSt[i]=R*n*np.log(V[i]/V[0])
    dy=list(range(d))
    j=0
    while j <= d-1:
        dy[j]=y[j]
        j=j+1
    d=d+1
    area1 = trapz(dy, dx=0.001)
    dS[i]=area1/T/2
    print("T=const, dS=",dS[i]," , dSt=",dSt[i])
    print()
    i=i+1


pV=[42799.3, 42835.8, 42757.8, 42749.0, 42587.2, 42530.9, 42676.4, 42657.6, 42484, 42572.1]
V=[38, 38.5, 39, 39.5, 40, 40.5, 41, 41.5, 42, 42.5]
P=[1120.3, 1103.5, 1093.8, 1080.4, 1063.3, 1051.5, 1042.7, 1030.3, 1019.9, 1007

plt.title("pV(V)")
plt.xlabel("pV")
plt.ylabel("V")
plt.grid()

plt.errorbar(V, pV,   fmt='o', c='blue', ecolor='green')
plt.figure()
plt.show() 