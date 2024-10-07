#%matplotlib notebook
import matplotlib.pyplot as plt
import math
from math import pi as pi
from numpy import zeros,exp,sin, linspace, meshgrid,empty,arctan,tan,cos,log
from numpy.linalg import norm
from matplotlib.pyplot import plot, figure, axes, show, subplot
from sympy import symbols,diff,exp,atan,tan,sin,cos,integrate


#---------------------------------Input
t_0 = 0; T = 0.3  #0.3
x_0 = 0; x_N =-1


N=50;J=50


def B_function(u):
    f=-2*exp(2*u)/(exp(2*u)+1)
    return f
def X0_function(t):
    f=0
    return f
def T0_function(x):
    f=sin(pi*x)
    return f
def F_U(u):
    f=-log(float(exp(2*u) + 1))
    return f
a=symbols('u')
f_u=integrate(B_function(a))
print(f_u)
#----------------------------------Def
def Chara_T0_line(t,x0,t0): #t0=0
    x=B_function(T0_function(x0))*(t-t0)+x0
    return x
def Chara_X0_line(t,x0,t0): #x0=0
    x=B_function(X0_function(t0))*(t-t0)+x0
    return x


k_boundary=B_function(T0_function(0))




def graph_function_analysis(y):
    fig = figure(figsize=(4,4))
    ax = axes(projection='3d')
    axX, axT = meshgrid(x, t)
    ax.plot_surface(axX, axT, y, rstride=1, cstride=1, cmap='magma')
    ax.set_title('Аналитическое решение')
    
    ax.set_xlabel("X")
    ax.set_ylabel("t")
    ax.set_zlabel("U(x, t")
    show()
    return
def graph_function_numberals(y):
    fig = figure()
    ax = axes(projection='3d')
    axX, axT = meshgrid(x, t)
    ax.plot_surface(axX, axT, y, rstride=1, cstride=1, cmap='magma')
    ax.set_title('Численное решение')
    ax.set_xlabel("X")
    ax.set_ylabel("t")
    ax.set_zlabel("U(x, t")
    show()
    return
def graph_function_errors(y):
    fig = figure()
    ax = axes(projection='3d')
    axX, axT = meshgrid(x, t)
    ax.plot_surface(axX, axT, y, rstride=1, cstride=1, cmap='magma')
    ax.set_title('Погрешности')
    ax.set_xlabel("X")
    ax.set_ylabel("t")
    ax.set_zlabel("погрешность U(x, t")
    show()
    return


#--------------
def FT0(x0, t0, x, t):
    f = B_function(T0_function(x0)) * (t - t0) + x0 - x
    return f
def FX0(x0, t0, x, t):
    f = B_function(X0_function(t0)) * (t - t0) + x0 - x
    return f
def Newton_slove_Chara_line(x,t):   #(x,t)=(x[i],t[j])
    if x_N<x_0:
        eps=0.001;i_max=50
        a = symbols('a')
        if x/t<k_boundary:
            c0 = empty(i_max+1)
            c0[0] = 0.5
            f=FT0(a,0,x,t)
            for i in range(i_max):
                m=0
                c0[i + 1] = (c0[i] - f.subs(a, c0[i]) / diff(f, a).subs(a, c0[i])).evalf()
                if i>=1 and abs((c0[i+1]-c0[i])/(1-((c0[i+1]-c0[i])/(c0[i]-c0[i-1]))))<eps:
                    m=i+1
                    break
            t0_or_x0=c0[m]
            au=T0_function(t0_or_x0)
        if x/t>=k_boundary:
            c0 = empty(i_max+1)
            c0[0] = 0.5
            f=FX0(0,a,x,t)
            for i in range(i_max):
                m=0
                c0[i + 1] = (c0[i] - f.subs(a, c0[i]) / diff(f, a).subs(a, c0[i])).evalf()
                if i>=1 and abs((c0[i+1]-c0[i])/(1-((c0[i+1]-c0[i])/(c0[i]-c0[i-1]))))<eps:
                    m=i+1
                    break
            t0_or_x0=c0[m]
            au=X0_function(t0_or_x0)
        return au,t0_or_x0
    if x_N>x_0:
        eps=0.001;i_max=500
        a = symbols('a')
        if x/t>=k_boundary:
            c0 = empty(i_max+1)
            c0[0] = 0.5
            f=FT0(a,0,x,t)
            for i in range(i_max):
                m=0
                c0[i + 1] = (c0[i] - f.subs(a, c0[i]) / diff(f, a).subs(a, c0[i])).evalf()
                if i>=1 and abs((c0[i+1]-c0[i])/(1-((c0[i+1]-c0[i])/(c0[i]-c0[i-1]))))<eps:
                    m=i+1
                    break
            t0_or_x0=c0[m]
            au=T0_function(t0_or_x0)
        if x/t<k_boundary:
            c0 = empty(i_max+1)
            c0[0] = 0.5
            f=FX0(0,a,x,t)
            for i in range(i_max):
                m=0
                c0[i + 1] = (c0[i] - f.subs(a, c0[i]) / diff(f, a).subs(a, c0[i])).evalf()
                if i>=1 and abs((c0[i+1]-c0[i])/(1-((c0[i+1]-c0[i])/(c0[i]-c0[i-1]))))<eps:
                    m=i+1
                    break
            t0_or_x0=c0[m]
            au=X0_function(t0_or_x0)
        return au,t0_or_x0
