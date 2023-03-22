library(dplyr)
library(GGally)

# Air temperature in New South Wales (as measured from the Bankstown Airport weather
# station). This data is sourced from the Australian Data Archive for Meteorology.
# Note: Unlike the total demand and forecast demand, the time interval between each
# observation may not be constant (i.e. half-hourly data). The variables are:

# DATETIME: Date time interval of each observation (dd/mm/yyyy hh:mm)
# TemperatureTEMPERATURE: Air temperature (°C)
# LOCATION: Location of a weather station (i.e., Bankstown weather station)

demand_temp_PV_data <- read.csv("C:\\Users\\AUZL503978\\Desktop\\UNSW\\2023_H2_ZZSC9020\\data\\demand_temp_PV_data.csv")#, stringsAsFactors = F)
demand_temp_PV_data$DATETIME <- as.POSIXct(demand_temp_PV_data$DATETIME,format="%Y-%m-%d")

ggpairs(demand_temp_PV_data)

demand_temp_PV_data.glm <- glm(TOTALDEMAND ~ .-PV.Quantity.Cumsum-PV.Output.kW.Cumsum-DATETIME, data = demand_temp_PV_data)
summary(demand_temp_PV_data.glm)
