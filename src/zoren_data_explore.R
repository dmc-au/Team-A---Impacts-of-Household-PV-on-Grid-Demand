library(dplyr)

# Air temperature in New South Wales (as measured from the Bankstown Airport weather
# station). This data is sourced from the Australian Data Archive for Meteorology.
# Note: Unlike the total demand and forecast demand, the time interval between each
# observation may not be constant (i.e. half-hourly data). The variables are:

# DATETIME: Date time interval of each observation (dd/mm/yyyy hh:mm)
# TemperatureTEMPERATURE: Air temperature (°C)
# LOCATION: Location of a weather station (i.e., Bankstown weather station)

temperature <- read.csv("C:\\Users\\AUZL503978\\Desktop\\UNSW\\2023_H2_ZZSC9020\\data\\temperature_nsw.csv")#, stringsAsFactors = F)
temperature$DATETIME <- as.POSIXct(temperature$DATETIME,format="%Y-%m-%d %H:%M:%S")

# There are outlier temperature readings (temp = -9999 degC). Instead of removing
# those rows, we replace those erroneous readings with the average of two adjacent
# measurements.
ols <- which(temperature$TEMPERATURE < -50)
for (i in ols) {
  temperature$TEMPERATURE[i] <- mean(temperature$TEMPERATURE[i-1], temperature$TEMPERATURE[i+1])
}

str(temperature)
summary(temperature)
#plot(temperature$DATETIME, temperature$TEMPERATURE)


# Total electricity demand, in 5 minutes increments for New South Wales. This data
# is sourced from the Market Management System database, which is published by the
# market operator from the National Electricity Market (NEM) system. The variables are:

# DATETIME: Date and time interval of each observation in the format (dd/mm/yyyy hh:mm)
# TOTALDEMAND: Total demand (MW)
# REGIONID: Region Identifier (i.e. NSW1)

demand <- read.csv("C:\\Users\\AUZL503978\\Desktop\\UNSW\\2023_H2_ZZSC9020\\data\\totaldemand_nsw.csv")
demand$DATETIME <- as.POSIXct(demand$DATETIME,format="%Y-%m-%d %H:%M:%S")
str(demand)
summary(demand)
#plot(demand$DATETIME, demand$TEMPERATURE)

forecast <- read.csv("C:\\Users\\AUZL503978\\Desktop\\UNSW\\2023_H2_ZZSC9020\\data\\forecastdemand_nsw.csv")
forecast$DATETIME <- as.POSIXct(forecast$DATETIME,format="%Y-%m-%d %H:%M:%S")
str(forecast)
summary(forecast)










