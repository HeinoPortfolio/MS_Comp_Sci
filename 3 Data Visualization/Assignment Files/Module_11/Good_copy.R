library(tidyverse)

setwd(dirname(rstudioapi::getSourceEditorContext()$path))

crime_bat <- readRDS("Crime3years.rds")

# Select two-year data
two_years = 365*24*2
start_date = 553
end_date = start_date + two_years - 1

two_year_crime <- crime_bat[start_date:end_date, ]

# Create new variables 
two_year_crime_new <- two_year_crime %>% 
  mutate(hour = hour(two_year_crime$Date),week= weekdays(two_year_crime$Date),  
         month = month(two_year_crime$Date),year=year(two_year_crime$Date)) %>% 
  mutate(weeknum= strftime(Date, format = '%V')) %>%
  mutate(monthnum= strftime(Date, format = '%m'))

two_year_crime_weekly <- two_year_crime_new %>% 
  group_by(weeknum,year) %>%
  summarize(case_weekly=sum(Battery)) %>%
  mutate(yearweek=paste0(year,weeknum))

two_year_crime_weekly%>%
  ggplot(aes(x = yearweek, y = case_weekly,group=1)) +
  geom_point(col = "maroon") + geom_line(col = "red") +
  labs(title = "Battery Crime from 2017-09-01 to 2019-08-31 in Chicago",
       x = "Week", y = "Number of Crimes")+
  scale_x_discrete(breaks = seq(min(two_year_crime_weekly$yearweek),
                                max(two_year_crime_weekly$yearweek),
                                10))

two_year_crime__monthly <- two_year_crime_new %>% 
  mutate(hour = hour(two_year_crime_new$Date), week=weekdays(two_year_crime_new$Date),
         month = month(two_year_crime_new$Date), year=year(two_year_crime_new$Date)) %>%
  group_by(monthnum, year) %>%
  summarize(case_monthly=sum(Battery)) %>%
  mutate(yearmonth=paste0(year, monthnum))

two_year_crime__monthly <- head(two_year_crime__monthly, -1)
#two_year_crime__monthly <- two_year_crime__monthly[apply(two_year_crime__monthly!= 0,
                                                       #  1, all),]
two_year_crime__monthly %>%
  ggplot(aes(x = yearmonth, y = case_monthly, group=1)) +
  geom_point(col = "maroon") + geom_line(col = "red") +
  labs(title = "Battery Crime from 2017-09-01 to 2019-08-31 in Chicago",
       x = "Week", y = "Number of Crimes")+
  scale_x_discrete(breaks = seq((min(two_year_crime__monthly$yearmonth)),
                                max(two_year_crime__monthly$yearmonth),
                                1))



