import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import random
def read (X):
    dat = pd.read_csv( X, sep=r"\s+", header=0)
    dat=dat.to_numpy()
    return dat
def minimum(X1):
    X=read(X1)
    shape = X.shape
    colums=shape[1]
    rows=shape[0]
    F=np.zeros(rows)
    f=np.zeros(rows)
    l1=1
    l2=1
    
    for i in range(rows):
      f[i]=X[i][1]
      F[i]=X[i][0]
    for i in range(rows-1):
      if i >=1:
         if f[i]<=min(f)+5:
          if f[i]<=f[i-1]:
              if f[i]<=f[i+1]:
                  
                   print("минимум №", l1, " интенсивность = ", f[i], "градусы = ", F[i])
                   l1=l1+1
      if i >=1:
         if f[i]>= max(f)-5:
          if f[i]>=f[i-1]:
              if f[i]>=f[i+1]:
                  
                    print("максимум №", l2, " интенсивность = ", f[i], "градусы = ", F[i])
                    l2=l2+1
print("L/2")    
minimum('e2p4.txt')
print("L/4")    
minimum('e3p3.txt')
print("неизвестная")
minimum('e5p4.txt')
print("упр 4")
minimum('e4p1.txt')
def polarplote1(X1):
    X=read(X1)
    shape = X.shape
    colums=shape[1]
    rows=shape[0]
    F=np.zeros(rows)
    f=np.zeros(rows)
    f2=np.zeros(rows)
    for i in range(rows):
      f[i]=X[i][1]
      F[i]=X[i][0]/360*2*np.pi
      f2[i]=np.cos(F[i])**2*200
    plt.subplot( polar=True)     
    plt.plot(F, f, label="эксперементальная зависимость")
    plt.plot(F, f2, label="cos^2(a)")
    plt.legend(["эксперементальная зависимость", "cos^2(a)"])
    plt.show()
    
polarplote1('e1p4.txt')
def polarplote2(X1):
    X=read(X1)
    shape = X.shape
    colums=shape[1]
    rows=shape[0]
    F=np.zeros(rows)
    f=np.zeros(rows)
    for i in range(rows):
      f[i]=X[i][1]
      F[i]=X[i][0]/360*2*np.pi
    

    plt.subplot( polar=True)   
    plt.plot(F, f, label="эксперементальная зависимость")
    plt.legend(["эксперементальная зависимость", "теоретич. элипс"])
    plt.show()
print("упр 4")
minimum('e4p1.txt')
polarplote2('e4p1.txt')   