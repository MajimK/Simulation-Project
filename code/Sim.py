import numpy as np
import csv
import pandas as pd
from openpyxl import Workbook
            

def Simulation(n:int,T:int,p:float):
    """
    Simulation function: simulate a server process with n serves connected in series
    n: Number of server
    T: Open time
    p: Regress probability. Preferably use a value greater than 0.5

    """

    arrival=[]
    serves_queue=[]
    wait_time=[]
    jump_number=[]

    for i in range(n):
        serves_queue.append(0)
        wait_time.append(99999)
        arrival.append({})
        jump_number.append(0)
    
    arrival_time=time=extra_time=arrival_number=out_number=jump_forward=jump_back=0
    out={}

    while(True):
        art=np.random.exponential()
        arrival_time= time + art
        min_wt=min(wait_time)

        # Case 1
        if (arrival_time<min_wt and arrival_time <= T):
            time=arrival_time
            arrival_number+=1
            serves_queue[0]+=1
            arrival[0][arrival_number] = time

            if (serves_queue[0]==1):
                wrt=np.random.exponential()
                wait_time[0]=time + wrt
        
        # Case 2
        if(min_wt < arrival_time and min_wt <= T):
            serve=wait_time.index(min_wt)
            time=min_wt
            change_variable=np.random.uniform()
            serves_queue[serve]-=1

            if(change_variable>p):
                jump_number[serve]+=1
                while True:
                    change_variable=np.random.uniform(0,n)
                    chan_serve=int(change_variable)
                    if chan_serve==serve: continue

                    serves_queue[chan_serve]+=1
                    arrival[chan_serve][arrival_number - sum(serves_queue[:chan_serve])]=time
                    if(serves_queue[chan_serve]==1):
                        wrt=np.random.exponential()
                        wait_time[chan_serve]=time + wrt

                    if chan_serve>serve: 
                        jump_forward+=1
                        break
                    else: 
                        jump_back+=1
                        break

            elif(serve == n-1):
                out_number+=1
                out[out_number]=time

            else:
                serves_queue[serve +1]+=1
                arrival[serve + 1][arrival_number - sum(serves_queue[:serve+1])]=time
                if(serves_queue[serve +1]==1):
                    wrt=np.random.exponential()
                    wait_time[serve+1]=time + wrt
            
            if(serves_queue[serve]==0): 
                wait_time[serve]=99999
                continue

            wrt=np.random.exponential()
            wait_time[serve]=time+wrt

        # Case 3
        if(min(min_wt,arrival_time)>T and sum(serves_queue)!=0):
            serve=wait_time.index(min_wt)
            time=min_wt
            serves_queue[serve]-=1
            change_variable=np.random.uniform()

            if(change_variable>p):
                jump_number[serve]+=1
                while True:
                    change_variable=np.random.uniform(0,n)
                    chan_serve=int(change_variable)
                    if chan_serve==serve: continue

                    serves_queue[chan_serve]+=1
                    arrival[chan_serve][arrival_number - sum(serves_queue[:chan_serve])]=time
                    if(serves_queue[chan_serve]==1):
                        wrt=np.random.exponential()
                        wait_time[chan_serve]=time + wrt

                    if chan_serve>serve: 
                        jump_forward+=1
                        break
                    else: 
                        jump_back+=1
                        break

            elif(serve == n-1):
                out_number+=1
                out[out_number]=time

            else:
                serves_queue[serve +1]+=1
                arrival[serve + 1][arrival_number - sum(serves_queue[:serve+1])]=time
                if(serves_queue[serve +1]==1):
                    wrt=np.random.exponential()
                    wait_time[serve+1]=time + wrt
            
            if(serves_queue[serve]==0):
                wait_time[serve]=99999
                continue
            
            wrt=np.random.exponential()
            wait_time[serve]=time+wrt

        # Case 4
        if (min(min_wt,arrival_time)>T and sum(serves_queue)==0):
            extra_time=max(time-T,0)
            break

    return (time,extra_time,arrival,out,jump_number,jump_forward,jump_back)    
    
    
    
        




    







