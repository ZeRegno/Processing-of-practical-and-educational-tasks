import matplotlib.pyplot as plt
import math
from math import pi as pi
from numpy import zeros,exp,sin, linspace, meshgrid,empty,cos,arctan,tan,max,min
from numpy.linalg import norm
from matplotlib.pyplot import plot, figure, axes, show, subplot
from sympy import symbols,diff,exp,atan,tan
#----------------------------------Input
x_l=0;x_r=pi
y_l=0;y_r=3
t_begin=0;t_end=10

J=40;N=40;M=40
Time_show=[4]
a_c=1
Type_boundary_condition_X=[0,0] # условие Дирихле == 0
Type_boundary_condition_Y=[0,0] # условие Неймана == 1
def cz(i):
    f=(i*pi)**2/9+1
    return f
def norm_xy(i):
    f=2*(1-cos(i*pi))/i/pi
    return f
def fourier_t(t,i):
    f=1/(cz(i)**2+1)*(exp(-cz(i)*t)+cz(i)*sin(t)-cos(t))
    return f
def Function_analysis(t,x,y):
    I=50
    sum=0 # i=0
    for i in range(1,I,1):
        sum=(sum+fourier_t(t,i)*norm_xy(i)*
             sin(x)*sin(i*pi*y/3))
    return sum
def Function_begin(x,y):
    f=0
    return f
def Function_right(t,x,y):
    f=sin(x)*sin(t)
    return f
#----------------------------------Def
def Choic_type_boundary_condition_X_for_scheme(type_l,type_r):
    x=zeros(N+1)
    if type_l==0 and type_r==0:
        h=(x_r-x_l)/N
        for n in range(N+1):
            x[n]=x_l+n*h
    if type_l==1 and type_r==0:
        h=(x_r-x_l)/(N-1/2)
        for n in range(N+1):
            x[n]=x_l-h/2+n*h
    if type_l==0 and type_r==1:
        h=(x_r-x_l)/(N-1/2)
        for n in range(N+1):
            x[n]=x_l+n*h
    if type_l==1 and type_r==1:
        h=(x_r-x_l)/(N-1)
        for n in range(N+1):
            x[n]=x_l-h/2+n*h
    return x,h
def Choic_type_boundary_condition_Y_for_scheme(type_l,type_r):
    y=zeros(M+1)
    if type_l==0 and type_r==0:
        l=(y_r-y_l)/M
        for n in range(M+1):
            y[n]=y_l+n*l
    if type_l==1 and type_r==0:
        l=(y_r-y_l)/(M-1/2)
        for n in range(M+1):
            y[n]=y_l-l/2+n*l
    if type_l==0 and type_r==1:
        l=(y_r-y_l)/(M-1/2)
        for n in range(M+1):
            y[n]=y_l+n*l
    if type_l==1 and type_r==1:
        l=(y_r-y_l)/(M-1)
        for n in range(M+1):
            y[n]=y_l-l/2+n*l
    return y,l
def Layer_Time():
    t = zeros(J + 1)
    tau = (t_end - t_begin) / J
    for j in range(J + 1):
        t[j] = t_begin + j * tau
    return t,tau
def graph_function_analysis(u,ax_zmax,ax_zmin,time_show):
    fig = figure()
    ax = axes(projection='3d')
    X, Y = meshgrid(y, x)
    ax.plot_surface(X, Y, u, rstride=1, cstride=1, cmap='magma')
    ax.set_title('Аналитическое решение t={0}'.format(time_show*tau))
    ax.set_ylim(x_l-0.2,x_r)
    ax.set_xlim(y_l,y_r+0.2)
    show()
    return
def Slove_progonka(N,a,b,c,parameter,f):
#   parameter[0)f0 1)fN 2)b0 3)aN 4)c0 5)cN]  ; a=a_i b=b_i c=c_i f=f_i
    Y=zeros(N+1)
    alpha=zeros(N)
    beta=zeros(N)
    alpha[0]=parameter[2]/(-parameter[4])
    beta[0]=parameter[0]/parameter[4]
# прямой ход прогонки:
    for n in range(0,N-1,1):
        alpha[n+1]=b/(-c-a*alpha[n])
        beta[n+1]=(a*beta[n]-f[n+1])/(-c-a*alpha[n])
# обратный ход прогонки:
    Y[N]=(-parameter[1]+parameter[3]*beta[N-1])/(-parameter[5]-parameter[3]*alpha[N-1])
    for n in range(N-1,-1,-1):
        Y[n]=alpha[n]*Y[n+1]+beta[n]
    return Y
