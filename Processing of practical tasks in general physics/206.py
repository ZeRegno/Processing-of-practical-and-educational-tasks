import numpy as np
import matplotlib.pyplot as plt

L=np.linspace(0.6, 0.1, 6)
T=[1722, 1431, 1138, 844, 564, 266]
y=T
x=L
St=1*10**(-6)
k=len(x)
yerr=list(range(k))
for i in range(k):
    y[i]=y[i]*10**(-6)

Sum_xy=0
Sum_x=0
Sum_y=0
Sum_x2=0
for i in range(k):
    Sum_xy=Sum_xy+x[i]*y[i]
    Sum_x=Sum_x+x[i]
    Sum_y=Sum_y+y[i] 
    Sum_x2=Sum_x2+x[i]**2
    yerr[i]=St
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
     
plt.title("Зависимость Времени прохождения сигналаот расстояния ")
plt.xlabel("расстояние L, м")
plt.ylabel("Время прохождения T, мкс")
plt.grid()
plt.errorbar(x, y_Aproximated,   fmt='-', c='blue', ecolor='c')
plt.errorbar( x, y,  fmt='o', yerr=yerr , c='r', ecolor='red')
plt.figure()
plt.show() 
V=1/A
Sv=V*Sigma_A/A*10**6
print(" V=", V, "+-", Sv)
T=np.linspace(50, 32, 19)
t=[1913, 1915, 1918, 1919, 1922, 1924, 1927, 1929, 1932, 1935,
   1938, 1940, 1943, 1946, 1948, 1951, 1954, 1957, 1960]
L0=0.695
T0=26.7
St=1*10**(-6)
k=len(t)
yerr=list(range(k))
V=list(range(k))
for i in range(k):
    t[i]=t[i]*10**(-6)
    T[i]=(T[i]+273)**0.5
    V[i]=L0/t[i]
y=list(range(k+1))
x=list(range(k+1))
y[0]=0
x[0]=0

i=1
while i <= k:
 y[i]=V[i-1]
 x[i]=T[i-1]
 i=i+1
print(x)
print(y)
i=0
Sum_xy=0
Sum_x=0
Sum_y=0
Sum_x2=0
for i in range(k):
    Sum_xy=Sum_xy+x[i]*y[i]
    Sum_x=Sum_x+x[i]
    Sum_y=Sum_y+y[i] 
    Sum_x2=Sum_x2+x[i]**2
    yerr[i]=St
A=(k*Sum_xy-Sum_x*Sum_y)/(k*Sum_x2-Sum_x**2)
B=(Sum_y-A*Sum_x)/k
Sigma_A=0
 
print("A=", A )
print("B=", B )

y_Aproximated=np.zeros(k+1, dtype=float)
for i in range(k):
     y_Aproximated[i]=x[i]*A+B
     Sigma_A= Sigma_A+(y[i]-y_Aproximated[i])**2
Sigma_A=(Sigma_A)
print("y_Aproximated=",y_Aproximated )
print("Sigma_A=", Sigma_A )
plt.title("Зависимость V(T^0.5) ")
plt.xlabel("T^0.5, K^0.5")
plt.ylabel("V, м/с")
plt.grid()
plt.errorbar(x, y_Aproximated,   fmt='', c='blue', ecolor='c')
plt.errorbar( x, y,  fmt='o' , c='r', ecolor='red')
plt.figure()
plt.show() 
y_Aproximated=np.zeros(k+1, dtype=float)


R=8.3145
M=0.02898
Y=M*A**2/R
Sy=2*Sigma_A/A
print(" Y=", Y, "+-", Sy)
Cv=R/(Y-1)
I=2/(Y-1)
Scv=R*(Y-1)**2*Sy
Si=2*(Y-1)**2*Sy
print(" Cv=", Cv, "+-", Scv)
print(" i=", I, "+-", Si)