#print(Newton_slove_Chara_line(0.06,0.03)[0])

#---------------------------------


h=(x_N-x_0)/N ; tau=(T-t_0)/J
x=zeros(N+1);t=zeros(J+1)
for i in range(N+1):
    x[i]=x_0+i*h
for j in range(J+1):
    t[j]=t_0+j*tau



#---------------------------------Характеристики

N0=10;J0=10
h0=(x_N-x_0)/N0 ; tau0=(T-t_0)/J0
x0=zeros(N0+1);t0=zeros(J0+1)
for i in range(N0+1):
    x0[i]=x_0+i*h0
for j in range(J0+1):
    t0[j]=t_0+j*tau0
    
    
#--------

chara_X0_x=zeros((J+1,J0+1))
for j0 in range(J0+1):
    for j in range(J+1):
        chara_X0_x[j,j0]=Chara_X0_line(t[j],0,t0[j0])
        
        
chara_T0_x=zeros((J+1,N0+1))
for i0 in range(N0+1):
    for j in range(J+1):
        chara_T0_x[j,i0]=Chara_T0_line(t[j],x0[i0],0)
        
#--------
#Вывод Характеристик
fig = figure(figsize=(4, 4))
if x_N>x_0:
    ax = axes(xlim=(t_0,T), ylim=(x_0,x_N))
if x_N<x_0:
    ax = axes(xlim=(t_0,T), ylim=(x_N,x_0))
 
ax.set_xlabel('t'); ax.set_ylabel('x');
ax.set_title('Характеристики')
for i0 in range(N0+1):
    plt.plot(t, chara_X0_x[:,1:i0],color='red')
for j0 in range(J0+1):
    plt.plot(t, chara_T0_x[:,1:j0],color='blue')
for i0 in range(N0+1):
    plt.plot(t, chara_X0_x[:,0],color='green')
plt.show()


#----------------------------------Аналитическое решение
u_analysis=zeros((N+1,J+1))
for i in range(1,N+1,1):
    for j in range(1,J+1,1):
        u_analysis[i,j]=Newton_slove_Chara_line(x[i],t[j])[0]
for i in range(0, N + 1, 1):
    u_analysis[i,0]=T0_function(x[i])
for j in range(0, J + 1, 1):
    u_analysis[0,j]=X0_function(t[j])
graph_function_analysis(u_analysis)

#----------------------------------Численное решение
def F_i1_j1_(x):
    f=x/2/tau+F_U(x)/2/h
    return f
def Diff_F_i1_j1_(x):
    f=1/2/tau+B_function(x)/2/h
    return f
def F_ij_(y_i_j,y_i1_j,y_i_j1):
    f=(y_i_j1-y_i1_j-y_i_j)/2/tau+(F_U(y_i1_j)-F_U(y_i_j1)-F_U(y_i_j))/2/h
    return f
def Solve_Hewton( y_i_j , y_i1_j , y_i_j1):
    eps=0.001;i_max=50
    c = empty(i_max + 1)
    c[0]=y_i_j
    m=0
    for i in range(i_max):
        c[i+1]=c[i]-(F_i1_j1_(c[i])+F_ij_(y_i_j,y_i1_j,y_i_j1))/Diff_F_i1_j1_(c[i])
        if i >= 1 and  abs((c[i + 1] - c[i]) / (1 - ((c[i + 1] - c[i]) / (c[i] - c[i - 1])))) < eps:
            m = i + 1
            break
    nu=c[m]
    return nu
def SOLVE(N):
    J=N
    t_0 = 0; T = 0.3  #0.3
    x_0 = 0; x_N =-1
    h=(x_N-x_0)/N ; tau=(T-t_0)/J
    x=zeros(N+1);t=zeros(J+1)
    for i in range(N+1):
        x[i]=x_0+i*h
    for j in range(J+1):
        t[j]=t_0+j*tau


    y1=zeros((N+1,J+1))
    for i in range(0, N + 1, 1):
        y1[i,0]=T0_function(x[i])
    for j in range(0, J + 1, 1):
        y1[0,j]=X0_function(t[j])
    for j in range(0, J, 1):
        for i in range(0, N, 1):
            y1[i+1,j+1]=Solve_Hewton(y1[i,j],y1[i+1,j],y1[i,j+1])
    

    T_need=0.1
    j_need=int(T_need/tau)-1
    X=zeros(len(x))
    U=zeros(len(x))
    for i in range(len(x)):
     U[i]=y1[i, j_need]
     X[i]=x[i]
    return X, U, y1;

X10, U10, y1=SOLVE(10)
X20, U20, y1=SOLVE(20)

X40, U40, y1=SOLVE(40)
X80, U80, y1=SOLVE(80)

plt.plot(X10,U10) #строим для разных сеток u(x)
plt.plot(X20,U20)

plt.plot(X40,U40)
plt.plot(X80,U80)

plt.legend (fontsize=15, shadow=True, framealpha=1)
plt.xlabel('x')
plt.ylabel('u')
plt.legend (["10", "20", "40", "80"])
plt.grid()
STR_NAME="график при сгущении сетки, при T=0.1"
plt.title(STR_NAME)



u_numberals=y1
Errors=u_numberals-u_analysis
graph_function_numberals(u_numberals)
graph_function_errors(Errors)
