import numpy as np
import matplotlib.pyplot as plt
import math
from tkinter import Tk, Label
import pandas as pd

def save(cosf, Ef1, Lf, dL): 
   plt.plot(cosf, Ef1, '.')
   plt.show()   
   name2='ДанныеАтомпрак11.xlsx'
   df = ({'1-cosф': list(cosf),
                   '1/Ef': list(Ef1),
                   'Lfэксп': list(Lf),
                   'dLfэксп': list(dL)})
   
   df = pd.DataFrame(data=df)
   writer=pd.ExcelWriter(name2, engine='xlsxwriter')
   df.to_excel(writer, sheet_name='Данные', index=False)
   writer.close()

f=[20/180*math.pi, 30/180*math.pi, 45/180*math.pi, 60/180*math.pi, 90/180*math.pi]
Vf=[552, 519, 426, 349, 247]
Ef=np.zeros(len(f))
Ef1=np.zeros(len(f))
cosf=np.zeros(len(f))
Lf=np.zeros(len(f))
dL=np.zeros(len(f))
R=0.965 #кЭв
h=4.136*10**(-15)
c=3*10**8
i=0
while i<= (len(f)-1):
    Ef[i]=R*Vf[i]
    Ef1[i]=1/Ef[i]
    cosf[i]=(1-np.cos(f[i]))
    Lf[i]=h*c/Ef[i]
    dL[i]=h*c*(1/Ef[i]-1/662)
    i=i+1
print(dL)

save(cosf, Ef1, Lf, dL)
    