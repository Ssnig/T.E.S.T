import numpy as np
import pandas as pd
from pandas import Series, DataFrame


series=Series([1,2,3,4,5],index=['q','w','e','r','t'])

print(series)
print("elements",series.values)
print("index",series.index)


data= {'ID':['100','101','102','103','104'],
       'City':['Tokyo','Osaka','Kyoto','Hokkaaido','Tokyo'],
       'Birth Year':[1990,1989,1992,1997,1982],
       'Name':['Hiroshi','Akiko','Yuki','Satoru','Steve']}
df = DataFrame(data)

print(df.head())

df_i=DataFrame(data,index=['a','b','c','d','e'])
print(df_i)

print('elements',df_i.values)
print('index',df_i.index)
print('columns',df_i.columns)