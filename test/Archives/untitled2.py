

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 08:59:16 2020

@author: PC_Nt
"""
# 

import pickle 
import pandas as pd
import csv

pickle_in = open("0.05_0.05_0.05_0.05.pkl","rb")
example_dict = pickle.load(pickle_in)
print(example_dict)

df = pd.DataFrame.from_dict(data=example_dict, orient='index')
df.transpose().to_csv("CentralDB_50terminals.csv")


df = pd.read_csv('CentralDB_50terminals.csv')
for id in range(0,10):
    df_id = df[df['id'] == id]
    file_name = str(id) + '.csv'
    df_id.to_csv(file_name)
