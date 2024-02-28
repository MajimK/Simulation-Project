import pandas as pd
import numpy as np

def Statistic(path):
    data=pd.read_excel(path)
    mean=data.mean()
    mean_values = mean.values.tolist()
    mean_column= data.columns.to_list()

    S=[]
    d=[]
    variance=0

    for i,value in enumerate(mean_column):
        count=0
        for element in data[value]:
            if np.isnan(element):continue
            result=(element-mean_values[i])**2
            variance+=result
            count+=1
        variance/=count-1
        d.append(np.sqrt(variance)*np.sqrt(count/(count-1)))
        S.append(np.sqrt(variance))

    with open(path + '.txt','w') as file:
        for element in mean_values:
            file.write(str(element) + '\n')
        file.write('\n')
        for element in S:
            file.write(str(element) + '\n')
