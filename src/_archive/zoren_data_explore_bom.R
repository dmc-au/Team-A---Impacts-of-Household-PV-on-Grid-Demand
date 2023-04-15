library(dplyr)


alldata <- read.csv("C:\\Users\\AUZL503978\\Desktop\\UNSW\\2023_H2_ZZSC9020\\data\\all_data_rain.csv")
alldata <- alldata[complete.cases(alldata), ]
alldata$datetime <- as.Date(alldata$datetime, format="%d/%m/%Y")
str(alldata)
summary(alldata)

plot(alldata$Rainfall.amount..millimetres., alldata$demand_max)
plot(alldata$temp_max, alldata$demand_max)
plot(alldata$cum_output, alldata$demand_max)

# Fit glm to beofre 2020-01-01
alldata_train <- alldata[(alldata$datetime < "2020-01-01" ),]
alldata_test <- alldata[(alldata$datetime >= "2020-01-01" ),]


alldata.glm <- glm(demand_max ~ temp_max+cum_output+Rainfall.amount..millimetres., data = alldata_train)
summary(alldata.glm)

(1 - alldata.glm$deviance/alldata.glm$null.deviance)

pred_demand_max <- predict(alldata.glm, alldata_test, type="response")

dif <- (pred_demand_max - alldata_test$demand_max)/alldata_test$demand_max
plot(seq(1,nrow(alldata_test)), dif)









