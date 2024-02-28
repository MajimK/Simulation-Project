from Sim import Simulation
from Extract_samples import Copy_Xslx, Extract
import pandas as pd
from Statistic import Statistic

count=0
n=20
T=50
p=0.9
time=[]
out=[]
jump=[]
arrival=[]
path='Datos\\Datos_n='+str(n)+'_T='+str(T)+'_p='+str(p)+'.xlsx'
while count<150:
    count+=1
    output=Simulation(n,T,p)
    values=Extract(output,time,out,jump,arrival)
    time=values[0]
    out=values[1]
    jump=values[2]
    arrival=values[3]

Copy_Xslx(time,out,jump,arrival,path)
Statistic(path)

