library(tidyverse)
library(lubridate)


# set the directory
setwd(dirname(rstudioapi::getSourceEditorContext()$path))

# Read in the file
crime_bat <- readRDS("Crime3years.rds")

# Filter years using the filter method
two_year_crime <- crime_bat %>% filter(between(as_date(Date), 
                                               as_date("2018-01-01"),
                                               as_date("2018-01-01") + 730))

glimpse(two_year_crime)

two_year_crime_new <- two_year_crime %>% 
  mutate(hour = hour(two_year_crime$Date),week= weekdays(two_year_crime$Date),  
         month = month(two_year_crime$Date),year=year(two_year_crime$Date)) %>% 
  mutate(weeknum= strftime(Date, format = '%V')) %>%
  mutate(monthnum= strftime(Date, format = '%m'))




two_year_crime_monthly <- two_year_crime_new %>% 
  mutate(hour = hour(two_year_crime_new$Date), week=weekdays(two_year_crime_new$Date),
         month = month(two_year_crime_new$Date), year=year(two_year_crime_new$Date)) %>%
  group_by(monthnum, year) %>%
  summarize(case_monthly=sum(Battery)) %>%
  mutate(first=1)  %>%
  mutate(yearandmonth = as.Date(format(as.Date(paste(year, monthnum, 1, sep="."),"%Y.%m.%d"),
                                       "%Y-%m-%d"))) %>%
  mutate(myDate=as.Date(format(as.Date(paste(1,monthnum,year,sep="."),"%d.%m.%Y"),"%Y-%m-%d")))


two_year_crime_monthly <- 
  two_year_crime_monthly[two_year_crime_monthly$year != 2020, ]


two_year_crime_monthly <- arrange(two_year_crime_monthly,two_year_crime_monthly$year, 
                                  two_year_crime_monthly$monthnum)

glimpse(two_year_crime_monthly)

# graph the monthly

ggplot(two_year_crime_monthly, aes(x=yearandmonth, y=case_monthly)) +
  geom_point() + 
  geom_line() +
  xlab("Month") +
  ylab("Number of Grimes")+
  ggtitle("Battery Crime in Chicago") +
  scale_x_date(date_breaks = "2 month", date_labels = "%Y/%b")+
  theme(axis.text.x=element_text(angle=90, hjust=1)) +
  guides(color=guide_legend(title = "Year"))


