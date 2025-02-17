# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

content = pd.read_csv("c:\Users\Krister\csv_python\K4G32001GF_head.csv")
demo = pd.read_csv("demo1.csv")
demo

header = content.head(10)
current_data=content.loc[11:31, :]
LoLeak1_data=content[content['testname'].str.contains("LOleak1")]
LoLeak2_data=content[content['testname'].str.contains("LOleak2")]
LoLeak3_data=content[content['testname'].str.contains("LOleak3")]
LoLeak4_data=content[content['testname'].str.contains("LOleak4")]
LoLeak5_data=content[content['testname'].str.contains("LOleak5")]
LoLeak6_data=content[content['testname'].str.contains("LOleak6")]

LoLeak6_data

LoLeak6V_data=LoLeak6_data[LoLeak6_data['testname'].str.contains("TxV")]
LoLeak6H_data=LoLeak6_data[LoLeak6_data['testname'].str.contains("TxH")]

LoLeak6V_data
LoLeak6H_data

plt.plot(LoLeak6H_data.testname,LoLeak6V_data.IC1)
plt.plot(LoLeak6V_data.testname,LoLeak6V_data.IC1)