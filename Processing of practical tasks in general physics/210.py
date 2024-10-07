R=8.31
mcu=23.1
Ccu=412
Tcu=427
m=[5.1, 19.7, 23.1, 9.2]
T=[249, 455, 427, 300]
k=len(m)
C=list(range(k))
for i in range(k):
    C[i]=Ccu*mcu/m[i]*T[i]/Tcu
C[3]=C[3]+2.5/6.7*(C[3]-900)
M=[ 0.012,  0.05585,  0.063546, 0.1187]
Cm=list(range(k))
CR=list(range(k))
for i in range(k):
    Cm[i]=C[i]*M[i]
    CR[i]=Cm[i]/R
    print(CR[i], '\n')

dT=[[-308.9, -188.07, -188.07, -305.03],
    [-441.7, -239.61, -242.23, -415.59],
    [-616, -291, -302, -549],
    [-735, -371,8, -385.7, 0]]
C2=[[-308.9, -188.07, -188.07, -305.03],
    [-441.7, -239.61, -242.23, -415.59],
    [-616, -291, -302, -549],
    [-735, -371,8, -385.7, 0]]
q=list(range(k))
i=0
while i <=3:
    j=0
    while j <=3:
        if i ==3:
         if j==3:
            break;
         C2[j][i]=Ccu*mcu/m[i]*dT[j][2]/dT[j][i]
         C[i]=C[3]+2.5/6.7*(C[3]-900)
        else:
         C2[j][i]=Ccu*mcu/m[i]*dT[j][2]/dT[j][i]
        print(C2[j][i]*M[i]/R,"  " ,dT[j][i])
        j=j+1
    i=i+1 
q=Ccu*mcu/6.7*(461)*(1420-1285)  
print(q)
T=506.01
S=q*m[3]/T/10**(6)
Sm=q*M[3]/T/10**3
print(S)
print(Sm)