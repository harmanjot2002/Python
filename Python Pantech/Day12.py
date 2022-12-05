"""
Data Frame:
1.It is a two dimensional array with different data elements(i.e.,it is a heterogeneous collection of data elements)
2.Data is stored in a tabular format in the form of rows and columns.
Data Frame Creation:
1.A pandas dataframe can be created by using various inputs like:
    -Lists
    -Dict
    -Series
    -Numpy adarrays
    -Another DataFrame
"""

import pandas as pd
df=pd.DataFrame()
print(df)
"""
O/P:Empty DataFrame
    Columns: []    
    Index: []  
"""

lst=['sun','earth','mars','venus','moon']
Df=pd.DataFrame(lst)
print(Df)
"""
           0
    0    sun
    1  earth
    2   mars
    3  venus
    4   moon
"""

data=[['Ros',10],['Popy',12],['Sunny',13]]
df1=pd.DataFrame(data,columns=['Name','Age'])
print(df1)
"""
        Name  Age
    0    Ros   10
    1   Popy   12
    2  Sunny   13
"""

data1={'Name':['Tom','Sam','Ricky','Steve'],'Age':[28,34,29,42]}
df2=pd.DataFrame(data1)
print(df2)
"""
        Name  Age
    0    Tom   28
    1    Sam   34
    2  Ricky   29
    3  Steve   42
"""

#A Series is like a fixed-size dict.
s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s['a'])
#O/p:1


