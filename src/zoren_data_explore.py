#%% Import packages

import pandas as pd
import os
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.dates import HourLocator
from datetime import datetime

#%% Read in data

# Set cwd
path = "C:\\Users\\AUZL503978\\Desktop\\UNSW\\2023_H2_ZZSC9020\\data"
os.chdir(path)

# Total demand data
demand_data = pd.read_csv("totaldemand_nsw.csv")
demand_data["DATETIME"] = pd.to_datetime(demand_data["DATETIME"])
demand_data = demand_data[["DATETIME", "TOTALDEMAND"]]

# Temperature data
temperature_data = pd.read_csv("temperature_nsw.csv")
temperature_data["DATETIME"] = pd.to_datetime(temperature_data["DATETIME"])
temperature_data = temperature_data[["DATETIME", "TEMPERATURE"]]

# Forecast demand data
forecast_data = pd.read_csv("forecastdemand_nsw.csv")
forecast_data["DATETIME"] = pd.to_datetime(forecast_data["DATETIME"])
forecast_data["LASTCHANGED"] = pd.to_datetime(forecast_data["LASTCHANGED"])
forecast_data = forecast_data[["DATETIME", "FORECASTDEMAND", "PREDISPATCHSEQNO", "PERIODID", "LASTCHANGED"]]

# PV installation data
pv_install_data = pd.read_csv("pv_installation_nsw.csv")
pv_install_data["Date"] = pd.to_datetime(pv_install_data["Date"])

#%% Data Cleaning

# Temperature data
temp_idx = temperature_data[temperature_data["TEMPERATURE"] < -50].index
for idx in temp_idx[:4]:
    temperature_data["TEMPERATURE"][idx] = np.mean([temperature_data["TEMPERATURE"][idx-1], temperature_data["TEMPERATURE"][idx+1]])

for idx in temp_idx[4:]:
    temperature_data["TEMPERATURE"][idx] = np.NaN

temperature_data["TEMPERATURE"] = temperature_data["TEMPERATURE"].interpolate()

#%% Data Transformation

demand_temp_data = pd.merge(demand_data, temperature_data, on=["DATETIME"], how="left")
demand_temp_data["TEMPERATURE"] = demand_temp_data["TEMPERATURE"].interpolate()

#%% EDA 1: Daily peaks

#%%% Get daily peak data

# Find daily peak demand
## 1) Find index of peak demand by date
daily_peak_demand_idx = demand_data.groupby([demand_data['DATETIME'].dt.date])["TOTALDEMAND"].idxmax()
## 2) Filtre dataframe to select the max indices
daily_peak_demand = demand_data.loc[daily_peak_demand_idx].reset_index(drop=True)

# Find daily peak temperature
## 1) Find index of peak temperature by date
daily_peak_temperature_idx = temperature_data.groupby([temperature_data['DATETIME'].dt.date])["TEMPERATURE"].idxmax()
## 2) Filtre dataframe to select the max indices
daily_peak_temperature = temperature_data.loc[daily_peak_temperature_idx].reset_index(drop=True)


# Group by day of week

temp_min = demand_data.groupby(demand_data['DATETIME'].dt.weekday).min()
temp_mean = demand_data.groupby(demand_data['DATETIME'].dt.weekday).mean()
temp_max = demand_data.groupby(demand_data['DATETIME'].dt.weekday).max()

weekday_df["MIN"] = 

#%%% Plotting

# Plot of peak demand over time
daily_peak_demand.plot(x="DATETIME", y="TOTALDEMAND", style='o', ms=1)


# Plot of peak demand time for each day
y = daily_peak_demand['DATETIME'].apply(lambda x: x.replace(year=1901, month=1, day=1)).tolist()
ax = plt.subplot()
ax.plot(daily_peak_demand["DATETIME"].dt.date, y, "o", ms=1)
ax.yaxis.set_major_locator(HourLocator())
ax.yaxis.set_major_formatter(DateFormatter('%H:%M'))
ax.set_ylim([datetime(1901,1,1,0,0,0), datetime(1901,1,1,23,59,59)])


#


#%% EDA 2: PV uptake

#%%% Merging data

# Get monthly averaged temperature and demand data
demand_temp_monthly_avg_data = demand_temp_data.groupby([(demand_temp_data['DATETIME'].dt.year), (demand_temp_data['DATETIME'].dt.month)])[["TOTALDEMAND", "TEMPERATURE"]].mean()
demand_temp_monthly_avg_data.index=demand_temp_monthly_avg_data.index.rename(['YEAR', 'MONTH'])

# Merge with PV install cumsum data

# Get new index, which is merge of year and month
new_idx = ['-'.join([str(n[0]), str(n[1])]) for n in demand_temp_monthly_avg_data.index]

demand_temp_monthly_avg_data["DATETIME"] = new_idx
demand_temp_monthly_avg_data["DATETIME"] = pd.to_datetime(demand_temp_monthly_avg_data["DATETIME"])
demand_temp_monthly_avg_data = demand_temp_monthly_avg_data.reset_index(drop=True)

# Merge demand, temperature with PV uptake
demand_temp_PV_data = pd.merge(demand_temp_monthly_avg_data, pv_install_data, left_on=["DATETIME"], right_on=["Date"], how="inner")
demand_temp_PV_data = demand_temp_PV_data.drop('Date', axis=1)

demand_temp_PV_data.to_csv('demand_temp_PV_data.csv', index=False)

#%%% Plotting



    
    


