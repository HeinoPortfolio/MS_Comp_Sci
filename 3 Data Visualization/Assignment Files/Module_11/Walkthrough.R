library(tidyverse)

setwd(dirname(rstudioapi::getSourceEditorContext()$path))

crime_bat <- readRDS("Crime3years.rds")

## Select two-years
bat_train <- head(crime_bat, 365*24*2)

#Basic time series based on scatter plot
bat_train %>% ggplot(aes(x = Date, y = Battery)) +
  geom_point(col = "maroon") + 
  geom_line(col = "red") +
  labs(title = "Battery Crime from 2017-09-01 to 2019-08-31 in Chicago", 
       x = "Hourly", y = "Number of Crimes")


# Create new variables 
bat_train_new<-bat_train %>% 
  mutate(hour = hour(bat_train$Date),week= weekdays(bat_train$Date),  
         month = month(bat_train$Date),year=year(bat_train$Date)) %>% 
  mutate(weeknum= strftime(Date, format = '%V')) %>%
  mutate(monthnum= strftime(Date, format = '%m'))

bat_train_weekly <- bat_train_new %>% 
  group_by(weeknum,year) %>%
  summarize(case_weekly=sum(Battery)) %>%
  mutate(yearweek=paste0(year,weeknum))

bat_train_weekly%>%
  ggplot(aes(x = yearweek, y = case_weekly,group=1)) +
  geom_point(col = "maroon") + geom_line(col = "red") +
  labs(title = "Battery Crime from 2017-09-01 to 2019-08-31 in Chicago",
       x = "Week", y = "Number of Crimes")+
  scale_x_discrete(breaks = seq(min(bat_train_weekly$yearweek),
                                max(bat_train_weekly$yearweek),
                                10))

bat_monthly <- bat_train_new %>% 
  mutate(hour = hour(bat_train$Date), week=weekdays(bat_train$Date),
         month = month(bat_train$Date), year=year(bat_train$Date)) %>%
  group_by(monthnum, year) %>%
  summarize(case_monthly=sum(Battery)) %>%
  mutate(yearmonth=paste0(year, monthnum))

bat_monthly <- head(bat_monthly, -1)
bat_monthly <- bat_monthly[apply(bat_monthly!= 0, 1, all),]



bat_monthly%>%
  ggplot(aes(x = yearmonth, y = case_monthly, group=1)) +
  geom_point(col = "maroon") + geom_line(col = "red") +
  labs(title = "Battery Crime from 2017-09-01 to 2019-08-31 in Chicago",
       x = "Week", y = "Number of Crimes")+
  scale_x_discrete(breaks = seq((min(bat_monthly$yearmonth)),
                                max(bat_monthly$yearmonth),
                                1))