def Choic_type_boundary_condition_for_progonka_parameter(type_l,type_r):
#   parameter[0)f0 1)fN 2)b0 3)aN 4)c0 5)cN]  ; a=a_i b=b_i c=c_i f=f_i
    parameter=zeros(6)
    if type_l==0 and type_r==0:
        parameter=[0,0,0,0,1,1]
    if type_l==1 and type_r==0:
        parameter=[0,0,1,0,-1,1]
    if type_l==0 and type_r==1:
        parameter = [0, 0, 0,-1, 1, 1]
    if type_l==1 and type_r==1:
        parameter = [0, 0, 1, -1, -1, 1]
    return parameter
def graph_function_numberals(u,ax_zmax,ax_zmin,time_show):
    fig = figure()
    ax = axes(projection='3d')
    X, Y = meshgrid(y, x)
    ax.plot_surface(X, Y, u, rstride=1, cstride=1, cmap='magma')
    ax.set_title('Численное решение t={0}'.format(time_show*tau))
    ax.set_ylim(x_l-0.2,x_r)
    ax.set_xlim(y_l,y_r+0.2)
    show()
    return
def graph_function_errors(u,time_show):
    fig = figure()
    ax = axes(projection='3d')
    X, Y = meshgrid(y, x)
    ax.plot_surface(X, Y, u, rstride=1, cstride=1, cmap='magma')
    ax.set_title('Погрешности t={0}'.format(time_show*tau))
    ax.set_ylim(x_l-0.2,x_r)
    ax.set_xlim(y_l,y_r+0.2)
    show()
    return

#----------------------------------Схема
x,h=Choic_type_boundary_condition_X_for_scheme(Type_boundary_condition_X[0],Type_boundary_condition_X[1])
y,l=Choic_type_boundary_condition_Y_for_scheme(Type_boundary_condition_Y[0],Type_boundary_condition_Y[1])
t,tau=Layer_Time()
#----------------------------------Аналитическое решение
U_analysis=zeros(((J+1,N+1,M+1)))
for j in range(J+1):
    for n in range(N + 1):
        for m in range(M + 1):
            U_analysis[j,n,m]=Function_analysis(t[j],x[n],y[m])
ax_zmax=max(U_analysis) ; ax_zmin=min(U_analysis)

#----------------------------------Численное решение
W_integer=zeros(((J+1,N+1,M+1)))
W_half=zeros(((J+1,N+1,M+1)))
f_right=zeros(((J+1,N+1,M+1)))
for n in range(N + 1):
    for m in range(M + 1):
        W_integer[0,n,m]=Function_begin(x[n],y[m])
paramater_X=Choic_type_boundary_condition_for_progonka_parameter(Type_boundary_condition_X[0],Type_boundary_condition_X[1])
paramater_Y=Choic_type_boundary_condition_for_progonka_parameter(Type_boundary_condition_Y[0],Type_boundary_condition_Y[1])

for j in range(J):
    for n in range(N+1):
        for m in range(M+1):
            f_right[j,n,m]=tau/2*Function_right(t[j]+0.5*tau,x[n],y[m])
    for m in range(1,M,1):
        fi_x=zeros(N+1)
        fi_x[:]=-(W_integer[j,:,m]+0.5*a_c*tau/l**2*(W_integer[j,:,m+1]-2*W_integer[j,:,m]+W_integer[j,:,m-1])+f_right[j,:,m])
        W_half[j,:,m]=Slove_progonka(N,0.5*a_c*tau/h**2,0.5*a_c*tau/h**2,-(a_c*tau/h**2+1),paramater_X,fi_x)[:]
    for n in range(1,N,1):
        fi_y=zeros(M+1)
        fi_y[:]=-(W_half[j,n,:]+0.5*a_c*tau/h**2*(W_half[j,n+1,:]-2*W_half[j,n,:]+W_half[j,n-1,:])+f_right[j,n,:])
        W_integer[j+1,n,:]=Slove_progonka(M,0.5*a_c*tau/l**2,0.5*a_c*tau/l**2,-(a_c*tau/l**2+1),paramater_Y,fi_y)[:]
for j in range(1,J+1,1):
    for m in range(0,M+1,1):
        W_integer[j,0,m]=Type_boundary_condition_X[0]*W_integer[j,1,m]
        W_integer[j,N,m]=Type_boundary_condition_X[1]*W_integer[j,N-1,m]
U_numberals=W_integer
Errors=U_numberals-U_analysis


graph_function_analysis(U_analysis[Time_show[0]],ax_zmax,ax_zmin,Time_show[0])
graph_function_numberals(U_numberals[Time_show[0]],ax_zmax,ax_zmin,Time_show[0])
graph_function_errors(Errors[Time_show[0]],Time_show[0])
