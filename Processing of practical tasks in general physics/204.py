import numpy as np
import matplotlib.pyplot as plt
P=0.0185
D=0.061
k=0.91
T1=23
xerr=[1, 1, 1, 1]
F=np.zeros(4)
s=np.zeros(4)
sa=np.zeros(4)
F_hol=[0.046, 0.045, 0.046]
F_tepl=[0.039, 0.04, 0.041]
tepl=[80+273, 76+273, 74+273, 23+273]
F_vniz=[0.019, 0.026, 0.0245, 0.024, 0.022, 0.02, 0.018, 0.016, 0.014, 0.012, 0.0105, 0.014]
F_vverh=[0.015, 0.015, 0.0155, 0.016, 0.0175, 0.02, 0.022, 0.024, 0.026, 0.028, 0.03, 0.0325, 0.035, 0.037, 0.0395, 0.0415, 0.042, 0.0425, 0.044, 0.045, 0.0465, 0.047, 0.0185]
Vniz=[0, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660]
Vverh=[600, 540, 480, 420, 360, 300, 240, 180, 120, 60, 0, -60, -120, -180, -270, -300, -360, -420, -480, -540, -600, -630, -660]

for i in range(3):
    F_hol[i]=F_hol[i]-P
    print(F_hol[i])
F_hsr=(F_hol[0]+F_hol[1]+F_hol[2])/3
print("F_hol=",F_hsr)
for i in range(3):
    Sfsr=(F_hsr-F_hol[i])**2
Sfsr=(Sfsr/6)**(1/2)
print("Sfsr=", Sfsr)
for i in range(3):
    F[i]=F_tepl[i]-P
    print(tepl[i], "F=", F[i])
F[3]=F_hsr
Ss=np.zeros(4)
for i in range(4):
    s[i]=F[i]/(2*k*3.1415*D)
    Ss=1.5*(0.0005/(2*k*3.1415*D))
    print(tepl[i], "s=", s[i], "+-", Ss)
x=tepl
y=s
Sum_xy=0
Sum_x=0
Sum_y=0
Sum_x2=0
k=4
for i in range(k):
    Sum_xy=Sum_xy+x[i]*y[i]
    Sum_x=Sum_x+x[i]
    Sum_y=Sum_y+y[i] 
    Sum_x2=Sum_x2+x[i]**2
A=(k*Sum_xy-Sum_x*Sum_y)/(k*Sum_x2-Sum_x**2)
B=(Sum_y-A*Sum_x)/k
Sigma_A=0
for i in range(4):
    sa[i]=tepl[i]*A+B
    print(tepl[i], "sa=", sa[i])
y_Aproximated=sa
for i in range(k):
     y_Aproximated[i]=x[i]*A+B
     Sigma_A= Sigma_A+(y[i]-y_Aproximated[i])
Sigma_A=(Sigma_A)**0.5
print("Sigma_A=", Sigma_A )
print("A=", A )
print("B=", B )
SA=Sigma_A
plt.title("s(T)")
plt.xlabel("T, К")
plt.ylabel("s, Н/м")
plt.grid()
plt.errorbar(tepl, sa,   fmt='-', c='r', ecolor='red')
plt.errorbar(tepl, s, xerr=xerr, yerr=Ss,   fmt='o', c='b', ecolor='b')
plt.figure()
plt.show()
q=np.zeros(4)
Sq=np.zeros(4)
for i in range(4):
    q[i]=-tepl[i]*A
    Sq[i]=((-tepl[i]*SA)**2+(0.5*A)**2)**0.5*5
    print(tepl[i], "q=", q[i],"+-", Sq[i])
plt.title("q(T)")
plt.xlabel("T, K")
plt.ylabel("q, Дж/К")
plt.grid()
plt.errorbar(tepl, q, yerr=Sq,  fmt='o-', c='r', ecolor='red')
plt.figure()
plt.show() 

plt.title("F(a)")
plt.xlabel("a(угол поворота ручки)")
plt.ylabel("F, Н")
plt.grid()
plt.errorbar(Vverh, F_vverh,  fmt='.', c='b', ecolor='red')
plt.errorbar(Vniz, F_vniz,   fmt='.', c='r', ecolor='red')
plt.figure()
plt.show() 
U=np.zeros(4)
SU=np.zeros(4) 
Sum_xy=0
Sum_x=0
Sum_y=0
Sum_x2=0  
A=0
B=0   
for i in range(4):
    U[i]=s[i]+q[i]
    SU[i]=(Ss**2+Sq[i]**2)**0.5
    print(tepl[i], "U=", U[i],"+-", SU[i])
k=4
x=tepl
y=U
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
Ua=y_Aproximated

plt.title("U(T)")
plt.xlabel("T, К")
plt.ylabel("U, Дж")
plt.grid()
plt.errorbar(tepl, Ua,  fmt='-', c='b', ecolor='red')
plt.errorbar(tepl, U, yerr=SU, fmt='o', c='r', ecolor='orange')
plt.figure()
plt.show() 