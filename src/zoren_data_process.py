#%% Import packages

import pandas as pd
import os

#%% Read in data

# Set cwd
path = "C:\\Users\\AUZL503978\\Desktop\\UNSW\\2023_H2_ZZSC9020\\data"
os.chdir(path)

sheet = "SGU-Solar"

years = [n for n in range(2008, 2021)]

files = [file for file in os.listdir() if '.xlsx' in file and "Postcode" in file]

solar_data = pd.DataFrame()

for n in range(len(files)):
    
    year = years[n]
    file = files[n]
    
    data = pd.read_excel(files[n])
    
    # Filtre to 2XXX
    data = pd.concat([data.head(2), data[data["Small Generation Unit (SGU) - Solar Panel (Deemed)"].str.startswith("2")]], ignore_index=True)
    
   
    if n == 0:
        
        temp_sum = data.iloc[2:,1:-2].sum()
        temp_sum = pd.DataFrame(temp_sum.values.reshape(-1, 2), columns = ['PV Quantity', 'PV Output kW'])
        
        temp_date_df = data.iloc[1,1:-2]
        temp_date_list = []
        temp_date_list.append('1-Dec-2007')
        
        for m in range(int((len(temp_date_df))/2 - 1)):
            m = m*2 + 2
            temp_date=['1']
            temp_date.extend(temp_date_df[m][:temp_date_df[m].find('-')].split())
            temp_date = '-'.join(temp_date)
            temp_date_list.append(temp_date)
        
        temp_sum["Date"] = pd.DataFrame({'Date': temp_date_list})
        temp_sum = temp_sum[['Date', 'PV Quantity', 'PV Output kW']]
        
        data_sum = temp_sum.copy()
        
    else:
        
        temp_sum = data.iloc[2:,27:-2].sum()
        temp_sum = pd.DataFrame(temp_sum.values.reshape(-1, 2), columns = ['PV Quantity', 'PV Output kW'])
        
        temp_date_df = data.iloc[1,27:-2]
        temp_date_list = []
        
        for m in range(int((len(temp_date_df))/2)):
            m *= 2
            temp_date=['1']
            temp_date.extend(temp_date_df[m][:temp_date_df[m].find('-')].split())
            temp_date = '-'.join(temp_date)
            temp_date_list.append(temp_date)
        
        temp_sum["Date"] = pd.DataFrame({'Date': temp_date_list})
        temp_sum = temp_sum[['Date', 'PV Quantity', 'PV Output kW']]
        
        data_sum = pd.concat([data_sum, temp_sum], ignore_index=True)
    
    data_sum["PV Quantity Cumsum"] = data_sum["PV Quantity"].cumsum()
    data_sum["PV Output kW Cumsum"] = data_sum["PV Output kW"].cumsum()

#%%

data_sum.to_csv('pv_installation_nsw.csv', index=False)
