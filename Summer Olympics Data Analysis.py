import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('I:/internship/summer.csv')
df.head()
df

len(df['City'].unique())
df['City'].unique()

data=df.values
data
data[15632][2]
lst=[]
for Sport in df['Sport'].unique():
    count=0
    for i in range(len(data)):
        if(data[i][2]==Sport):
            if(data[i][8]=='Gold'):
                count+=1
    lst.append([Sport,count])
lst
pd.DataFrame(lst,columns = ['Sport','Medal']).sort_values(by='Medal', ascending=False).head()
pd.DataFrame(lst,columns = ['Sport','Medal']).sort_values(by='Medal', ascending=False).head().plot(x = 'Sport', y = 'Medal', kind = 'bar', figsize = (5,5))
data[0][8]
df['Medal']=='Gold'
df[df['Medal']=='Gold']
df['Medal'].unique()
data=[]
for Sport in df[df['Medal']=='Gold']:
    data.append([Sport, len(df[df['Medal']=='Gold'])])
    data=[]
for Sport in df['Sport'].unique():
    data.append([Sport , len(df[df['Medal'] == 'Gold' ])])
    df['Sport'].unique()
    
data=df.values
data
lst=[]
for Sport in df['Sport'].unique():
    count=0
    for i in range(len(data)):
        if(data[i][2]==Sport):
                count+=1
    lst.append([Sport,count])
    lst
    pd.DataFrame(lst,columns = ['Sport','Medal']).sort_values(by='Medal', ascending=False).head()
    pd.DataFrame(lst,columns = ['Sport','Medal']).sort_values(by='Medal', ascending=False).head().plot(x = 'Sport', y = 'Medal', kind = 'bar', figsize = (5,5))
    pd.DataFrame(lst,columns = ['Sport','Medal']).sort_values(by='Medal', ascending=False)
    pd.DataFrame(lst,columns = ['Sport','Medal']).sort_values(by='Medal', ascending=False).plot(x = 'Sport', y = 'Medal', kind = 'bar', figsize = (10,7))

data=df.values
data
for Year in df['Year'].unique():
    count=0
    for i in range(len(data)):
        if(data[i][0]==Year):
            if(data[i][5]=='IND')&(data[i][8]=='Gold'):
                print(data[i][0])
                break

data=df.values
data
lst=[]
for Athlete in df['Athlete']:
    count=0
    for i in range(len(data)):
        if(data[i][8]=='Gold'):
            if(data[i][4] == Athlete):
                count+=1
    lst.append([Athlete,count])
    df['Athlete'].unique()
    lst
