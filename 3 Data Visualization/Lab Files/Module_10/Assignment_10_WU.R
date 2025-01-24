library(tidyverse)

crime_bat <- readRDS("Crime3years.rds")

two_years = 365*24*2
start_date = 553
end_date = start_date + two_years - 1

#new_crime_bat <- crime_bat[start_date:end_date, ]
new_crime_bat <- head(crime_bat, 365*24*2)


bat_crime  <- new_crime_bat %>% 
  mutate(hour = hour(new_crime_bat$Date), week=weekdays(new_crime_bat$Date),
         month = month(new_crime_bat$Date), year=year(new_crime_bat$Date)) %>%
  mutate(monthnum = strftime(Date, format = '%m'))
         

#How to group the data into weekly (every 7 days) data
bat_monthly <- bat_crime %>% 
  group_by(year, monthnum) %>%
  summarize(case_monthly=sum(Battery)) %>%
  mutate(yearmonth=paste0(year, monthnum))


bat_monthly%>%
  ggplot(aes(x = yearmonth, y = case_monthly,group=1)) +
  geom_point(col = "maroon") + geom_line(col = "red") +
  labs(title = "Battery Crime from 2017-09-24 to 2019-09-24 in Chicago",
       x = "Week", y = "Number of Crimes")+
  scale_x_discrete(breaks = seq(min(bat_monthly$yearmonth),
                                max(bat_monthly$yearmonth),
                                10))


temp <- new_crime_bat[0:168, 2]









