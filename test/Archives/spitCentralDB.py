# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 01:44:09 2020

@author: PC_Nt
"""
import csv
import numpy as np
import pandas as pd
      
df = pd.read_csv('train_withid.csv')
for id in range(0,df['id'].max):
    df_id = df[df['id'] == id]
    file_name = str(id) + '.csv'
    df_id.to_csv(file_name)




