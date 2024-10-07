import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
V=6.95/1000
l=0.2
r=0.9/1000
R=8.31
M=28.98/1000
t=298
dat = pd.read_csv('201.dat', delimiter=',')
data=dat.to_numpy()
shape = data.shape
colums=shape[1]
rows=shape[0]
T=list(range(rows))
P1=list(range(rows))
P2=list(range(rows))
for i in range(rows):
    T[i]=data[i][0]
    P1[i]=data[i][1]
    P2[i]=data[i][2]
plt.title("dS(ln(Ti/T0))")
plt.xlabel("ln(Ti/T0)")
plt.ylabel("dS")
plt.grid()
plt.semilogy(T, P2, c='red' )
plt.semilogy(T, P1, c='black' )
plt.figure()
plt.show()

plt.title("pV(V)")
plt.xlabel("V")
plt.ylabel("pV")
plt.grid()
plt.errorbar(T, P2, c='red')
plt.errorbar(T, P1, c='black')
plt.figure()
plt.show() 
k=100
I=list(range(k))
T1=list(range(k))
i=0
while i <= k-1:
   I[i]=-V*(P1[i+1]-P1[i])/(T[i+1]-T[i])
   T1[i]=T[i]
   i+=1
plt.title("I(t)")
plt.xlabel("T")
plt.ylabel("Iv")
plt.grid()
plt.semilogy(T1, I, c='red' )
plt.figure()
plt.show()   

η=list(range(k))
P11=list(range(k))
P21=list(range(k))
for i in range(k):
    η[i]=np.pi*r**4*((P1[i]**2)-(P2[i]**2))/(16*I[i]*l)
    P11[i]=P1[i]
    P21[i]=P2[i]
plt.title("η(P1)")
plt.xlabel("P1")
plt.ylabel("η")
plt.grid()
plt.semilogx(P11, η, c='red')
plt.figure()
plt.show()  
v=420
λ1=list(range(k))
λ2=list(range(k))
λt1=list(range(k))
λt2=list(range(k))
for i in range(k):
    λ1[i]=3*η[i]*R*t/(v*P1[i]*M)
    λ2[i]=3*η[i]*R*t/(v*P2[i]*M)
    λt1[i]=6.2*10**(-3)/P1[i]
    λt2[i]=6.2*10**(-3)/P2[i]
plt.title("η(P1)")
plt.xlabel("P1")
plt.ylabel("η")
plt.grid()
plt.semilogx(P11, λ1,  c='red')
plt.semilogx(P11, λt1, c='blue')
plt.figure()
plt.show() 

plt.title("η(P1)")
plt.xlabel("P1")
plt.ylabel("η")
plt.grid()
plt.semilogx(P21, λ2,  )
plt.semilogx(P21, λt2)
plt.figure()
plt.show() 



nV0=4.5*3600
Pmin=216*10**(-6)
y=1.3


I2=list(range(k))
S=list(range(k))
S2=list(range(k))
P22=list(range(k))
i=0
j=0
while i <= k-1:
   I2[j]=-V*(P2[i]-P2[i-1])/(T[i]-T[i-1])
   print('I=', I2[j])
   P22[j]=P2[i]
   S[j]=I2[j]/P22[j]
   S2[j]=nV0*(1-(Pmin/P22[j])**(1/2.6))/10**6
   j+=1
   i+=1
plt.title("S(P2)")
plt.xlabel("P2")
plt.ylabel("S")
plt.grid()
plt.semilogx(P22, S, c='red')
plt.semilogx(P22, S2, c='blue')
plt.figure()
plt.show() 
k=110
rows=130
d=k
k=rows-d
T2=list(range(k))
P12=list(range(k))
i=d
j=0
while i <= rows-1:
   T2[j]=T[i]
   P12[j]=P1[i]
   j+=1
   i+=1

y=P12
x=T2
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
Sigma_A=(Sigma_A)
print("Sigma_A=", Sigma_A )
plt.title("pV(V)")
plt.xlabel("V")
plt.ylabel("pV")
plt.grid()
plt.errorbar(x, y_Aproximated,   fmt='-', c='blue', ecolor='green')
plt.errorbar( x, y,  fmt='o', c='r', ecolor='red')
plt.figure()
plt.show() 