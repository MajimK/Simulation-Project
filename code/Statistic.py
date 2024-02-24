import pandas as pd
import numpy as np

path='Datos\\Datos_n=3_T=10_p=0.7.xlsx'

data=pd.read_excel(path)
mean=data.mean()
mean_values = mean.values.tolist()
mean_column= data.columns.to_list()

todo=[]
desviacion_poblacional=[]
variance=0

for i,value in enumerate(mean_column):
    count=0
    for element in data[value]:
        if np.isnan(element):continue
        result=(element-mean_values[i])**2
        variance+=result
        count+=1
    variance/=count-1
    desviacion_poblacional.append(np.sqrt(variance)*np.sqrt(count/(count-1)))
    todo.append(np.sqrt(variance))

print(desviacion_poblacional)
print(todo)
#print(mean_values)