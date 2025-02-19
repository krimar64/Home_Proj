import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

content = pd.read_csv(r"c:\Users\ekrrmai\OneDrive - Ericsson\Ericsson\Python_Home\RTEP\SpuriousEmission\TcTxSpuriousMeasK50_2022-12-14-16_10_56.xlsx",index_col=False  ,header=43)
rows,columns = content.shape
