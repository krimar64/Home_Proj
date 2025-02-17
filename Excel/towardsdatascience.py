# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 07:58:35 2020

@author: ekrrmai
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
Sales = pd.read_excel('https://github.com/datagy/mediumdata/raw/master/pythonexcel.xlsx', sheet_name = 'sales')
States = pd.read_excel('https://github.com/datagy/mediumdata/raw/master/pythonexcel.xlsx', sheet_name = 'states')
print()
print(Sales)
print()
print(States)
print()
print(Sales.head())
print()
df1 = pd.DataFrame(Sales)
df2 = pd.DataFrame(States)
print(df1)
print()
print(df2)

df['MoreThan500'] = ['Yes' if x > 500 else 'No' for x in df1]