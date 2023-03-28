# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 19:26:36 2023

@author: AUZL503978
"""

import pandas as pd
import os
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.dates import HourLocator
from datetime import datetime

path = "C:\\Users\\AUZL503978\\Desktop\\UNSW\\2023_H2_ZZSC9020\\data"
os.chdir(path)

#%% Find post code group with max PV output

df = pd.read_csv("Postcode time series.csv")
df_sum = df.groupby("Postcode").agg("sum") #21xx


#%% Group BoM rain data into single df



weather_station_ids = [
"066124",
"068242",
"066212",
"066194",
"067119",
"067019"
]


for n in range(len(weather_station_ids)):
    
    file_name = "IDCJAC0009_" + weather_station_ids[n] + "_1800_Data.csv"
    
    if n == 0:
        
        df = pd.read_csv(file_name)
        df = df.drop(columns=["Product code", "Period over which rainfall was measured (days)", "Quality"])
        df = df[df["Year"] >= 2010]
        df['Rainfall amount (millimetres)'] = df['Rainfall amount (millimetres)'].fillna(0)

    else:
        
        temp_df = pd.read_csv(file_name)
        temp_df = temp_df.drop(columns=["Product code", "Period over which rainfall was measured (days)", "Quality"])
        temp_df = temp_df[temp_df["Year"] >= 2010]
        temp_df['Rainfall amount (millimetres)'] = temp_df['Rainfall amount (millimetres)'].fillna(0)
        
        df = pd.concat([df, temp_df], ignore_index=True)

df.to_csv('NSW_BoM_Rainfall_Data.csv', index=False)

